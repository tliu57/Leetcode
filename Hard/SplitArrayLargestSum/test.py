class Solution(object):
	def splitArray(self, nums, m):
		max_value = 0
		sum_value = 0
		for num in nums:
			max_value = max(max_value, num)
			sum_value += num
		if m == 1:
			return sum_value
		l = max_value
		r = sum_value
		while l <= r:
			mid = (l + r) / 2
			if self.canDivide(mid, nums, m):
				r = mid - 1
			else:
				l = mid + 1
		return l

	def canDivide(self, limit, nums, m):
		total = 0
		count = 1
		for num in nums:
			total += num
			if total > limit:
				count += 1
				total = num
			if count > m:
				return False
		return True

sol = Solution()
nums = [7, 2, 5, 10, 8]
print sol.splitArray(nums, 2)
#print sol.canDivide(15, nums, 2)
