class MovingAverage(object):
	def __init__(self, size):
		self.id = 0
		self.size = size
		self.sum = []
		self.sum.append(0)

	def next(self, val):
		self.sum.append(self.sum[-1] + val)
		self.id += 1
		if self.id > self.size:
			return float(self.sum[self.id] - self.sum[self.id - self.size])/ self.size
		else:
			return float(self.sum[self.id]) / self.id

movAverage = MovingAverage(3)
print movAverage.next(1)
print movAverage.next(10)
print movAverage.next(3)
print movAverage.next(5)
