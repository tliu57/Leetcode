class Solution(object):
    def backpackIV(self, nums, target):
	dp = [0 for _ in range(target+2)]
	dp[0] = 1
	for i in range(len(nums)):
	    for j in range(nums[i], target+1):
		dp[j] += dp[j-nums[i]]
	return dp[target]

sol = Solution()
print sol.backpackIV([2, 3, 5, 7], 9)

