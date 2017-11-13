class Solution:
	def knightShortestPath(self, matrix, source, destination):
		if not matrix:
			return -1
		m = len(matrix)
		if m < 1:
			return -1
		n = len(matrix[0])
		steps = 0
		visited = set()
		queue = []
		dx = [1, 2, -1, -2, 1, 2, -1, -2]
		dy = [2, 1, 2, 1, -2, -1, -2, -1]
		queue.append(source)
		while queue:
			steps += 1
			q_size = len(queue)
			for i in range(q_size):
				curr_x, curr_y = queue.pop(i)
				for i in range(len(dx)):
					next_x = curr_x + dx[i]
					next_y = curr_y + dy[i]
					if next_x, next_y == source:
						return counts
					elif self.isValid(next_x, next_y):
						if (next_x, next_y) in visited:
							continue
						visited.append((next_x, next_y))
					
