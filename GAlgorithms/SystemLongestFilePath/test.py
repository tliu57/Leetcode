class Solution:
	def lengthLongestPath(self, input):
		if not input:
			return 0
		ans = 0
		lines = input.split("\n")
		levels = [0 for i in range(len(input))]
		for line in lines:
			curr_level = line.count("\t")
			curr_len = len(line.strip("\t"))
			if "." in line:
				ans = max(ans, levels[curr_level - 1] + curr_len)
			else:
				levels[curr_level] = levels[curr_level - 1] + curr_len + 1
		return ans

sol = Solution()
string1 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
string2 = ""
print sol.lengthLongestPath(string2) 
