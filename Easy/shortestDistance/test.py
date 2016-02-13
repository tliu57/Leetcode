word_list = ["practice", "makes", "perfect", "coding", "makes"]

class Solution():
	def shortestDistance(self, words, word1, word2):
		list1= []
		list2= []
		for i in range(len(words)):
			if words[i] == word1:
				list1.append(i)
			if words[i] == word2:
				list2.append(i)
		print list1
		print list2
		dis = len(words)
		for i in list1:
			for j in list2:
				if abs(i-j) < dis:
					dis = abs(i-j)
		return dis

sol = Solution()
print sol.shortestDistance(word_list, "makes", "coding")
