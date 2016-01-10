# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
	def read(self, buf, n):
		"""
		:type buf: Destination buffer (List[str])
		:type n: Maximum number of characters to read (int)
	 	:rtype: The number of characters read (int)
	  	"""
	  	actual_read = 0
	  	while n > 0:
			buf4 = [''] * 4
	  		l = read4(buf4)

	  		if not l:
	  			return actual_read

	  		for i in range(min(n, l)):
		  		buf[actual_read] = buf4[i]
		  		actual_read += 1
		  		n -= 1

		 return actual_read
