from sets import Set
grid = [['.', '#', '.', 'G'],
     	['.', '.', '#', '.'],
	['G', '.', '.', '.'],
	['.', '.', '.', '.']]

expected_output = [['2', '#', '1', 'G'],
		   ['1', '2', '#', '1'],
		   ['G', '1', '2', '2'],
		   ['1', '2', '3', '3']]


class Solution(object):
	def ShortestDist(self, grid):
		self.que = []
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 'G':
					self.bfs(grid, i, j, Set([]))
		return grid

	def bfs(self, grid, i, j, visited_set):
		self.que.append((i,j))
		visited_set.add((i,j))
		while len(self.que)!= 0:
			(ix, jx) = self.que.pop()
			if self.check(grid, ix-1, jx, visited_set):
				self.writeToGrid(grid, (ix-1, jx),(ix, jx))
				self.que.append((ix-1, jx))
				visited_set.add((ix-1, jx))
			if self.check(grid, ix+1, jx, visited_set):
				self.writeToGrid(grid, (ix+1, jx), (ix, jx))
				self.que.append((ix+1, jx))
				visited_set.add((ix+1, jx))
			if self.check(grid, ix, jx-1, visited_set):
				self.writeToGrid(grid, (ix, jx-1), (ix, jx))
				self.que.append((ix, jx-1))
				visited_set.add((ix, jx-1))
			if self.check(grid, ix, jx+1, visited_set):
				self.writeToGrid(grid, (ix, jx+1), (ix, jx))
				self.que.append((ix, jx+1))
				visited_set.add((ix, jx+1))
#			print "for ix = %d, jx = %d, visited_set is:"%(ix, jx), visited_set
#			print "queue is:", self.que
#			print "-----------"


	def check(self, grid, ix, jx, visited_set):
		if ix < 0 or jx < 0 or ix >= len(grid) or jx >= len(grid[0]) or (ix, jx) in visited_set:
			return False
		if grid[ix][jx] == '#' or grid[ix][jx] == 'G':
		 	return False
		return True

	def writeToGrid(self, grid, curr_pos, prev_pos):
		(i, j) = curr_pos
		(ix, jx) = prev_pos
		if grid[ix][jx] == 'G':
			grid[i][j]= str(1)
		else:
			tmp_dist = int(grid[ix][jx]) + 1
			if grid[i][j] == '.' or tmp_dist < int(grid[i][j]):
				grid[i][j] = str(tmp_dist)

sol = Solution()
print sol.ShortestDist(grid)
print expected_output
assert sol.ShortestDist(grid)==expected_output
