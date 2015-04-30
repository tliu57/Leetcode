public class TestCase {
	public static void main(String[] args) {
		Solution answer = new Solution();
		int[] nums = {1, 2, 3, 4, 5, 6, 7};
		answer.rotate(nums, 3);
		for(int i = 0 ; i < nums.length ; i++) {
			System.out.println(nums[i]);
		}
	}
}
