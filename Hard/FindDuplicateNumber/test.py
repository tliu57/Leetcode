from itertools import compress
nums = [3, 2, 5, 14, 5, 5, 19, 18, 11, 10, 1, 4, 5, 5, 5, 5, 12, 5, 17, 5]

class Solution(object):
	def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		low = 1
		high = len(nums) - 1
		n = high
		while low < high:
		 	 mid = low + (high - low )* 0.5
		 	 print "mid is,", mid
			 counter_low = 0
			 new_len = 0
			 for i in nums:
				 if low <= i <= high:
					new_len += 1
				 if low <= i <= mid:
			 		counter_low += 1
			 print "counter low is:", counter_low
			 if counter_low >= new_len * 0.5:
				high = low + (high - low)/2 
			 else:
			 	low = low + (high - low)/2 + 1
		return low

sol = Solution()
print sol.findDuplicate(nums)
