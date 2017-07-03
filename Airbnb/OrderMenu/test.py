class Solution(object):
	def combinationSum(self, candidates, target):
		candidates = sorted(candidates.items(), key = lambda x: x[1])
		print "xxx, candidates:", candidates
		res = []
		sub = []
		self.combinationSumHelper(candidates, target, 0, sub, res)
		return res
	
	def combinationSumHelper(self, candidates, target, pos, sub, res):
		if target >= 0 and target < epsilon:
			res.append([elem for elem in sub])
			return
		for i in range(pos, len(candidates)):
			newTarget = target - candidates[i][1]
			if newTarget >= 0:
				sub.append((candidates[i].key, candidates[i].value))
				self.combinationSumHelper(candidates, newTarget, i, sub, res)
				sub.pop()

