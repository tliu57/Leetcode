
public class main {
	public static void main(String[] args) {
		char[][] grid = {
			{'1', '1', '1', '1', '0'},
			{'1', '1', '0', '1', '0'},
			{'1', '1', '0', '0', '0'},
			{'0', '0', '0', '0', '0'},
		};
		
		Solution answer = new Solution();
		System.out.println(answer.NumIslands(grid));
	}
}
