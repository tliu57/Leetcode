class Solution(object):
	def lengthOfLIS(self, nums):
		if not nums or len(nums) == 0:
			return 0
		sequence = []
		length = 0
		sequence.append(nums[0])
		length += 1

		for i in range(1, len(nums)):
			if nums[i] > sequence[length-1]:
				sequence.append(nums[i])
				length += 1
			else:
				pos = self.binarySearch(sequence, 0, length-1, nums[i])
				sequence[pos] = nums[i]
		return length

	def binarySearch(self, sequence, low, high, target):
		while low <= high:
			mid = low + (high - low)/2
			if target == sequence[mid]:
				return mid
			elif sequence[mid] > target:
				high = mid - 1
			else:
				low = mid + 1
		return low

sol = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print sol.lengthOfLIS(nums)
