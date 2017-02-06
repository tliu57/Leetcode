class Solution(object):
	def maxSubArrayLen(self, nums, k):
		sum_dic = {0: -1}
		i = 0
		sum = 0
		maxLength = 0
		while i < len(nums):
			sum += nums[i]
			if sum not in sum_dic:
				sum_dic[sum] = i
			if (sum - k) in sum_dic:
				maxLength = max(maxLength, i- sum_dic[sum-k])			
			i += 1
		return maxLength

sol = Solution()
nums = [1, -1, 5, -2, 3]
k = 3
print sol.maxSubArrayLen(nums, k)

print "================="
nums2 = [-2, -1, 2, 1]
k2 = 1
print sol.maxSubArrayLen(nums2, k2)

nums3 = [-1]
k3 = -1
print sol.maxSubArrayLen(nums3, k3)		 	
