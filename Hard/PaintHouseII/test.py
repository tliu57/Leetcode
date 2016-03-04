import sys

print float('inf')

class Solution(object):
	def minCostII(self, costs):
		n = len(costs)
		if not costs or n == 0:
			return 0
		k = len(costs[0])
		min1 = -1
		min2 = -1
		last1, last2 = self.findTwoSmallest(costs[0])
		for i in range(1, len(costs)):
			for j in range(k):
				if i > 1:
					last1 = min1
					last2 = min2
				if j != last1:
					costs[i][j] += costs[i-1][last1] if last1 >= 0 else 0
				else:
					costs[i][j] += costs[i-1][last2] if last2 >= 0 else 0
				if min1 < 0 or costs[i][j] < costs[i][min1]:
			 		min2 = min1
			 		min1 = j
				elif min2 < 0 or costs[i][j] < costs[i][min2]:
			 		min2 = j
		return costs[n-1][min1]

	def findTwoSmallest(self, array):
		assert len(array)>=2
		smallest, second_smallest = sys.maxint, sys.maxint
		for c in array:
			if c <= smallest:
				smallest, second_smallest = c, smallest
			else:
				second_smallest = min(c, second_smallest)
		return array.index(smallest), array.index(second_smallest)
costs = []
costs.append([20, 19, 11, 13, 12, 16, 16, 17, 15, 9, 5, 18])
costs.append([3, 8, 15, 17, 19, 8, 18, 3, 11, 6, 7, 12])
costs.append([15, 4, 11, 1, 18, 2, 10, 9, 3, 6, 4, 15])

sol = Solution()
print sol.minCostII(costs)
