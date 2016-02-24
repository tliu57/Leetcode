class Solution(object):
	def isValidSerialization(self, preorder):
		preorder = preorder.split(",")
		slot = 1
		for node in preorder:
			if slot == 0:
				return False
			if node == "#":
				slot -= 1
			else:
				slot += 1
		return slot == 0

sol = Solution()
str1 = "9,3,4,#,#,1,#,#,2,#,6,#,#"
str2 = "1,#"
str3 = "9,#,#,1"
str4 = "#,#,3,5,#"
print sol.isValidSerialization(str1)
print sol.isValidSerialization(str2)
print sol.isValidSerialization(str3)
print sol.isValidSerialization(str4)
