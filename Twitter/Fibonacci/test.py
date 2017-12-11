# Return the nth number of a fibonacci
# Fibonacci series: 0, 1, 1, 2, 3
class Solution():
    def fibonacci(self, n):
	a = 0
	b = 1
	for i in range(1, n):
	    c = a+b
	    a = b
	    b = c
	return a

sol = Solution()
print sol.fibonacci(3)

