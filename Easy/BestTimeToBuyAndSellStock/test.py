class Solution(object):
	def maxProfit(self, prices):
		if not prices or len(prices) == 1:
			return 0
		minPrice = prices[0]
		priceDiff = 0
		for i in range(1, len(prices)):
			if prices[i] < minPrice:
				minPrice = prices[i]
			elif prices[i] - minPrice > priceDiff:
				priceDiff = prices[i] - minPrice
		return priceDiff

sol = Solution()
#print sol.maxProfit([7, 1, 5, 3, 6, 4])
print sol.maxProfit([2, 4, 1])
