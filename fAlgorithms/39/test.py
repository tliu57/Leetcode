class Solution(object):
	def combinationSum(self, candidates, target):
		res = []
		if not candidates or len(candidates) == 0:
			return res
		candidates.sort()
		self.combinationSumHelper(candidates, target, 0, [], res)
		return res

	def combinationSumHelper(self, candidates, target, pos, subsol, res):
		if target == 0:
			sub_res = [elem for elem in subsol]
			res.append(sub_res)
			return

		for i in range(pos, len(candidates)):
			newTarget = target - candidates[i]
			if newTarget >= 0:
				subsol.append(candidates[i])
				self.combinationSumHelper(candidates, newTarget, i, subsol, res)
				subsol.pop()

sol = Solution()
candidates = [2, 3, 6, 7]
print sol.combinationSum(candidates, 7)

