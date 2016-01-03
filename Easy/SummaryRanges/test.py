

class Solution(object):
	def summaryRanges(self, nums):
		return_list = []
		if not nums or len(nums) == 0:
			return return_list
		nums.append(nums[-1]+2)
		head = nums[0]
		for i in range(1, len(nums)):
			if nums[i] - nums[i-1] > 1:
				if head == nums[i-1]:
					return_list.append(str(head))
				else:
					return_list.append(str(head) + "->" + str(nums[i-1]))
				head = nums[i]
		return return_list

nums = [1,2,3,4,7,8,9]
sol = Solution()
print sol.summaryRanges(nums)

			
