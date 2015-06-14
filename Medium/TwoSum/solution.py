class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer[]}
	def twoSum(self, nums, target):
		dict = {};
		for j, item in enumerate(nums, 1):
			i = dict.get(target - item, -1) # returns value or default if key not in dictionary, returns -1 if key not found
			if i > 0:
				return [i, j]
			dict[item] = j
