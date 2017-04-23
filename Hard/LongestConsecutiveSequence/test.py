class Solution(object):
	def longestConsecutive(self, nums):
		res = 0
		map = {}
		for num in nums:
			if not num in map:
				left = map[num-1] if num-1 in map else 0
				right = map[num+1] if num+1 in map else 0
				sum = left + right + 1
				map[num] = sum
				res = max(res, sum)
				map[num - left] = sum
				map[num + right] = sum
			else:
				continue
		return res

sol = Solution()
print sol.longestConsecutive([100, 4, 200, 1, 3, 2])
