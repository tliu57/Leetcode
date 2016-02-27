class Solution(object):
	def gameOfLife(self, board):
		if not board or len(board) == 0:
			return
		m = len(board)
		n = len(board[0])
		for i in range(m):
			for j in range(n):
				lives = self.findSurroundLives(board, i, j, m, n)
				if board[i][j] == 1 and 2 <= lives <= 3:
					board[i][j] = 3
				if board[i][j] == 0 and lives == 3:
					board[i][j] = 2
		for i in range(m):
			for j in range(n):
				board[i][j] >>=1
		print board

	def findSurroundLives(self, board, i, j, m, n):
		lives = 0
		for x in range(max(i-1 ,0), min(i+1, m-1)+1):
			for y in range(max(j-1, 0), min(j+1, n-1)+1):
				lives += (board[x][y] & 1)
		lives -= (board[i][j] & 1)
		return lives

matrix = [ [ 0, 0, 0, 0],
	   [ 0, 1, 1, 0],
	   [ 0, 1, 1, 0],
	   [ 0, 0, 0, 0]
	 ]
sol = Solution()
sol.gameOfLife(matrix)
