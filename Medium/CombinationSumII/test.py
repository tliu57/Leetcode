class Solution(object):
	def combinationSum2(self, candidates, target):
		res = []
		if not candidates or len(candidates)==0:
			return res
		candidates.sort()
		self.combinationSumHelper(candidates, target, 0, [], res)
		return res

	def combinationSumHelper(self, candidates, target, pos, subsol, res):
		if target == 0:
			subsol_cp = [elem for elem in subsol]
			res.append(subsol_cp)
			return
		i = pos
		while i < len(candidates):
			new_target = target - candidates[i]
			if new_target >= 0:
				subsol.append(candidates[i])
				self.combinationSumHelper(candidates, new_target, i+1, subsol, res)
				subsol.pop()
			else:
				break
			while i < len(candidates) - 1 and candidates[i+1] == candidates[i]:
				i += 1
			i += 1

sol = Solution()
print sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
			
