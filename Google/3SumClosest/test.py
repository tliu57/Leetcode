import sys

class Solution():
	def __init__(self):
		self.res = []
		self.dictionary = {}
		self.gap = sys.maxint

	def threeSumClosest(self, nums, target):
		for i in range(len(nums)):
			target_sum = target - nums[i]
			low = i + 1
			high = len(nums) - 1
			while low <= high:
				current_sum = nums[low] + nums[high]
				if current_sum <= target_sum:
					if abs(current_sum - target_sum) < self.gap:
						self.gap = abs(current_sum - target_sum)
						self.update_dict(i, low, high, target)
					low += 1
				elif current_sum > target_sum:
					if abs(current_sum - target_sum) < self.gap:
						self.gap = abs(current_sum - target_sum)
						self.update_dict(i, low, high, target)	
					high -= 1
		return self.dictionary[self.dictionary.keys()[0]]

	def update_dict(self, i, low, high, target):
		sub = []
		sub.append(nums[i])
		sub.append(nums[low])
		sub.append(nums[high])
		if len(self.dictionary) == 0:
			self.dictionary[self.gap] = sub
		else:
			if self.gap < self.dictionary.keys()[0]:
				self.dictionary.clear()
				self.dictionary[self.gap] = sub
			elif self.dictionary.keys()[0] == gap:
				self.dictionary[self.gap].append(sub)
		
sol = Solution()
nums = [-4, -1, 1, 2]
print sol.threeSumClosest(nums, 1)



