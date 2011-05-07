"""
Integration tests.
"""
import csv

from compare import find
from compare import util
from pprint import pprint


def read_file(file):
	reader = csv.reader(open(file, 'r'),)
	doc_list = []
	header = [h.strip() for h in reader.next()]
	for row in reader:
		doc_list.append(dict(((header[i], item.strip()) for i, item in enumerate(row))))

	return doc_list


def map_by_key(seq, key):
	return dict(((item[key], item) for item in seq))

raw = read_file('./test/data/simple.txt')
seg = find.DefaultSegmenter('seg')
builder = find.DocumentPropertySetBuilder({'first': 'name', 'last': 'name', 'pow': 'pow'})
pairs = find.find_similar_single(raw, segmenter=seg, set_builder=builder, doc_key='num', duplicate_threshold=-1)

m = map_by_key(raw, 'num')
for pair in sorted(pairs, key=lambda p: p.score, reverse=True):
	print "%s\n%s\n%s\n\n" % (
		pair,
		m[pair.doc1],
		m[pair.doc2]
	)

print len(pairs)
