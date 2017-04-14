class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution:
	def cloneGraph(self, node):
		if not node:
			return None
		newNode = UndirectedGraphNode(node.label)
		map = {newNode.label: newNode}
		queue = [node]
		while queue:
			node = queue.pop(0)
			for n in node.neighbors:
				if n.label not in map:
					map[n.label] = UndirectedGraphNode(n.label)
					queue.append(n)
				map[node.label].neighbors.append(map[n.label])
		return newNode


no1 = UndirectedGraphNode(1)
no0 = UndirectedGraphNode(0)
no2 = UndirectedGraphNode(2)
no0.neighbors = [no1, no2]
no1.neighbors = [no2]
no2.neighbors = [no2]

sol = Solution()
new_node = sol.cloneGraph(no0)
new0 = new_node.neighbors[0]
new1 = new_node.neighbors[1]
print new0.label
print new1.label
neighbor_0 = new0.neighbors
print neighbor_0[0].label
neighbor_1 = new1.neighbors[0]
print neighbor_1.label				
				
