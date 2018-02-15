class Solution():
	def getTimeWithCooldown(self, nums, cooldown):
		time = 0
		if not nums or len(nums) == 0:
			return time
		map = {}
		for i in range(len(nums)):
			if nums[i] not in map:
				map[nums[i]] = time
			elif time - map[nums[i]] >= cooldown + 1:
				map[nums[i]] = time
			else:
				time += cooldown + 1 - (time - map[nums[i]])
				map[nums[i]] = time
			time += 1
		print map
		return time

sol = Solution()
print sol.getTimeWithCooldown([1, 2, 3, 2, 3], 3)
print sol.getTimeWithCooldown([1, 2, 4, 2, 3, 5, 3], 4)	
