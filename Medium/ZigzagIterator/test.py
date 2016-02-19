v1 = []
v2 = []

class ZigzagIterator(object):
	def __init__(self, v1, v2):
		self.queue = [_ for _ in (v1, v2) if _]
	
	def next(self):
		curr_list = self.queue.pop(0)
		ret = curr_list.pop(0)
		if curr_list:
			self.queue.append(curr_list)
		return ret

	def hasNext(self):
		if self.queue:
			return True
		return False

i = ZigzagIterator(v1, v2)
v = []
while i.hasNext():
	v.append(i.next())
print v
