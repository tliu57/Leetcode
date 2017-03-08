from sets import Set
class Solution(object):
	def intersection(self, nums1, nums2):
		set1 = Set()
		intersection = []
		for num in nums1:
			set1.add(num)
		for num in nums2:
			if num in set1 and num not in intersection:
				intersection.append(num)
		return intersection

sol = Solution()
nums1 = [1, 2, 2, 1]
num2 = [2, 2]
print sol.intersection(nums1, num2)
