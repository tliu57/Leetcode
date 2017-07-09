class TVertex(object):
	def __init__(self, val):
		self.val = val
		self.incoming = set()

class Solution(object):
	def minTravel(self, mapTravel):
		graph = {}
		sourceMap = {}
		for i in range(len(mapTravel)):
			curr = mapTravel[i]
			if curr[0] not in graph:
				graph[curr[0]] = TVertex(curr[0])
			if curr[1] not in graph:
				graph[curr[1]] = TVertex(curr[1])
			graph[curr[1]].incoming.add(curr[0])
		
		visited = set()
		results = set()
		
		for key in graph:
			self.dfs(visited, graph, key, graph[key], sourceMap)
		
		print "xxx, sourceMap is:", sourceMap	
		for key in sourceMap:
			if sourceMap[key] not in results:
				results.add(sourceMap[key])
		return list(results)

	def dfs(self, visited, graph, key, vertex, sourceMap):
		if vertex.val in visited:
			return
		visited.add(vertex.val)
		sourceMap[key] = vertex.val
		for prevNode in vertex.incoming:
			prevVertex = graph[prevNode]
			self.dfs(visited, graph, key, prevVertex, sourceMap)
		visited.remove(vertex.val)


sol = Solution()
mapTravel = [
		[0, 1],
		[0, 2],
		[2, 3],
		[2, 4],
		[4, 5],
		[5, 6],
		[7, 3]
]
cycleTravel = [
		[0, 1],
		[1, 2],
		[2, 3],
		[3, 4],
		[4, 5],
		[5, 6],
		[6, 7],
		[7, 0],
		[6, 8]
]
print sol.minTravel(cycleTravel)




