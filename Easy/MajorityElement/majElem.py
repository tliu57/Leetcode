class Solution:
	# @param {integer[]} nums
	# @return {integer}
	def majorityElement(self, nums):
		candidate = None
		count = 0
		for item in nums:
			if candidate == None:
				candidate = item
				count +=1
			elif candidate == item:
				count += 1
			elif candidate != item and count == 1:
				candidate = None
				count -= 1
			elif candidate != item:
				count -= 1
		return candidate
