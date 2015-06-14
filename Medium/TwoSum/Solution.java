import java.util.*;
public class Solution {
	public int[] twoSum(int[] numbers, int target) {
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		for(int i = 0 ; i < numbers.length ; i++) {
			int temp = numbers[i];
			if(map.containsKey(target - temp))
				return int[] {map.get(target - temp) + 1, i+1};
			map.put(temp, i);
		}
		throw new IllegalArgumentException("No two sum solution");
	}
}
