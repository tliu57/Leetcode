class Solution(object):
    def maxCoins(self, nums):
	nNums = [elem for elem in nums]
	nNums.insert(0, 1)
	nNums.append(1)
	length = len(nNums)
	dp = [[0]*length for i in range(length)]

	for k in range(2, length):
	    for i in range(0, length-k):
		left = i
		right = i + k
		for i in range(left+1, right):
			dp[left][right] = max(dp[left][right], nNums[left]*nNums[i]*nNums[right]+dp[left][i]+dp[i][right])

	return dp[0][length-1]

sol = Solution()
print sol.maxCoins([3, 1, 5, 8])
