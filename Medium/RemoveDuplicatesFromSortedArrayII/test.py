class Solution(object):
	def removeDuplicates(self, nums):
		i = 0
		for num in nums:
			if i < 2 or num != nums[i-2]:
				print "...writing num %d to array" % num
				nums[i] = num
				print "...adding 1 to i, i is:", i
				i += 1
		print nums
		return i

sol = Solution()
print sol.removeDuplicates([1, 1, 1, 2, 2, 3]) 
