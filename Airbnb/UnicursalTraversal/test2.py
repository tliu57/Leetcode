class Solution(object):
	def findUPoint(self, graph):
		res = []
		visited = set()
		for i in graph:
			if i not in visited:
				res.append(i)
				self.dfs(graph, visited, res, i, i)
		return res
	
	def dfs(self, graph, visited, res, i, start):
		visited.add(i)
		for next in graph[i]:
			if next in res:
				res.remove(next)
				res.append(start)
				continue
			if next in visited:
				continue
			self.dfs(graph, visited, res, next, start)
sol = Solution()
graph = {}
graph[1] = set([2])
graph[2] = set([1,3])
graph[3] = set([1])

graph2 = {}
graph2[1] = set([2])
graph2[2] = set([3])
graph2[3] = set([4])
graph2[4] = set([5])
graph2[5] = set([1])
graph2[6] = set([4])
print sol.findUPoint(graph2)
