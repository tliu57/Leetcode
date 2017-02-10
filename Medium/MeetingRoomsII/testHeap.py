import heapq
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def minMeetingRooms(self, intervals):
		intervals.sort(key=lambda x: x.start)
		heap = [] # stores the end time of intervals
		for i in intervals:
			if heap and i.start >= heap[0]:
				heapq.heapreplace(heap, i.end)
			else:
				heapq.heappush(heap, i.end)
		return len(heap)

sol = Solution()
print sol.minMeetingRooms([Interval(9, 10), Interval(4, 9), Interval(4, 17)])

