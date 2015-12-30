class Solution(object):
    def __init__(self):
	self.ret_arr = []

    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
	dict = {}
	odd_count = 0
	unrepeated_set = set(s)
	middle = ''
	for c in unrepeated_set:
		dict[c] = s.count(c)
		if dict[c]%2 == 1:
			odd_count += 1
			dict[c] -= 1
			middle = c
		if odd_count > 1:
			return []
	self.createPalindromes(dict, middle)
	return self.ret_arr

    def createPalindromes(self, dict, middle):
	no_more = True
	for c in dict.keys():
		if dict[c] == 0:
			continue
		dict[c] -= 2
		self.createPalindromes(dict, c+middle+c)
		dict[c] += 2
		no_more = False

	if no_more:
		self.ret_arr.append(middle)
		

sol = Solution()
print sol.generatePalindromes("abcab")
