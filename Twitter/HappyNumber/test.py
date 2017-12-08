class Solution(object):
    def isHappy(self, n):
	total = n
	visited = set()
	while total != 1:
		num_list = self.rip_num_to_list(total)
		print num_list
		total = self.get_square_sum(num_list)
		print total
		if total == 1:
			return True
		elif total in visited:
			return False
		else:
			visited.add(total)

    def rip_num_to_list(self, n):
	num_list = []
	while n >= 10:
		num_list.insert(0, n%10)
		n /= 10
	num_list.insert(0, n%10)
	return num_list

    def get_square_sum(self, num_list):
	num_total = 0
	for num in num_list:
		num_total += num*num
	return num_total

sol = Solution()
print sol.isHappy(7)

