class Solution(object):
    def exist(self, board, word):
	m = len(board)
	if m < 1:
		return False
	n = len(board[0])
	for i in range(m):
	    for j in range(n):
		if self.dfs(board, word, i, j, 0):
		    return True
	return False

    def dfs(self, board, word, i, j, pos):
	if pos == len(word):
	    return True
	if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[pos]:
	    return False
	c = word[pos]
	board[i][j] = "#"
	result = self.dfs(board, word, i-1, j, pos+1) or self.dfs(board, word, i, j-1, pos+1) or self.dfs(board, word, i+1, j, pos+1) or self.dfs(board, word, i, j+1, pos + 1)
	board[i][j] = c
	return result

sol = Solution()
board = [
	 ['A', 'B', 'C', 'E'],
	 ['S', 'F', 'C', 'S'],
	 ['A', 'D', 'E', 'E']

]
print sol.exist(board, 'ABCB')
print sol.exist(board, "SEE")
print sol.exist(board, "ABCCED")
