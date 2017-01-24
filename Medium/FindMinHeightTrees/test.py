class Solution():
	def findMinHeightTrees(self, n, edges):
		if n == 1:
			return [0]
		graph_dict = [set() for i in range(n)]
		for edge in edges:
			graph_dict[edge[0]].add(edge[1])
			graph_dict[edge[1]].add(edge[0])
		print "graph_dict", graph_dict

		leaves = []
		for i in range(n):
			if len(graph_dict[i]) == 1:
				leaves.append(i)
		print "leaves is:", leaves
		
		while n > 2:
			n -= len(leaves)
			new_leaves = []
			for node in leaves:
				adj_node = graph_dict[node].pop()
				graph_dict[adj_node].remove(node)
				if len(graph_dict[adj_node]) == 1:
					new_leaves.append(adj_node)
			leaves = new_leaves

		return leaves
			

sol = Solution()
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print sol.findMinHeightTrees(n, edges)
