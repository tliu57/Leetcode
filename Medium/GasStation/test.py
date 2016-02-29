class Solution(object):
	def findMinimumGas(self, gas, cost):
		if not gas or not cost or len(gas) == 0 or len(cost)==0:
			return -1
		gas_sum = 0
		gas_total = 0
		index = -1
		for i in range(len(gas)):
			gas_sum += gas[i] - cost[i]
			gas_total += gas[i] - cost[i]
			if gas_sum < 0:
			 	index = i
				gas_sum = 0
		print "gas_total is:", gas_total
		print "index is:", index
		return -1 if gas_total < 0 else index + 1

gas = [5]
cost = [4]
sol = Solution()
print sol.findMinimumGas(gas, cost)
