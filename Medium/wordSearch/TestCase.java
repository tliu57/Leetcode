public class TestCase {
	public static void main(String[] args) {
		char[][] board = {
			{'A','B', 'C', 'E'},
			{'S','F', 'C', 'S'},
			{'A','D', 'E', 'E'},
		};

		Solution answer = new Solution();
		System.out.println(answer.exist(board, "see"));
	}
}
