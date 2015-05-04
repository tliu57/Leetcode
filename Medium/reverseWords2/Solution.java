public class Solution {
	public String reverseWords2 (String s) {
		char[] str = s.toCharArray();
		reverse(str, 0 , str.length);
		for(int i = 0, j = 0 ; j <= str.length ; j++) {
			if( j == str.length || str[j] == ' ' ) {
				reverse(str, i, j);
				i = j+1;
			}
		}
		return String.valueOf(str);
	}

	private void reverse(char[] str, int start, int end) {
		for(int i = 0; i < (end-start)/2; i++) {
			char temp = str[start + i];
			str[start + i] = str[ end - 1 - i ];
			str[ end - i - 1 ] = temp;
		}
	}
}
