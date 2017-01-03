class Solution(object):
	def canFinish(self, numCourses, prerequisites):
		graph = self.makeGraph(numCourses, prerequisites)
		degrees = self.compute_indegree(graph)
		for i in range(numCourses):
			j = 0
			while j < numCourses:
				if degrees[j] == 0:
					break
				j += 1
			if j == numCourses:
				return False
			degrees[j] = -1
			for neigh in graph[j]:
				degrees[neigh] -= 1
		return True

	def makeGraph(self, numCourses, prerequisites):
		graph = []
		for i in range(numCourses):
			graph.append(set())
		for each_prerequisite in prerequisites:
			graph[each_prerequisite[1]].add(each_prerequisite[0])
		return graph

	def compute_indegree(self, graph):
		degrees = [0] * len(graph)
		for neighbors in graph:
			for neigh in neighbors:
				degrees[neigh] += 1
		return degrees

sol = Solution()
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print sol.canFinish(numCourses, prerequisites)

numCourses2 = 2
prerequisites2 = [[1, 0]]
print sol.canFinish(numCourses2, prerequisites2)
