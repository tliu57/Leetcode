class Solution(object):
    def findNumberOfLIS(self, nums):
	if not nums:
		return 0
	n = len(nums)
	dp = [0] * n
	ans = [0] * n
	maxlen = 1
	dp[0] = 1
	ans[0] = 1
	for i in range(1, n):
	    dp[i] = 1
	    ans[i] = 1
	    for j in range(i):
		if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
			dp[i] = dp[j] + 1
			ans[i] = ans[j] 
		elif nums[i] > nums[j] and dp[j] + 1 == dp[i]:
			ans[i] += ans[j]
	    if dp[i] > maxlen:
	 	maxlen = dp[i]
	count = 0
	for i in range(n):
	    if dp[i] == maxlen:
	        count += ans[i]
	return count

sol = Solution()
print sol.findNumberOfLIS([1,3,5,4,7])
print sol.findNumberOfLIS([2, 2, 2, 2, 2])
