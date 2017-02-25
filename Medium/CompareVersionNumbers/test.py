class Solution(object):
	def compareVersion(self, version1, version2):
		arr1 = version1.split(".")
		arr2 = version2.split(".")
		length = max(len(arr1), len(arr2))
		i = 0
		while i < length:
			num1 = int(arr1[i]) if i < len(arr1) else 0
			num2 = int(arr2[i]) if i < len(arr2) else 0
			if num1 < num2:
				return -1
			if num1 > num2:
				return 1
			i += 1
		return 0

sol = Solution()
print sol.compareVersion("0.1", "1.1")
print sol.compareVersion("1.1", "1.2")
print sol.compareVersion("1.2", "13.37")
print sol.compareVersion("01", "1")
