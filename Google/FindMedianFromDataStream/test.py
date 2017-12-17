from heapq import heappushpop, heappush, heappop

class MedianFinder(object):
    def __init__(self):
	self.minHeap = []
	self.maxHeap = []

    def addNum(self, num):
	smallest_of_max_heap = heappushpop(self.maxHeap, num)
	heappush(self.minHeap, -smallest_of_max_heap)
	if len(self.minHeap) > len(self.maxHeap):
		largest_of_min_heap = - heappop(self.minHeap)
		heappush(self.maxHeap, largest_of_min_heap)

    def findMedian(self):
	if len(self.minHeap) == len(self.maxHeap):
	    return float(self.maxHeap[0] - self.minHeap[0]) / float(2)
	else:
	    print self.maxHeap
	    return self.maxHeap[0]

sol = MedianFinder()
sol.addNum(1)
sol.addNum(2)
print sol.findMedian()
sol.addNum(3)
print sol.findMedian()
