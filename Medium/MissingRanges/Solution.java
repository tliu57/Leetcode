/**
  * Given a sorted integer array where the ranges of elements are [start, end]
  * inclusive, return its missing ranges.
  * For example, given [0, 1, 3, 50, 75], and range is [0, 99]
  * return ["2", "4->49", "51->74", "76->99"]
  */
import java.util.*;

public class Solution{
	public List<String> findMissingRanges(int[] vals, int start, int end) {
		List<String> Ranges = new ArrayList<String>();
		int prev = start - 1;
		int i = 0;
		while(i <= vals.length) {
			int curr = (i!=vals.length)? vals[i]: end + 1;
			if(curr - prev >= 2) {
				Ranges.add(getRanges(prev+1, curr-1));
			}
			prev = curr;
			i++;
		}	
		return Ranges;
	}

	public String getRanges(int prev, int curr) {
		return (prev == curr)? String.valueOf(prev): prev + "->" + curr; 
	}
}
