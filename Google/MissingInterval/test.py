class Solution(object):
	def missingInterval(self, nums, lower, upper):
		ans = []
		if not nums:
			return addRange(ans, lower, upper)
		for i in range(len(nums)-1):
			if i == 0:
				self.addRange(ans, lower+1, nums[i])
			else:
				self.addRange(ans, nums[i]+1, nums[i+1] - 1)
		self.addRange(ans, nums[i+1]+1, upper)		
		return ans

	def addRange(self, ans, lower, upper):
		if lower > upper:
			return
		if lower == upper:
			ans.append(str(lower))
		else:
			ans.append(str(lower) + "->" + str(upper))

sol = Solution()
nums = [0, 1, 3, 50, 75]
print sol.missingInterval(nums, 0, 99)
