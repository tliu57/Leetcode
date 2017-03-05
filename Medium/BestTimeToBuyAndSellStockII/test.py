class Solution(object):
	def maxProfit(self, prices):
		if not prices or len(prices) == 1:
			return 0
		maxProfit = 0
		for i in range(1, len(prices)):
			if prices[i] > prices[i-1]:
				maxProfit += prices[i] - prices[i-1]
		return maxProfit

sol = Solution()
print sol.maxProfit([7, 5, 1, 4, 6])
