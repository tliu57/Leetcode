class Solution(object):
    def backpackV(self, nums, target):
	n = len(nums)
	dp = [0 for _ in range(target+1)]
	dp[0] = 1
	for i in range(n):
	    for j in range(target, nums[i]-1, -1):
		dp[j] += dp[j-nums[i]]
	return dp[target]

sol = Solution()
target = 9
nums = [2, 3, 5, 7]
print sol.backpackV(nums, target)


class Solution2(object):
    def backpackV(self, nums, target):
	n = len(nums)
	dp = [[0 for _ in range(target+2)]for _ in range(n+2)]
	dp[0][0] = 1
	for i in range(1, n+1):
	    for j in range(target+1):
		dp[i][j] = dp[i-1][j]
		if j >= nums[i-1]:
			dp[i][j] += dp[i-1][j-nums[i-1]]
	return dp[n][target]


sol = Solution2()
print sol.backpackV(nums, target)
