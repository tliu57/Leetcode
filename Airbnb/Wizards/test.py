import sys

class Wizard(object):
	def __init__(self, idx, dis):
		self.idx = idx
		self.dis = dis

class Solution(object):
	def findMinDistance(self, costs):
		n = len(costs)
		wizards = []
		for i in range(n):
			wizards.append(Wizard(i, 0 if i == 0 else sys.maxsize))

		queue = []
		queue.append(wizards[0])
		while queue:
			curr = queue.pop()
			for i in costs[curr.idx]:
				newDis = curr.dis + (curr.idx - i)^2
				if newDis < wizards[i].dis:
					wizards[i].dis = newDis
					queue.append(wizards[i])
		return wizards[n-1].dis

sol = Solution()
costs= [
	[1, 4, 5],
	[],
	[],
	[],
	[9],
	[],
	[],
	[],
	[],
	[]
]
print sol.findMinDistance(costs)
