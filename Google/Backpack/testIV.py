class Solution(object):
    def backpackIV(self, nums, target):
	n = len(nums)
	dp = [0 for _ in range(target+1)]
	dp[0] = 1
	for i in range(n):
	    for j in range(target, nums[i]-1, -1):
		dp[j] += dp[j-nums[i]]
	return dp[target]

sol = Solution()
target = 11
nums = [2, 3, 6, 9]
print sol.backpackIV(nums, target)
