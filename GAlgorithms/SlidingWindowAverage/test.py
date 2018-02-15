class MovingAverage(object):
	def __init__(self, size):
		self.id = 0
		self.size = size
		self.sum = [0 for i in range(size+1)]

	def next(self, val):
		self.id += 1
		curr_idx = self.id % (self.size + 1)
		prev_idx = (self.id - 1) % (self.size + 1) 
		self.sum[curr_idx] = self.sum[prev_idx] + val
		if self.id > self.size:
			return float(self.sum[curr_idx] - self.sum[(self.id - self.size) % (self.size + 1)])/ self.size
		else:
			return float(self.sum[curr_idx]) / self.id

movAverage = MovingAverage(3)
print movAverage.next(1)
print movAverage.next(10)
print movAverage.next(3)
print movAverage.next(5)
