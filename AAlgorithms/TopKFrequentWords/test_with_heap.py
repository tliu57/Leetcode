import collections
import heapq
class Element(object):
    def __init__(self, count, word):
	self.count = count
	self.word = word

    def __lt__(self, other):
	if self.count == other.count:
		return self.word > other.word
	return self.count < other.count

    def __eq__(self, other):
	return self.count == other.count and self.word == other.word

class Solution(object):
    def topKFrequent(self, words, k):
	counts = collections.Counter(words)
	freqs = []
	heapq.heapify(freqs)
	for word, count in counts.items():
	    heapq.heappush(freqs, (Element(count, word), word))
	    if len(freqs) > k:
	    	poped = heapq.heappop(freqs)
		print poped


	res = []
	for _ in range(k):
	    res.append(heapq.heappop(freqs)[1])
	return res[::-1]

sol = Solution()
print sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
