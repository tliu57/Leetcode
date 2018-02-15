class Solution(object):
    def reverseWords(self, string):
	length = len(string)
	arr = list(string)
	self.reverse(arr, 0, length)
	starting = 0
	for i in range(length):
	    if arr[i] == " ":
	    	self.reverse(arr, starting, i)
	    	starting = i+1
	self.reverse(arr, starting, length)
	string = "".join(arr)
	return string

    def reverse(self, array, starting, ending):
	ending -= 1
	while starting < ending:
		tmp = array[starting]
		array[starting] = array[ending]
		array[ending] = tmp
		starting += 1
		ending -= 1

sol = Solution()
print sol.reverseWords("the sky is blue")

