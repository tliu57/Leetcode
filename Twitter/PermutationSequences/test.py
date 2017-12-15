class Solution(object):
    def getPermutation(self, n, k):
	sums = 1
	factorials = [0 for i in range(n+1)]
	factorials[0] = 1
	for i in range(1, n+1):
	    sums *= i
	    factorials[i] = sums
	nums = []
	for i in range(1, n+1):
	    nums.append(i)
	res = ""
	k -= 1
	for i in range(1, n+1):
	    index = k / factorials[n-i]
    	    res += str(nums[index])
	    del nums[index] 
	    k -= index * factorials[n-i]
	return res

sol = Solution()
print sol.getPermutation(4, 14)
