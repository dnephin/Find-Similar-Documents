"""
 Common utility function.
"""
from math import sqrt


def pearson(v1, v2):
	"""Find the Person correlation for two lists of numbers."""
	sum1, sum2 = sum(v1), sum(v2)

	sum1Sq = sum([ pow(v, 2) for v in v1])
	sum2Sq = sum([ pow(v, 2) for v in v2])

	pSum = sum([ v1[i] * v2[i] for i in xrange(len(v1))])
	num = pSum-(sum1 * sum2 / len(v1))
	den = sqrt((sum1Sq - pow(sum1, 2) / len(v1)) * (sum2Sq - pow(sum2, 2) / len(v1)))
	if not den: 
		return 0
	return 1.0 - num / den


def jaccard(sl, sr):
	"""Find the Jaccard similarity coefficient of two sets."""
	union = sl | sr
	if not union:
		return 0.0
	return len(sl & sr) / float(len(union))


