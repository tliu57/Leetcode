class Solution(object):
	def productExceptSelf(self, nums):
		n = len(nums)
		left_products = [1, nums[0]]
		for i in range(2, n):
			left_products.append(left_products[i-1] * nums[i-1])
		right_products = [1 for i in range(n)]
		for i in range(n-2, -1 , -1):
			right_products[i] = right_products[i+1] * nums[i+1]
		res = []
		for i in range(n):
			res.append(left_products[i] * right_products[i])
		return res

nums = [1, 2, 3, 4]
sol = Solution()
print sol.productExceptSelf(nums)
