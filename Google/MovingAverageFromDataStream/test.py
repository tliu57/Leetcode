class MovingAverage(object):
    def __init__(self, size):
	self.sum = 0
	self.size = size
	self.window = []

    def next(self, val):
	self.sum += val
	self.window.append(val)
	if len(self.window) > self.size:
		self.sum -= self.window[0]
		self.window.pop(0)
	return self.sum/len(self.window)


mov = MovingAverage(3)
print mov.next(1)
print mov.next(10)
print mov.next(3)
print mov.next(5)
