# Capture all regions surrounded by 'X'. A region is captured by flipping all
# 'O's into 'X's in that surrounded region.
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
# X X X X
# X X X X
# X X X X
# X O X X

class Solution(object):
	def FlipSurroundedRegion(self, board):
	# input: char[][] board
	# output: char[][] board
		m = len(board)
		if m < 1:
			return board
			
		n = len(board[0])
		if m < 2 or n < 2:
			return board
		for i in range(m):
			self.bfs(board, i, 0)
			self.bfs(board, i, n-1)
		for j in range(n):
			self.bfs(board, 0, j)
			self.bfs(board, m-1, j)

		for i in range(m):
			for j in range(n):
				if board[i][j] == 'O':
					board[i][j] = 'X'
				if board[i][j] == '#':
					board[i][j] = 'O'
		return board
	def bfs(self, board, i , j):
		queue = []
		self.visit(board, i , j , queue)
		while len(queue) != 0:
			pos = queue.pop()
			x = pos /len(board[0])
			y = pos % len(board[0])
			self.visit(board, x - 1, y , queue)
			self.visit(board, x, y+1, queue)
			self.visit(board, x + 1, y , queue)
			self.visit(board, x, y-1, queue)
	
	def visit(self, board, i, j, queue):
		if i < 0 or j < 0 or i > len(board) - 1 or j > len(board) - 1 or board[i][j] != 'O':
			return
		else:
			board[i][j] = '#'
			queue.append(i * len(board[0]) + j)


sol = Solution()
board = [['X','X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
print sol.FlipSurroundedRegion(board)
