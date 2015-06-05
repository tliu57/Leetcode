class Solution:
	# @param {integer[]} nums
	# @param {integer} k
	# @return {boolean}
	def containsNearbyDuplicate(self, nums, k):
		dict = {}
		for i in range(len(nums)):
			if nums[i] in dict:
				currIndex = dict[nums[i]]
				if i - currIndex <= k:
					return True
			dict[nums[i]] = i
		return False
