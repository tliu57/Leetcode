import heapq

class Wizard(object):
	def __init__(self, idx, dis):
		self.idx = idx
		self.dis = dis

class Solution(object):
	def dijkstra(self, costs):
		n = len(costs)
		path = []
		heap = []
		
		while h:
			curr = heapq.heappop(h)
		
