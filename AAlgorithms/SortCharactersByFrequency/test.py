import operator

class Solution(object):
    def frequencySort(self, s):
	d = {}
	for c in s:
	    if c not in d:
	    	d[c] = 1
	    else:
	    	d[c] += 1
	nStr = ""
	sorted_d = sorted(d.items(), key = operator.itemgetter(1))
	print sorted_d
    	for key, value in sorted_d[::-1]:
	    nStr += key * value
	return nStr

sol = Solution()
print sol.frequencySort("tree")
print sol.frequencySort("cccaaa")
print sol.frequencySort("Aabb")

class Solution2(object):
    def frequencySort(self, s):
	d = {}
	for c in s:
	    if c not in d:
	    	d[c] = 1
	    else:
	    	d[c] += 1
	bucket = ["" for _ in range(len(s) + 1)]
	for elem in d:
		bucket[d[elem]] += elem * d[elem]
	n_str = ""
	print bucket
	for string in reversed(bucket):
		n_str += string
	return n_str

sol = Solution2()
print sol.frequencySort("tree")
