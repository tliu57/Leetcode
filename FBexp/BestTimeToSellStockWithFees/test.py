class Solution(object):
	def maxProfit(self, prices, fee):
		if not prices or len(prices) == 0:
			return 0
		maxProfit = 0
		minPrice = prices[0]
		maxPrice = prices[0]
		for i in range(1, len(prices)):
			if prices[i] >= maxPrice:
				maxPrice = prices[i]
			elif prices[i] < maxPrice:
				if prices[i] < minPrice:
					maxPrice = prices[i]
					minPrice = prices[i]
				elif maxPrice - prices[i] > fee:
					if maxPrice - minPrice > fee:
						# We can sell the stock
						maxProfit += maxPrice - minPrice - fee
						maxPrice = prices[i]
						minPirce = prices[i]
		if maxPrice - minPrice > fee:
			maxProfit += maxPrice - minPrice - fee
		return maxProfit

prices1 = [1, 3, 4, 5]
prices2 = [1, 5, 4, 8]
prices3 = [1, 5, 1, 8]
prices4 = [7, 6, 1, 8]
prices5 = [1, 5, 4, 3, 2]
prices6 = [1, 5, 2, 8]
sol = Solution()
assert sol.maxProfit(prices1, 3) == 1
assert sol.maxProfit(prices2, 3) == 4
assert sol.maxProfit(prices3, 3) == 5
assert sol.maxProfit(prices4, 3) == 4
assert sol.maxProfit(prices5, 3) == 1
assert sol.maxProfit(prices6, 3) == 4

# print sol.maxProfit(prices4, 3)
