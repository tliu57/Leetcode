class Solution(object):
    def reverseVowels(self, s):
	vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
	start = 0
	end = len(s) - 1
	strs = list(s)
	while start <= end:
		while start <= end and strs[start] not in vowels:
			start += 1
		while start <= end and strs[end] not in vowels:
			end -= 1
		if start <= end:
			strs[start], strs[end] = strs[end], strs[start]
		start += 1
		end -= 1
	return "".join(strs)

sol = Solution()
# print sol.reverseVowels("hello")
print sol.reverseVowels(" ")
print sol.reverseVowels("aA")
