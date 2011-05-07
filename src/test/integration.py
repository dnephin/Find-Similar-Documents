"""
Integration tests.
"""
import csv

from compare import find
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

def c_print(pairs, raw1, raw2, key='id'):
	m = []
	m.append(map_by_key(raw1, key))
	m.append(map_by_key(raw2, key))
	for pair in sorted(pairs, key=lambda p: p.score, reverse=True):
		print "%s\n%s\n%s\n\n" % (
			pair,
			m[pair.doc1_source][pair.doc1],
			m[pair.doc2_source][pair.doc2]
		)

raw = read_file('./test/data/simple.txt')
seg = find.DefaultSegmenter('seg')
builder = find.DocumentPropertySetBuilder({'first': 'name', 'last': 'name', 'pow': 'pow'})
#pairs = find.find_similar(raw, segmenter=seg.segment, set_builder=builder.build_props, doc_key='num', duplicate_threshold=0.5)
#assert len(pairs), 4
#c_print(pairs, raw, 'num')

raw = read_file('./test/data/biz.txt')
seg = find.DefaultSegmenter('prov')
builder = find.DocumentPropertySetBuilder({'name': 'name', 'city': 'city', 'phone': 'phone', 'street': 'street'})
#pairs = find.find_similar(raw, segmenter=seg.segment, set_builder=builder.build_props, duplicate_threshold=0.5)
#print len(pairs)
#c_print(pairs, raw)

raw1 = read_file('./test/data/small1.txt')
raw2 = read_file('./test/data/small2.txt')
seg = find.DefaultSegmenter('prov')
builder = find.DocumentPropertySetBuilder({'name': 'name', 'city': 'city', 'phone': 'phone', 'street': 'street'})
pairs = find.find_similar_many([raw1, raw2], segmenter=seg.segment, set_builder=builder.build_props, duplicate_threshold=0.5)
print len(pairs)
c_print(pairs, raw1, raw2)

