class Solution(object):
	def rob(self, nums):
		last = 0
		now = 0
		for i in nums:
			last, now = now, max(i+last, now)
		return now		

sol = Solution()
print sol.rob([2, 1, 3])
