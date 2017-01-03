class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		graph = self.makeGraph(numCourses, prerequisites)
		degrees = self.computeIndegree(graph)
		order = [0] * numCourses
		toVisit = []
		for i in range(len(degrees)):
			if degrees[i] == 0:
				toVisit.append(i)

		visited = 0
		while toVisit:
			fromNode = toVisit.pop()
			order[visited] = fromNode
			visited += 1
			for toNode in graph[fromNode]:
				degrees[toNode] -= 1
				if degrees[toNode] == 0:
					toVisit.append(toNode)
		return order if visited == len(degrees) else []

	def makeGraph(self, numCourses, prerequisites):
		graph = []
		for i in range(numCourses):
			graph.append(set())
		for each_prerequisite in prerequisites:
			graph[each_prerequisite[1]].add(each_prerequisite[0])
		return graph

	def computeIndegree(self, graph):
		degrees = [0] * len(graph)
		for neighbors in graph:
			for neigh in neighbors:
				degrees[neigh] += 1
		return degrees

sol = Solution()
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print sol.findOrder(numCourses, prerequisites)
