class Solution(object):
	def intersect(self, nums1, nums2):
		nums1.sort()
		nums2.sort()
		map = {}
		for num in nums1:
			if num not in map:
				map[num] = 1
			else:
				map[num] += 1
		out = []
		for num in nums2:
			if num in map and map[num] > 0:
				out.append(num)
				map[num] -= 1
		return out

sol = Solution()
print sol.intersect([1, 2, 2, 1], [2, 2])
