class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		graph = self.makeGraph(numCourses, prerequisites)
		print "graph is:", graph
		degrees = self.computeIndegree(graph)
		print "degree is:", degrees
		order = []
		toVisit = []
		for i in range(len(degrees)):
			if degrees[i] == 0:
				toVisit.append(i)
		while toVisit:
			print "toVisite is:", toVisit
			fromNode = toVisit.pop()
			print "fromNode is:", fromNode
			order.append(fromNode)
			for toNode in graph[fromNode]:
				degrees[toNode] -= 1
				if degrees[toNode] == 0:
					toVisit.append(toNode)
		print "order is:", order
		return order if len(order) == len(degrees) else []

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
