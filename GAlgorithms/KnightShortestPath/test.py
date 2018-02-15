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
			q_size = len(queue)
			for i in range(q_size):
				curr_x, curr_y = queue.pop(i)
				visited.add((curr_x, curr_y))
				if (curr_x, curr_y) == destination:
					return steps
				for i in range(len(dx)):
					next_x = curr_x + dx[i]
					next_y = curr_y + dy[i]
					if self.isValid(next_x, next_y, matrix):
						if (next_x, next_y) in visited:
							continue
						queue.append((next_x, next_y))
			steps += 1

	def isValid(self, x, y, matrix):
		m = len(matrix)
		n = len(matrix[0])
		if x < 0 or y < 0 or x >= m or y >= n:
			return False
		if matrix[x][y] == 1:
			return False
		else:
			return True

sol = Solution()
matrix = [
	  [0, 0, 0],
	  [0, 0, 0],
	  [0, 0, 0]
]
source = (2, 0)
destination = (2, 2)
matrix1 = [
	   [0, 1, 0],
	   [0, 0, 0],
	   [0, 0, 0]
]
print sol.knightShortestPath(matrix1, source, destination)
