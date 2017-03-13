from sets import Set
import heapq
class Solution(object):
	def getSkyline(self, buildings):
		if not buildings:
			return []
		# all possible corner positions
		positions = Set([b[0] for b in buildings] + [b[1] for b in buildings])		
		positions = sorted(positions)
		
		heap = [] # get heighest height(as heapq maintains min_heap, store -height)
		result = [[-1, 0]]
		i = 0
		building_len = len(buildings)
		for pos in positions:
			while i < building_len and buildings[i][0] <= pos:
				# add the new buildings whose left side is lefter than position
				heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))
				i += 1
			while heap and heap[0][1] <= pos:
				# remove the past buildings whose right side is lefter than position
				heapq.heappop(heap)
			
			# Pick the heighest exisiting building at this moment
			height = 0
			if heap != []:
				height = -heap[0][0]
			if height != result[-1][1]:
				result.append([pos, height])
		return result[1:]


sol = Solution()
# print sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
print sol.getSkyline([[2, 9, 10], [9, 12, 15]])

			
