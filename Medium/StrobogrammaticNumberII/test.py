class Solution(object):
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
print sol.findStrobogrammatic(3)
