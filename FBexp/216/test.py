class Solution(object):
	def combinationSum3(self, k, n):
		res = []
		self.combinationSum3Helper(k, 1, [], n, res)
		return res
	
	def combinationSum3Helper(self, k, start, sub, target, res):
		if len(sub) == k and target == 0:
			sub_res = [elem for elem in sub]
			res.append(sub_res)
		for i in range(start, 10):
			sub.append(i)
			self.combinationSum3Helper(k, i+1, sub, target - i, res)
			sub.pop()

sol = Solution()
print sol.combinationSum3(3, 7)
print sol.combinationSum3(3, 9)
