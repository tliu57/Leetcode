class Solution():
	def decodeString(self, s):
		res = ""
		stringStack = []
		countStack = []
		idx = 0
		while idx < len(s):
			if s[idx].isdigit():
				count = ""
				while s[idx].isdigit():
					count += s[idx]
					idx += 1
				countStack.append(int(count))
			elif s[idx] == "[":
				stringStack.append(res)
				res = ""
				idx += 1
			elif s[idx] == "]":
				tmp = stringStack.pop()
				repeatTimes = int(countStack.pop())
				for i in range(0, repeatTimes):
					tmp += res
				res = tmp
				idx += 1
			else:
				res += s[idx]
				idx += 1

		return res


sol = Solution()
s = "100[leetcode]"
print sol.decodeString(s)
			
