class Solution(object):
    def findDisappearedNumbers(self, nums):
	missing = []
	for i in range(len(nums)):
	    value = abs(nums[i])
	    if nums[value-1] > 0:
	    	nums[value-1] = -nums[value-1]

	for i in range(len(nums)):
	    if nums[i] > 0:
		missing.append(i+1)
	return missing


sol = Solution()
print sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
