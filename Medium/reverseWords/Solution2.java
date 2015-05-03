public class Solution2 {
	public String reverseWords(String s) {
		StringBuilder str = new StringBuilder();
		int j = s.length();
		for(int i = s.length()-1; i >= 0 ; i--) {
			if(s.charAt(i)==' ') j=i;
			else if(i==0 || s.charAt(i-1) == ' ') {
				str.append(s.substring(i, j));
				if(str.length() != 0) {
					str.append(' ');
				}
			}
		}
		return str.toString();
	}
}
