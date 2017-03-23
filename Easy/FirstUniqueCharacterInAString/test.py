import sys

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for c in s:
                if c not in dic:
                        dic[c] = 1
                else:
                        dic[c] += 1
        for i in range(len(s)):
                if dic[s[i]] == 1:
                        return i
        return -1


test_str = "abc"
print test_str.find("d")
