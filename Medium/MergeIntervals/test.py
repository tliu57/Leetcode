class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
                return []
        intervals.sort()
        start = intervals[0].start
        end = intervals[0].end
        result = []
        index = 1
        while index < len(intervals):
                if intervals[index].start < end:
                        end = max(end, intervals[index].end)
                else:
                        result.append([start, end])
                        start = intervals[index].start
                        end = intervals[index].end
                index += 1
        result.append([start, end])
        return result


intervals = [Interval(1, 4), Interval(2, 5)]
sol = Solution()
print sol.merge(intervals)
