import collections
class Solution(object):
	def countComponents(self, n, edges):
		edges.sort()
		roots = [0] * n
		for i in range(n):
			roots[i] = i
		for edge in edges:
			root1 = self.findRoot(roots, edge[0])
			root2 = self.findRoot(roots, edge[1])
			if root1 != root2:
				roots[root1] = root2
				n -= 1
		return n
		
	def findRoot(self, roots, id):
		while roots[id] != id:
			roots[id] = roots[roots[id]]
			id = roots[id]
		return id
	
sol = Solution()
edges = [[0,1], [1,2], [0,2], [3,4]]
print sol.countComponents(5, edges)

edges2 = [[0,1], [1,2], [3,4]]
print sol.countComponents(5, edges2)
