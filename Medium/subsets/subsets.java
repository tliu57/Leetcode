import java.util.*;

public class Solution {
	public List<List<Integer>> subsets(int[] nums) {

		Arrays.sort(nums);
		ArrayList<List<Integer>> solution = new ArrayList<List<Integer>>();
		subsetsHelper(nums, 0, new ArrayList<Integer>(), solution);
		return solution;
	}

	public void subsetsHelper(int[] nums, int start, ArrayList<Integer> subsol, ArrayList<List<Integer>> sol) {
		sol.add(new ArrayList<Integer>(subsol));
		for(int i = start; i < nums.length; i++) {
			subsol.add(nums[i]);
			subsetsHelper(nums, i+1, subsol, sol);
			subsol.remove(subsol.size()-1);
		}

	}
}
