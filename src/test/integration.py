"""
Integration tests.
"""
import csv

from compare import find
import cfind

def read_file(file):
	reader = csv.reader(open(file, 'r'),)
	doc_list = []
	header = [h.strip() for h in reader.next()]
	for row in reader:
		doc_list.append(dict(((header[i], item.strip()) for i, item in enumerate(row))))

	return doc_list

def map_by_key(seq, key):
	return dict(((item[key], item) for item in seq))

def c_print(pairs, raw, key='id'):
	m = [map_by_key(r, key) for r in raw]
	for pair in sorted(pairs, key=lambda p: p.score, reverse=True):
		print "%s\n%s\n%s\n\n" % (
			pair,
			m[pair.doc1_source or 0][pair.doc1],
			m[pair.doc2_source or 0][pair.doc2]
		)

raw = read_file('./test/data/simple.txt')
seg = find.DefaultSegmenter('prov')
builder = find.DocumentPropertySetBuilder({'first': 'name', 'last': 'name', 'pow': 'pow'})
#pairs = find.find_similar(raw, segmenter=seg.segment, set_builder=builder.build_props, doc_key='num', duplicate_threshold=0.5)
#assert len(pairs), 4
#c_print(pairs, raw, 'num')

#raw = read_file('./test/data/100k.txt')
#seg = find.MultiSegmenter(['prov'])
#builder = find.DocumentPropertySetBuilder({'name': 'name', 'city': 'city', 'phone': 'phone', 'street': 'street'})
#pairs = cfind.find_similar(raw, segmenter=seg.segment, set_builder=builder.build_props, duplicate_threshold=0.5)
#print len(pairs)
#c_print(pairs, [raw])


raw = [read_file('./test/data/small%s.txt' % i) for i in xrange(1,5)]
seg = find.DefaultSegmenter('prov')
builder = find.DocumentPropertySetBuilder({'name': 'name', 'city': 'city', 'phone': 'phone', 'street': 'street'})
#pairs = find.find_similar_many(raw, segmenter=seg.segment, set_builder=builder.build_props, duplicate_threshold=0.5)
#print len(pairs)
#c_print(pairs, raw)


raw = read_file('./test/data/100k.txt')
builder = find.DocumentPropertySetBuilder({'name': 'name', 'city': 'city', 'phone': 'phone', 'street': 'street'})
pairs = find.find_probably(raw, set_builder=builder.build_props, max_prop_freq=2000, threshold=0.5)

#for pair in pairs:
#	print "Pair(%s %s %s)\n%s\n%s" % (pair.doc1['id'], pair.doc2['id'], pair.score, pair.doc1, pair.doc2)

from pprint import pprint
reduce = find.reduce(pairs)
pprint(reduce.items())
print len(reduce)