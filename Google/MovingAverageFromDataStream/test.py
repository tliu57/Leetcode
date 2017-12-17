class MovingAverage(object):
    def __init__(self, size):
	self.sum = [0 for i in range(size + 1)]
	self.index = 0
	self.size = size

    def mod(self, val):
	return val % (self.size + 1)

    def next(self, val):
	self.index += 1
	self.sum[self.mod(self.index)] = self.sum[self.mod(self.index - 1)] + val
	if self.index > self.size:
		return float(self.sum[self.mod(self.index)] - self.sum[self.mod(self.index - self.size)]) / float(self.size)
	return float(self.sum[self.mod(self.index)])/float(self.index)


mov = MovingAverage(3)
print mov.next(1)
print mov.next(10)
print mov.next(3)
print mov.next(5)
