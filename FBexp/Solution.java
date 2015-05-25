import java.util.*;

public class Solution {
	public String sortString(String order, String input) {
		Map<Character, Integer> map = new HashMap<Character, Integer>();
		for(int i = 0 ; i < order.length() ; i++) {
			map.put(order.charAt(i), i);
		}
		int[] arr = new int[input.length()];
		for(int i = 0 ; i < input.length(); i++) {
			arr[i] = map.get(input.charAt(i));

		}
		Arrays.sort(arr);
		StringBuffer out = new StringBuffer();
		for(int i = 0 ; i < arr.length ; i++) {
			out.append(order.charAt(arr[i]));
		}
		return out.toString();
	}
}
