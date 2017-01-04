import collections
class Solution():
	def findItinerary(self, tickets):
		tripMap = collections.defaultdict(list)
		for ticket in sorted(tickets)[::-1]:
			tripMap[ticket[0]].append(ticket[1])
		print "tripMap is:", tripMap
		itinerary = []
		self.visit('JFK', itinerary, tripMap)
		print itinerary[::-1]

	def visit(self, airport, route, map):
		while map[airport]:
			self.visit(map[airport].pop(), route, map)
		route.append(airport)
		

sol = Solution()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
sol.findItinerary(tickets)
			

