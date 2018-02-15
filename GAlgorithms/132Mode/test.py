class Solution(object):
    def find132Pattern(self, nums):
	if len(nums) <= 2:
		return False
    	minList = self.getMinList(nums)
	maxList = self.getMaxList(nums)
	for i in range(1, len(nums)-1):
	    if nums[i] > minList[i-1] and nums[i] > maxList[i+1]:
	    	return True
	return False

    def getMinList(self, nums):
	minList = [0 for i in range(len(nums))]
	minList[0] = nums[0]
	for i in range(1, len(nums)):
	    if nums[i] < minList[i-1]:
	    	minList[i] = nums[i]
	    else:
	    	minList[i] = minList[i-1]
	print minList
	return minList

    def getMaxList(self, nums):
	maxList = [0 for i in range(len(nums))]
	maxList[-1] = nums[-1]
	for i in range(len(nums)-2, -1, -1):
	    if nums[i] > maxList[i+1]:
	    	maxList[i] = nums[i]
	    else:
	    	maxList[i] = maxList[i+1]
	print maxList
	return maxList

nums = [3, 1, 4, 2]
sol = Solution()
print sol.find132Pattern(nums)
nums2 = [-1, 3, 2, 0]
print sol.find132Pattern(nums2)
nums3 = [1, 2, 3, 4]
print sol.find132Pattern(nums3)
