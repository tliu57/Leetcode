class Solution(object):
	def find_intersect_num(self, rectangles):
		roots = {i: i for i in xrange(len(rectangles))}
		print roots
		num_intersections = 0
		for i in xrange(len(rectangles)):
			for j in xrange(i):
				if self.is_intersect(rectangles[i], rectangles[j]):
					i_root = self.find(i, roots)
					j_root = self.find(j, roots)
					if i_root != j_root:
						roots[j_root] = i_root
						num_intersections += 1

		return num_intersections

	def find(self, i, root):
		while i != root[i]:
			root[i] = root[root[i]]
			i = root[i]
		return i
	
	def is_intersect(self, r1, r2):
		left_x = max(r1[0][0], r2[0][0])
		right_x = min(r1[1][0], r2[1][0])
		lower_y = max(r1[0][1], r2[0][1])
		upper_y = min(r1[1][1], r2[1][1])
		return (left_x < right_x) and (lower_y < upper_y)


rectangles = [
		[[0, 0], [4, 2]],
		[[3, 0], [7, 3]],
		[[2, 1], [6, 4]]
	     ]

sol = Solution()
print sol.find_intersect_num(rectangles)


