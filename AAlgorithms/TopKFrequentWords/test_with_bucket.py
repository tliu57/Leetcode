class Solution(object):
    def topKFrequent(self, words, K):
	n = len(words)
	bucket = [[] for _ in range(n+1)]
	d = {}
	for word in words:
		if word not in d:
			d[word] = 1
		else:
			d[word] += 1
	for elem in d:
		frequency = d[elem]
		bucket[frequency].append(elem)
		bucket[frequency].sort()
        result = []
	index = len(bucket) - 1
	while len(result) < K and index >= 0:
		while len(bucket[index]) == 0:
			index -= 1
		for each_word in bucket[index]:
			result.append(each_word)
    			if len(result) >= K:
				return result
		index -= 1
	return result

sol = Solution()
# print sol.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
print sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
