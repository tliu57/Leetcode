class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e


class Solution(object):
	def minMeetingRooms(self, intervals):
		start = []
		end = []
		for interval in intervals:
			start.append(interval.start)
			end.append(interval.end)		
		start.sort()
		end.sort()
		s = 0
		e = 0
		available = 0
		numRooms = 0
		while s < len(start):
			if start[s] < end[e]:
				if available == 0:
					numRooms += 1
				else:
					available -= 1
				s += 1
			else:
				available  += 1
				e += 1
		return numRooms
		
intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]

# intervals = [Interval(9, 10), Interval(4, 9), Interval(4, 17)]
sol = Solution()
print sol.minMeetingRooms(intervals)	
