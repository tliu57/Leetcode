intervals = [[1,3],[2,6],[3,4],[8,10],[15,18]]

class Solution():
	def merge(self, intervals):
		intervals = sorted(intervals)
		res = []
		intval_elem = intervals[0]
		total_len = len(intervals)
		for i in range(1, total_len):
			if intervals[i][0] > intval_elem[1]:
				res.append(intval_elem)
				intval_elem = intervals[i]
			else:
				intval_elem[1] = max(intval_elem[1], intervals[i][1])
		res.append(intval_elem)
		return res

sol = Solution()
print sol.merge(intervals)
