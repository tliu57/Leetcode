from sets import Set

class Solution(object):
	def concatenation(self, dictionary, key):
		table = [False for i in range(len(key)+1)]
		for i in range(len(key)):
			for j in range(i, -1, -1):
				if table[j] and dictionary.contains(key[j:i+1]):
					table[i+1] = True
					break
		return table[len(key)]

sol = Solution()
dictionary = Set()
dictionary.add("world")
dictionary.add("hello")
dictionary.add("super")
dictionary.add("hell")
key = "helloworld"
print key[0:5]
print sol.concatenation(dictionary, key)
			
