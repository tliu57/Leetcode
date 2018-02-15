class Solution(object):
    def maxProfit(self, prices):
	n = len(prices)
	if n < 2:
		return 0
	sell = 0
	buy = -prices[0]
	prev_sell = 0 
	prev_buy = 0
	for i in range(n):
	    prev_buy = buy
	    buy = max(prev_sell - prices[i], prev_buy)
	    prev_sell = sell
	    sell = max(prev_buy + prices[i], prev_sell)
	return sell

sol = Solution()
prices = [1, 2, 3, 0, 2]
print sol.maxProfit(prices)
