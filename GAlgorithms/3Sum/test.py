class Solution():
	def threeSum(self, nums, target):
		res = []
		for i in range(len(nums)):
			sum = target -  nums[i]
			low = i+1
			high = len(nums) - 1
			while low <= high:
				if nums[low] + nums[high] == sum:
					sub_res = []
					sub_res.append(nums[i])
					sub_res.append(nums[low])
					sub_res.append(nums[high])
					if sub_res not in res:
						res.append(sub_res)
				if nums[low] + nums[high] < sum:
					low += 1
				else:
					high -= 1
		return res


sol = Solution()
nums = [1,1,1,2,3,4]
print sol.threeSum(nums, 6)

