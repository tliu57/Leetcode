class Solution(object):
	def reverseString(self, s):
		if len(s) < 1:
			return s
		char_list = list(s)
		i = 0
		j = len(s) - 1
		while i < j:
			char_i = char_list[i]
			char_j = char_list[j]
			if char_i != char_j:
				char_list[i], char_list[j] = char_j, char_i
			i += 1
			j -= 1
		str = "".join(char_list)
		return str

string = "hello"
sol = Solution()
print sol.reverseString(string)
