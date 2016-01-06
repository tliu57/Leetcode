class Solution(object):
	def strobogrammaticInRange(self, low, high):
		"""
		:type low: str
		:type high: str
		:rtype: int
		"""
		if len(low) == len(high):
			a = self.getStrobogrammaticNumbers(high)
			b = self.getStrobogrammaticNumbers(low-1)
			return a - b if a > b else 0
		if len(high) == len(low) + 1:
			a = self.getStrobogrammaticNumbers(high)
			b = len(self.findStrobogrammatic(len(low))) - self.getStrobogrammaticNumbers(str(int(low)-1))
			return a + b
		if len(high) > len(low) + 1:
		 	a = self.getStrobogrammaticNumbers(high)
		 	b = len(self.findStrobogrammatic(len(low))) - self.getStrobogrammaticNumbers(low - 1)
		 	total = a + b
		 	for len_candidate in xrange(len(low)+1, len(high)-1):
				total += len(self.findStrobogrammatic(len_candidate))
			return total
		else:
			return 0

	def getStrobogrammaticNumbers(self, upper_bound):
		length = len(upper_bound)
		print "-----------------"
		print "for upper_bound:", upper_bound, 
		print "length is:", length
		StroNumberList = self.findStrobogrammatic(length)
		print "for upper_bound:", upper_bound,
		print "StroNumberList is:", StroNumberList
		print "------------------"
		count = 0
		for num in StroNumberList:
			if int(num) <= int(upper_bound):
				count += 1
		print "for this upper_bound, count is:", count
		return count

	def findStrobogrammatic(self, n):
		odd_insertion = ["0", "1", "8"]
		even_insertion = ["00", "11", "69", "96", "88"]
		if n == 1:
			return odd_insertion
		if n == 2:
			return even_insertion[1:]
		if n %2 == 1:
			pre_end, mid = self.findStrobogrammatic(n-1), odd_insertion
		else:
			pre_end, mid = self.findStrobogrammatic(n-2), even_insertion
		pre_len = (n-1)/2
		return_list = []
		for elem in pre_end:
			for mid_candidate in mid:
				ans = elem[:pre_len] + mid_candidate + elem[pre_len:]
	 			return_list.append(ans)
	 	return return_list

sol = Solution()
low = "50"
high = "100"
print sol.strobogrammaticInRange(low, high)
