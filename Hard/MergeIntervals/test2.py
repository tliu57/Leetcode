class Interval():
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution():
	def merge(self, intervals):
		if len(intervals) == 0:
			return intervals
		intervals = sorted(intervals, key = lambda interval:interval.start)
		res = []
		elem = intervals[0]
		length = len(intervals)
		for i in range(1, length):
			if intervals[i].start > elem.end:
				res.append(elem)
				elem = intervals[i]
			else:
				elem.end = max(elem.end, intervals[i].end)
				print elem.start
				print elem.end
		res.append(elem)
		return res

intervals = [Interval(s=1, e=4)]
intervals.append(Interval(s=1, e=5))
sol = Solution()
print sol.merge(intervals)
