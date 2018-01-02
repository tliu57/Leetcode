class Solution(object):
    def findLengthOfLCIS(self, nums):
	if not nums:
		return 0
	n = len(nums)
	dp = [1] * n
	maxLen = 1
	for i in range(1, n):
	    if nums[i] > nums[i-1]:
	    	dp[i] = dp[i-1] + 1
	    if dp[i] > maxLen:
	    	maxLen = dp[i]
	return maxLen

sol = Solution()
print sol.findLengthOfLCIS([1, 3, 5, 4, 7])
print sol.findLengthOfLCIS([2, 2, 2, 2, 2])
