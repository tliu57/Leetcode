class Solution(object):
	def alienOrder(self, words):
		map = {}
		degree = {}
		result = ""
		if not words:
			return result
		for word in words:
			for c in word:
				degree[c] = 0
		print degree
		
		for i in range(0, len(words)-1):
			curr = words[i]
			next = words[i+1]
			length = min(len(curr), len(next))
			for j in range(0, length):
				c1 = curr[j]
				c2 = next[j]
				if c1 != c2:
					post_elem_set = set()
					if c1 in map:
						post_elem_set = map[c1]
					if c2 not in post_elem_set:
						post_elem_set.add(c2)
						map[c1] = post_elem_set
						degree[c2] += 1
					break
		print "degree", degree
		print "map", map
		result = ""
		q = []
		for c in degree:
			if degree[c] == 0:
				q.append(c)
		
		while q:
			char = q.pop(0)
			result += char
			if char in map:
				for c in map[char]:
					degree[c] -= 1
					if degree[c] == 0:
						q.append(c)
		if len(result) != len(degree):
			return ""
		return result			

sol = Solution()
words = ["wrt", "wrf", "er", "ett", "rftt"]
print sol.alienOrder(words)
