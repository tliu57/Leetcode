class Solution(object):
    def nextPermutation(self, nums):
	length = len(nums)
	if length < 2:
		return
	i = length - 1
	while i > 0:
		if nums[i-1] < nums[i]:
			break
		else:
			i -= 1
	if i == 0:
		self.reverseSort(nums, 0, length-1)
		return
	else:
	    val = nums[i-1]
	    j = length - 1
	    while j >= i:
	    	if nums[j] > val:
	    		break
	    	j -= 1
	    self.swap(nums, j, i-1)
	    self.reverseSort(nums, i, length - 1)
	    print nums
	    return

    def swap(self, nums, i, j):
	tmp = nums[i]
	nums[i] = nums[j]
	nums[j] = tmp

    def reverseSort(self, nums, start, end):
	if start > end:
		return
	for i in range(start, start + (end-start)/2 + 1):
	    self.swap(nums, i, start + end-i)

sol = Solution()
sol.nextPermutation([1, 3, 2])
