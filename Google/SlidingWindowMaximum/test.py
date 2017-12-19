class Solution():
    def maxSlidingWindow(self, nums, k):
	d = []
	out = []
	for i, n in enumerate(nums):
	    while d and nums[d[-1]] < n:
	    	d.pop()
	    d.append(i)
	    if d[0] == i - k:
	    	d.popleft()
	    if i >= k-1:
	    	out += nums[d[0]],
	return out

sol = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
print sol.maxSlidingWindow(nums, 3)
