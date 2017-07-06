class Solution(object):
	def preferenceList(self, preferences):
		map = {}
		degree = {}
		result = []
		if not preferences:
			return result
		for pref in preferences:
			for elem in pref:
				degree[elem] = 0
		for pref in preferences:
			for i in range(1, len(pref)):
				for j in range(i):
					if pref[j] not in map:
						post_elem_set = set()
						post_elem_set.add(pref[i])
						map[pref[j]] = post_elem_set
					else:
						map[pref[j]].add(pref[i])
		for key in map:
			for elem in map[key]:
				degree[elem] += 1
		q = []
		for c in degree:
			if degree[c] == 0:
				q.append(c)

		while q:
			char = q.pop(0)
			result.append(char)
			if char in map:
				for c in map[char]:
					degree[c] -= 1
					if degree[c] == 0:
						q.append(c)
		return result
sol = Solution()
preferences = [
		[3, 5, 7, 9],
		[2, 3, 8],
		[5, 8]
	      ]
print sol.preferenceList(preferences)
		
