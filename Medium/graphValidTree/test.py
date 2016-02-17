import collections
n = 5
edges = [[0,1], [1,2], [2,3], [1,3], [1, 4]]

class Solution(object):
	def validTree(self, n, edges):
		diction = {i:set() for i in range(n)}
		for i, j in edges:
			diction[i].add(j)
			diction[j].add(i)
		que = []
		que.append(diction.keys()[0])
		visited = collections.defaultdict(int)
		while que:
			node = que.pop()
			if visited[node] == 1:
				return False
			visited[node] = 1
			for i in diction[node]:
				que.append(i)
				diction[i].remove(node)
			del diction[node]
		return not diction

sol = Solution()
print sol.validTree(n, edges)
