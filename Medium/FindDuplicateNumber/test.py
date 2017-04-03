class Solution(object):
	def findDuplicate(self, nums):
		slow = 0
		fast = 0
		while True:
			slow = nums[slow]
			fast = nums[nums[fast]]
			if slow == fast:
				break
		slow = 0
		while slow != fast:
			slow = nums[slow]
			fast = nums[fast]
		return slow

sol = Solution()
print sol.findDuplicate([1, 2, 3, 2])
print sol.findDuplicate([1, 2, 2, 3])
