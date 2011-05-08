import logging
from compare.find import SimilarPair
import cutil

log = logging

def find_similar(
	doc_iterable,
	compare_func=cutil.jaccard,
	segmenter=None,
	set_builder=None,
	doc_key='id',
	duplicate_threshold=0.8
):
	segmented_docs = segmenter(doc_iterable)

	pairs = []
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
