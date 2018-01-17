class Solution(object):
    def minSubArrayLen(self, s, nums):
	if not nums:
		return 0
	i = 0
	j = 0
	currSum = 0
	import sys
	minLen = sys.maxint
	while j < len(nums):
	    while currSum < s and j < len(nums):	
	    	currSum += nums[j]
		j += 1
	    while currSum >= s and i <= j:
	    	minLen = min(minLen, j-i)
	     	currSum -= nums[i]
	    	i += 1
        return minLen


sol = Solution()
print sol.minSubArrayLen(7, [2,3,1,2,4,3])
		
