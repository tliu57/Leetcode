import java.util.*;

public class TestCase {
	public static void main(String[] args) {
		Solution answer = new Solution();
		int[] vals = {0, 1, 3, 50, 75};
		List<String> list = answer.findMissingRanges(vals, 0 , 99);
		for(String str : list) {
			System.out.println(str);
		}
	}
}

