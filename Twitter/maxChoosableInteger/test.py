class Solution():
    def firstOneCanWin(self, maxChoosableInteger, desiredTotal):
	total_sum = (1+maxChoosableInteger) * maxChoosableInteger / 2
	if total_sum < desiredTotal:
		return False
	if desiredTotal <= maxChoosableInteger:
		return True
    	used = [0 for i in range(maxChoosableInteger+1)]
	dp = [-1 for i in range(1 << maxChoosableInteger)]
	return self.helper(dp, used, desiredTotal)

    def helper(self, dp, used, total):
	if total <= 0:
		return False
	key = self.to_decimal(used)
	if dp[key] == -1:
		for i in range(1, len(used)):
	    		if not used[i]:
				used[i] = 1
				if not self.helper(dp, used, total - i):
		    		    dp[key] = 1
				    used[i] = 0
				    return True
				used[i] = 0
		dp[key] = 0
	return dp[key] == 1

    def to_decimal(self, used):
	res = 0
	for i in used:
		res <<= 1
		if i:
			res |= 1
	return res

sol = Solution()
print sol.firstOneCanWin(10, 11)
print sol.firstOneCanWin(10, 40)
print sol.firstOneCanWin(4, 6)
print sol.firstOneCanWin(20, 210)
print sol.firstOneCanWin(20, 209)
