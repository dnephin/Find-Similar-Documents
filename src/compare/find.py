
from compare import util
import itertools
import logging
from collections import defaultdict

log = logging

class DefaultSegmenter(object):
	"""Segment a list of dicts using key as the segmentation point."""

	def __init__(self, key):
		self.key = key

	def segment(self, document_list):
		"""Return a dict of segmentation key to a list of documents from
		document_list that belong in that segment.
		"""
		segment_map = defaultdict(list)
		for document in document_list:
			if self.key not in document:
				log.warn("%s missing from doc: %s" % (self.key, document))
				continue
			segment_map[document[self.key]].append(document)
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
		# TODO: print with source
		return "SimilarPair(%s, %s, score=%s)" % (self.doc1, self.doc2, self.score)

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

			
def find_similar(doc_lists, set_compare_func=util.jaccard, segmenter=None):
	"""
	Find documents in a set of documents (or many sets) that are similar.
	"""
	segmented_list = [segmenter.segment(dl) for dl in doc_lists]

	segment_keys = set((seg_doc.keys() for seg_doc in util.xflatten(segmented_list)))

	for key in segment_keys:
		for doc_list_combo in itertools.combinations(segmented_list, 2):
			pass


def find_similar_single(
	doc_list, 
	set_compare_func=util.jaccard, 
	segmenter=None, 
	set_builder=None, 
	doc_key='id',
	duplicate_threshold=0.8
):
	segmented_docs = segmenter.segment(doc_list)

	pairs = []
	for key, segment in segmented_docs.iteritems():
		log.info("Starting segment %s" % (key))
		
		# Convert documents to properties and compare
		doc_as_props = {}
		for document in segment:
			doc_props = set_builder.build_props(document)

			for doc_id, other_prop_set in doc_as_props.iteritems():
				score = set_compare_func(doc_props, other_prop_set)
				if score > duplicate_threshold:
					pairs.append(SimilarPair(doc_id, document[doc_key], score))

			doc_as_props[document[doc_key]] = doc_props
	return pairs

