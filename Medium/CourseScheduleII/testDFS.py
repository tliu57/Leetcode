class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		graph = self.constructGraph(numCourses, prerequisites)
		return self.solveByDFS(numCourses, graph)

	def solveByDFS(self, numCourses, graph):
		visited = [False] * numCourses
		onStack = [False] * numCourses
		order = []
		for i in range(len(graph)):
			if not visited[i] and not self.hasOrder(i, graph, visited, onStack, order):
				return []
		visitOrder = [0] * len(graph)
		for i in range(len(order)):
			visitOrder[i] = order.pop()
		return visitOrder
				
	def hasOrder(self, index, graph, visited, onStack, order):
		visited[index] = True
		onStack[index] = True
		for desNode in graph[index]:
			if not visited[desNode]:
				if not self.hasOrder(desNode, graph, visited, onStack, order):
					return False
			elif onStack[desNode]:
				return False
		onStack[index] = False
		order.append(index)
		return True

	def constructGraph(self, numCourses, prerequisites):
		graph = []
		for i in range(numCourses):
			graph.append(set())
		for each_prerequisite in prerequisites:
			graph[each_prerequisite[1]].add(each_prerequisite[0])
		return graph

sol = Solution()
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

print sol.findOrder(numCourses, prerequisites)	
