class Solution():
    def merge(self, list1, list2):
	m = len(list1)
	n = len(list2)
	for index2 in range(n-1, -1, -1):
		last = list1[m-1]
		index1 = m - 2
		while index1 > 0 and list1[index1] > list2[index2]:
			list1[index1+1] = list1[index1]
			index1 -= 1
		if last > list2[index2]:
			list1[index1+1] = list2[index2]
			list2[index2] = last

	return list1, list2

sol = Solution()
print sol.merge([10], [2, 3])
print sol.merge([1, 5, 9, 10, 15, 20], [2, 3, 8, 13])

