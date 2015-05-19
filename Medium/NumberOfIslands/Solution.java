public class Solution {
	public int NumIslands(char[][] grid) {
		if(grid == null || grid.length == 0 || grid[0].length == 0)	return 0;
		int numRows = grid.length;
		int numCols = grid[0].length;
		int res = 0;
		for(int i = 0 ; i < numRows; i++) {
			for(int j = 0 ; j < numCols; j++) {
				if(grid[i][j] == '1') {
					dfs(grid, i, j, numRows, numCols);
					res++;
				}
			}
		}
		return res;
	}

	public void dfs(char[][] grid, int row, int col, int numRows, int numCols) {
	if(row < 0 || row >= numRows || col < 0 || col >= numCols)	return;
	if(grid[row][col]!= '1')	return;
	grid[row][col] = 'M';
	dfs(grid, row-1, col, numRows, numCols);
	dfs(grid, row, col-1, numRows, numCols);
	dfs(grid, row+1, col, numRows, numCols);
	dfs(grid, row, col+1, numRows, numCols);
	} 
}
