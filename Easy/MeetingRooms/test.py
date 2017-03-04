class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def canAttendMeetings(self, intervals):
		if not intervals or len(intervals) == 0 or len(intervals) == 1:
			return True
		starts = []
		ends = []
		for interval in intervals:
			starts.append(interval.start)
			ends.append(interval.end)
		starts.sort()
		ends.sort()
		s = 1
		e = 0
		while s < len(starts) and e < len(ends):
			if starts[s] < ends[e]:
				return False
			s += 1
			e += 1
		return True

sol = Solution()
example = [Interval(s=0, e=30), Interval(s=5, e=10), Interval(s=15, e=20)]
print sol.canAttendMeetings(example)
