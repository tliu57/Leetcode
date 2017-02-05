class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	def insert(self, intervals, newInterval):
		result = []
		i = 0
		while i < len(intervals) and intervals[i].end < newInterval.start:
			result.append(intervals[i])
			i += 1
		while i < len(intervals) and intervals[i].start <= newInterval.end:
			newInterval = Interval(min(intervals[i].start, newInterval.start), max(intervals[i].end, newInterval.end))
			i += 1
		if newInterval not in result:
			result.append(newInterval)
		while i < len(intervals):
			result.append(intervals[i])
			i += 1
		return result

# test_intervals = [Interval(s=1, e=2), Interval(s=3, e=5), Interval(s=6, e=7), Interval(s=8, e=10), Interval(s=12, e=16)]
# newInterval = Interval(s=4, e=9)

test_intervals = []
newInterval = Interval(s=5, e=7)

# test_intervals = [Interval(1, 5)]
# newInterval = Interval(2, 3)

# test_intervals = [Interval(1, 5)]
# newInterval = Interval(0, 1)

# test_intervals = [Interval(1, 5)]
# newInterval = Interval(0, 0)
sol = Solution()
new_list = sol.insert(test_intervals, newInterval)
for each_interval in new_list:
	print "[", each_interval.start, each_interval.end, "]"
