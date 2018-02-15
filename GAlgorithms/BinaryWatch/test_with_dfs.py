class Solution(object):
    def readBinaryWatch(self, num):
	res = []
	nums1 = [8, 4, 2, 1]
	nums2 = [32, 16, 8, 4, 2, 1]
	for i in range(num+1):
		list1 = self.generateDigit(nums1, i)
		list2 = self.generateDigit(nums2, num-i)
		for num1 in list1:
		    if num1 >= 12:
		    	continue
		    for num2 in list2:
		    	if num2 >= 60:
		    		continue
		    	if num2 < 10:
                            num2 = "0" + str(num2)
                        res.append(str(num1)+":"+str(num2))
	return res

    def generateDigit(self, nums, count):
	res = []
	self.dfs(res, nums, count, 0, 0)
	return res

    def dfs(self, res, nums, count, pos, currSum):
	if count == 0:
		res.append(currSum)
		return
	for i in range(pos, len(nums)):
	    self.dfs(res, nums, count-1, i+1, currSum+nums[i])

sol = Solution()
print sol.readBinaryWatch(1)
