vector = [
	  [1, 2],
	  [3],
	  [4, 5, 6]
]

class Vector2D(object):
	def __init__(self, vec2d):
		self.row = 0
		self.col = 0
		self.vector = vec2d
	
	def next(self):
		val = self.vector[self.row][self.col]
		self.col += 1
		return val
	
	def hasNext(self):
		while self.row != len(self.vector) and self.col == len(self.vector[self.row]):
			self.row += 1
			self.col = 0
		return self.row != len(self.vector)


i, v = Vector2D(vector), []
while i.hasNext():
	v.append(i.next())

print v
