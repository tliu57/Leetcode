# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	    # @param {TreeNode} root
	    # @return {boolean}
	    def isSymmetric(self, root):
		    if not root:
		    	return true
		    return isSymmetric(root.left, root.right);
					           
            def isSymmetric(self, node1, node2):
	            if node1 and node2:
			 return node1.value == node2.value and self.isSymmetric(node1.left, node2.right) and self.isSymmetric(node1.right, node2,left)
		    else:
			 return node1 == ndoe2
