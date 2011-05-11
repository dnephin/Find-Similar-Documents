"""
 Common utility function.
"""
from math import sqrt

def jaccard(sl, sr):
	"""Find the Jaccard similarity coefficient of two sets."""
	union = sl | sr
	if not union:
		return 0.0
	return len(sl & sr) / float(len(union))


