/* Given board = 
   [
   	["ABCE"],
	["SFCS"],
	["ADEE"]
   ]

  word = "ABCCED"	returns true
  word = "SEE"		returns true
  word = "ABCB"		returns false
*/

public class Solution {
	public boolean exist(char[][] board, String word) {
		if(board == null || board.length == 0 || board[0].length == 0)	return false;
		if(word == null || word.length() == 0) return true;

		for(int i = 0 ; i < board.length ; i++) {
			for(int j = 0 ; j < board[0].length ; j++) {
				if(board[i][j] == word.charAt(0)) {
						if(dfs(board, word, i , j , 0))	return true;
						}
			}
		}
		return false;
	}

	private boolean dfs(char[][] board, String word, int i , int j , int n) {
		if(n == word.length())	return true;
		if(i < 0 || j < 0 || i >= board.length || j >= board[0].length || board[i][j] != word.charAt(n))	return false;
		board[i][j] = '#';
		boolean res = dfs(board, word, i-1, j , n+1) || dfs(board, word, i+1, j, n+1) || dfs(board, word, i, j-1, n+1) || dfs(board, word, i, j+1, n+1);
		board[i][j] = word.charAt(n);
		return res;
	}
}
