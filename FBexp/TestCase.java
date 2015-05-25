public class TestCase {
	public static void main(String[] args) {
		String order = "ACEBDF";
		String input = "BECAAFD";
		Solution answer = new Solution();
		System.out.println(answer.sortString(order, input));
	}
}
