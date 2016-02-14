import pdb

class Solution(object):
	def missingNumber(self, nums):
		start = 0
		end = len(nums) - 1
		return self.missingNumberHelper(start, end, nums)

	def missingNumberHelper(self, start, end, nums):
		pdb.set_trace()
		if start == end:
			pdb.set_trace()
			return nums[start-1] + 1
		else:
			mid = start + (end - start) / 2
			if nums[mid] - nums[start] != mid - start:
				pdb.set_trace()
				return self.missingNumberHelper(start, mid, nums)
			else:
				pdb.set_trace()
				return self.missingNumberHelper(mid, end, nums)

sol = Solution()
nums = [0, 1, 3]
print sol.missingNumber(nums)
