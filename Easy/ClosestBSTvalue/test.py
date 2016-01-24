class Solution():
	def closestValue(self, root, target):
		kid = root.right if root.val < target else root.left
		if not kid:
			return root.val
		kid_closest = self.closestValue(kid, target)
		return root.val if abs(root.val - target) < abs(kid_closest - target) else kid_closest
