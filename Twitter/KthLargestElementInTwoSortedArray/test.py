# Input: 2, 3, 6, 7, 9
# Input: 1, 4, 8, 10
# Input: k = 5

class Solution(object):
    def kthLargestElement(self, list1, list2, k):
	ptr1 = 0
	ptr2 = 0
	arr = [0 for i in range(k)]
	i = 0
	while ptr1 < len(list1) and ptr2 < len(list2) and i < k:
		if list1[ptr1] < list2[ptr2]:
			arr[i] = list1[ptr1]
			ptr1 += 1
		else:
			arr[i] = list2[ptr2]
			ptr2 += 1
		i += 1
	while i < k:
		if ptr1 < len(list1):
		    arr[i] = list1[ptr1]
		    ptr1 += 1
		else:
		    arr[i] = list2[ptr2]
		    ptr2 += 1
		i += 1
	return arr[k-1]

sol = Solution()
print sol.kthLargestElement([2, 3, 6, 7, 9], [1, 4, 8, 10], 5)
