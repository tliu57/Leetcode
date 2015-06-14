class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer[]}
	def twoSum(self, nums, target):
		dict = {};
		for i in nums:
			temp = nums[i]
			if dict.has_key(target - temp):
				return integer[]{dict.get(target - temp) + 1, i+1}
			dict.setdefault(key, i)
		return null
