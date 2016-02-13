class Solution(object):
	def countComponents(self, n, edges):
		edges.sort()
		counter = 1
		for i in range(1, len(edges)):
			if edges[i][0] != edges[i-1][1]:
				counter += 1
		return counter

sol = Solution()
edges = [[0,1], [1,2], [2,3], [3,4]]
print sol.countComponents(5, edges)

