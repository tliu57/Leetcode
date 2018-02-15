class Point(object):
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b

class Solution:
	def maxPoints(self, points):
		if not points:
			return 0
		ans = 0
		for i in range(0, len(points)):
			map = {}
			maxPoints = 0
			vertical = 0
			overlap = 0
			for j in range(i+1, len(points)):
				if points[i].x == points[j].x:
					if points[i].y == points[j].y:
						overlap += 1
					else:
						vertical += 1
				else:
					slope = float((points[i].y - points[j].y)) / float((points[i].x - points[j].x))
					if slope not in map:
						map[slope] = 0
					map[slope] += 1	
					maxPoints = max(maxPoints, map.get(slope, 0))
			maxPoints = max(maxPoints, vertical)
			ans = max(maxPoints + overlap + 1, ans)
			print map
		return ans


sol = Solution()
A = Point(1, 2)
B = Point(3, 6)
C = Point(0, 0)
D = Point(1, 3)
#print sol.maxPoints([A, B, C, D])
#print sol.maxPoints([Point(0, 0)])
#print sol.maxPoints([Point(0, 0), Point(0, 1)])
print sol.maxPoints([Point(0, 9), Point(138, 429), Point(115, 359), Point(115, 359), Point(-30, -102), Point(230, 709), Point(-150, -686),
Point(-135, -613), Point(-60, -248), Point(-161, -481), Point(207, 639), Point(23, 79), Point(-230, -691), Point(-115, -341), Point(92, 289),
Point(60, 336), Point(-105, -467), Point(135, 701), Point(-90, -393), Point(-184, -551), Point(150, 774)])
