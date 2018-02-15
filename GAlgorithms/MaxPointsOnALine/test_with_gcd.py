class Point(object):
    def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution(object):
    def maxPoints(self, points):
	if not points:
		return 0
	if len(points) <= 2:
		return len(points)

	slope_map = {}
	result = 0
	for i in range(len(points)):
	    slope_map.clear()
	    overlap = 0
	    max_points = 0
	    for j in range(i+1, len(points)):
		x_diff = points[i].x - points[j].x
		y_diff = points[i].y - points[j].y
		if x_diff == 0 and y_diff == 0:
			overlap += 1
			continue
		else:
			gcd = self.getGCD(x_diff, y_diff)
			if gcd != 0:
				x_diff /= gcd
				y_diff /= gcd
			if x_diff in slope_map:
			    if y_diff in slope_map[x_diff]:
				slope_map[x_diff][y_diff] += 1
			    else:
				slope_map[x_diff][y_diff] = 1
			else:
			    slope_map[x_diff] = {}
			    slope_map[x_diff][y_diff] = 1
			max_points = max(slope_map[x_diff][y_diff], max_points)
    	    result = max(result, max_points + overlap + 1)
    	return result

    def getGCD(self, a, b):
	if b == 0:
		return a
	else:
		return self.getGCD(b, a%b)

sol = Solution()
#print sol.maxPoints([Point(a=0, b=0), Point(a=94911151, b=94911150), Point(a=94911152, b=94911151)])
#print sol.maxPoints([Point(a=0, b =0), Point(a=-1, b=-1), Point(a=2, b=2)])
print sol.maxPoints([Point(a=0, b=0), Point(a=1, b=1), Point(a=0, b=0)])

