class Solution(object):
    def reversePairs(self, nums):
	res = 0
	copy = [num for num in nums]
	bit = [0 for i in range(len(nums)+1)]
	copy.sort()

	for elem in nums:
		res += self.search(bit, self.index(copy, 2*elem + 1))
    		self.insert(bit, self.index(copy, elem))
    	return res

    def index(self, arrs, val):
	l = 0
	r = len(arrs) - 1
	m = 0
	while l <= r:
		m = l + ((r - l) >> 1)
		if arrs[m] >= val:
			r = m - 1
		else:
			l = m + 1
	return l + 1

    def search(self, bit, i):
	sum = 0
	while i < len(bit):
	    sum += bit[i]
	    i += i & -i
	return sum

    def insert(self, bit, i):
	while i > 0:
		bit[i] += 1
		i -= i & -i

sol = Solution()
print sol.reversePairs([2, 4, 3, 5, 1])
