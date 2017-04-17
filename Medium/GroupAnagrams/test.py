class Solution(object):
	def groupAnagrams(self, strs):
		ret = []
		map = {}
		for str in strs:
			key = tuple(sorted(str))
			if key in map:
				map[key].append(str)
			else:
				map[key] = [str]
		for k, v in map.items():
			ret.append(v)
		return ret

sol = Solution()
print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
