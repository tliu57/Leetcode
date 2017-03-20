class Solution(object):

	def combinationSum(self, candidates, target):
		res = []
		if not candidates or len(candidates) == 0:
			return res
		candidates.sort()
		subsol = []
		self.combinationSumHelper(candidates, target, 0, subsol, res)
		return res

	def combinationSumHelper(self, candidates, target, pos, subsol, res):
		if target == 0:
			new_sub = [elem for elem in subsol]
			res.append(new_sub)
			print "res is:", res
			return
		for i in range(pos, len(candidates)):
			new_target = target - candidates[i]
			if new_target >= 0:
				subsol.append(candidates[i])
				self.combinationSumHelper(candidates, new_target, i, subsol, res)
				subsol.pop()

sol = Solution()
print sol.combinationSum([2, 3, 6, 7], 7)

