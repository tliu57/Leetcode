PEOPLE = 0
ZOMBIE = 1
WALL = 2

class Solution():
	def getAffectionTime(self, matrix):
		if not matrix:
			return 0
		m = len(matrix)
		if m < 1:
			return 0
		n = len(matrix[0])
		peoples = 0
		queue = []
		for i in range(m):
			for j in range(n):
				if matrix[i][j] == PEOPLE:
					peoples += 1
				if matrix[i][j] == ZOMBIE:
					queue.append((i, j))

		days = 0
		if peoples == 0:
			return days
		while queue:
			days += 1
			q_size = len(queue)
			for i in range(q_size):
				curr_x, curr_y = queue.pop(i)
				dx = (1, 0, -1, 0)
				dy = (0, 1, 0, -1)
				for j in range(4):
					next_x = curr_x + dx[j]
					next_y = curr_y + dy[j]
					if not self.isPeople(next_x, next_y, matrix):
						continue
					else:
						matrix[next_x][next_y] = ZOMBIE
						peoples -= 1
						if peoples == 0:
							return days
						queue.append((next_x, next_y))
		return -1

	def isPeople(self, x, y, matrix):
		m = len(matrix)
		n = len(matrix[0])
		if x< 0 or y < 0 or x >= m or y >= n:
			return False
		return matrix[x][y] == PEOPLE

sol = Solution()
matrix = [
	  [0, 0, 0, 0],
	  [0, 0, 1, 0],
	  [1, 0, 2, 0],
	  [0, 2, 0, 1]
	] 
matrix1 = [
	   [0, 0],
	   [0, 2]
	]
print sol.getAffectionTime(matrix1)
							
