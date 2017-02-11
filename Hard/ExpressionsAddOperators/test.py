class Solution():
	def addOperators(self, num, target):
		res = []
		if not num or len(num) == 0:
			return res
		self.helper(res, "", num, target, 0, 0, 0)
		return res

	def helper(self, res, path, num, target, pos, eval, multed):
		if pos == len(num) and eval == target:
			res.append(path)
		
		for i in range(pos, len(num)):
			currNum = int(num[pos: i+1])
			if i != pos and num[pos] == '0':
				break
			if len(path) == 0:
				self.helper(res, path + str(currNum), num, target, i+1, eval + currNum, currNum)
			else:
				self.helper(res, path + "+" + str(currNum), num, target, i+1, eval + currNum, currNum)
				self.helper(res, path + "-" + str(currNum), num, target, i+1, eval - currNum, -currNum)
				self.helper(res, path + "*" + str(currNum), num, target, i+1, eval - multed + multed * currNum, multed * currNum)

sol = Solution()
print sol.addOperators("123", 6)
print sol.addOperators("232", 8)
print sol.addOperators("105", 5)
print sol.addOperators("00", 0)
print sol.addOperators("3456237490", 9191)
