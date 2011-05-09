"""
 Find similar (or possibly duplicate) documents in a list of one or more
 documents.  This is accomplished by turning each document into a set
 of properties (propsets).  Document propsets are then compared (using
 jaccard index by default) to find the similarity between then.  If
 that value is greater then a threshold, then those documents are considered
 to be similar, and are returned as a pair.

 Author: Daniel Nephin
 
"""
import itertools
import logging
from collections import defaultdict
import cutil

log = logging

class DefaultSegmenter(object):
	"""Segment a list of dicts using key as the segmentation point."""

	def __init__(self, key):
		self.key = key

	def segment(self, document_list, key=None):
		"""Return a dict of segmentation key to a list of documents from
		document_list that belong in that segment.
		"""
		key = key or self.key

		segment_map = defaultdict(list)
		for document in document_list:
			if key not in document:
				log.warn("%s missing from doc: %s" % (key, document))
				continue
			segment_map[document[key]].append(document)

		def only_two_or_more(t_value_list):
			return len(t_value_list[1]) > 1
		return itertools.ifilter(only_two_or_more, segment_map.iteritems())

class MultiSegmenter(DefaultSegmenter):
	"""Segment a list of dicts on many keys. Documents can be returned more
	then once if they more then once key is used.
	"""

	def __init__(self, keys):
		self.keys = keys

	def segment(self, document_list):
		segment_map = {}
		for key in self.keys:
			key_segment_map = super(MultiSegmenter, self).segment(
				document_list,
				key=key
			)
			segment_map.update(key_segment_map)
		return segment_map



class SimilarPair(object):
	"""A single structure which holds ids of documents which are similar."""

	def __init__(self, doc1, doc2, score, doc1_source=None, doc2_source=None):
		self.doc1 = doc1
		self.doc2 = doc2
		self.doc1_source = doc1_source
		self.doc2_source = doc2_source
		self.score = score

	def __repr__(self):
		ss1 = "source(%s):" % self.doc1_source if self.doc1_source is not None else ""
		ss2 = "source(%s):" % self.doc2_source if self.doc2_source is not None else ""
		return "SimilarPair(%s%s, %s%s, score=%s)" % (
			ss1, self.doc1, ss2, self.doc2, self.score)

	@classmethod
	def for_docs(cls, source1, source2):
		"""Return a generator method to create SimilarPair objects whos
		source are already defined."""
		def gen_pair(doc1, doc2, score):
			return SimilarPair(doc1, doc2, score, source1, source2)
		return gen_pair


class DocumentPropertySetBuilder(object):
	"""Build a set of properties from a dictionary."""
	
	def __init__(self, field_map):
		"""
		field_map:  a dict of keys in the document dict to the propery name
		to use for that key in the prop set this class builds.
		
		Example:
		DocumentPropertySetBuilder(
			{'address1': 'addr', 'address2': 'addr', 'phone': 'phone'}
		)
		"""
		self.field_map = field_map

	def build_props(self, doc):
		"""Return a set of properties mapped from a dict."""
		props = set()
		for key, value in self.field_map.iteritems():
			if not key in doc:
				continue
			# TODO: could this be split some other way?
			prop_set = ('%s::%s' % (self.field_map[key], v) for v in doc[key].split())
			props.update(prop_set)
		return props

def find_similar(
	doc_iterable, 
	compare_func=cutil.jaccard,
	segmenter=None, 
	set_builder=None, 
	doc_key='id',
	duplicate_threshold=0.8
):
	"""
	Find similar documents in a list.

	doc_iterable: 
		an iterable that contains dictionaries
	compare_func:
		a function which takes two sets and returns a score of their
		similarity (1 is highest, 0 is lowest)
	segmenter:
		a function which takes an iterable and returns segments
	set_builder:
		a function which builds and returns a property set for a document
	doc_key:
		key in the document dictionary that uniquely identifies the document
	duplicate_threshold:
		minimum score required for a pair to be considered a duplicate
	"""
	segmented_docs = segmenter(doc_iterable)

	pairs = []
	for key, segment in segmented_docs.iteritems():
		log.info("Starting segment %s" % key)
		
		# Convert documents to properties and compare
		doc_as_props = {}
		for document in segment:
			doc_props = set_builder(document)

			for doc_id, other_prop_set in doc_as_props.iteritems():
				score = compare_func(doc_props, other_prop_set)
				if score > duplicate_threshold:
					pairs.append(SimilarPair(doc_id, document[doc_key], score))

			doc_as_props[document[doc_key]] = doc_props
	return pairs



def find_similar_many(
	list_doc_iterable,
	compare_func=cutil.jaccard,
	segmenter=None,
	set_builder=None,
	doc_key='id',
	duplicate_threshold=0.8
):
	"""
	Find similar documents between the list of document lists.

	list_doc_iterable:
		an iterable that contains sequences of dictionaries
	compare_func:
		a function which takes two sets and returns a score of their
		similarity (1 is highest, 0 is lowest)
	segmenter:
		a function which takes an iterable and returns segments
	set_builder:
		a function which builds and returns a property set for a document
	doc_key:
		key in the document dictionary that uniquely identifies the document
	duplicate_threshold:
		minimum score required for a pair to be considered a duplicate
	"""
	list_segmented_lists = [segmenter(dl) for dl in list_doc_iterable]

	segment_keys = set(
		itertools.chain(
			*(segment_map.keys() for segment_map in list_segmented_lists)
		)
	)

	pairs = []
	for segment_key in segment_keys:
		log.info("Starting segment %s" % segment_key)

		# get documents as prop_sets
		list_propset_lists = []
		for document_list in (segments[segment_key] for segments in list_segmented_lists):
			propset_list = [set_builder(doc) for doc in document_list]
			list_propset_lists.append(propset_list)

		for left_list_id, right_list_id in itertools.combinations(xrange(len(list_propset_lists)), 2):
			# Create a class factory for SimilarPairs of these documents
			pair_factory = SimilarPair.for_docs(left_list_id, right_list_id)
			left_propset_list = list_propset_lists[left_list_id]
			right_propset_list =  list_propset_lists[right_list_id]

			# n^2 sucks, but what are you going to do ?
			for left_idx, left_propset in enumerate(left_propset_list):
				for right_idx, right_propset in enumerate(right_propset_list):
					score = compare_func(left_propset, right_propset)
					if score > duplicate_threshold:
						pairs.append(pair_factory(
							list_segmented_lists[left_list_id][segment_key][left_idx][doc_key],
							list_segmented_lists[right_list_id][segment_key][right_idx][doc_key],
							score
						))
	return pairs
