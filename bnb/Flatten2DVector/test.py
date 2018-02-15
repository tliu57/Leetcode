vector = [
	  [1, 2],
	  [3],
	  [4, 5, 6]
]

class Vector2D(object):
	def __init__(self, vec2d):
		self.prevRow = None
		self.prevCol = None
		self.row = 0
		self.col = 0
		self.vector = vec2d
		self._moveToNext()
	
	def _moveToNext(self):
		while self.row < len(self.vector):
			if self.col < len(self.vector[self.row]):
				break
			self.row += 1
			self.col = 0

	def next(self):
		if self.hasNext():
			self.prevRow = self.row
			self.prevCol = self.col
			self.col += 1
			self._moveToNext()
			return self.vector[self.prevRow][self.prevCol]
		else:
			return None
	
	def hasNext(self):
		return self.row < len(self.vector)

	def remove(self):
		if self.prevRow and self.prevCol:
			ls = self.vector[self.prevRow]
			self.vector[self.prevRow] = ls[:self.prevCol] + ls[self.prevCol+1:]
			self.row = self.prevRow
			self.col = self.prevCol
			self._moveToNext()
			self.prevRow = None
			self.prevCol = None
		else:
			raise Exception("called remove before next!")

i, v = Vector2D(vector), []
while i.hasNext():
	v.append(i.next())

print v
