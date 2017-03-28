class Solution(object):
	def checkSubarraySum(self, nums, k):
		sums = [0 for i in range(len(nums))]
		sum = 0
		for i in range(len(nums)):
			sum += nums[i]
			sums[i] = sum
			if i >= 1:
				if k != 0 and sums[i] % k == 0:
					return True
				if k == 0 and sums[i] == 0:
					return True
				for j in range(i-1):
					if k!= 0 and (sums[i] - sums[j]) % k == 0:
						return True
					elif k == 0 and (sums[i] - sums[j]) == 0:
						return True
		return False

sol = Solution()
print sol.checkSubarraySum([23, 2, 6, 4, 7], 6)
print sol.checkSubarraySum([0, 1, 0], 0)
print sol.checkSubarraySum([0, 0], 0)
