from collections import OrderedDict
class LRUCache(object):

	def __init__(self, capacity):
		self.dict = OrderedDict()
		self.cap = capacity

	def get(self, key):
	        if key not in self.dict:
			return -1
		value = self.dict.pop(key)
		self.dict[key] = value
		return value
	
	def set(self, key, value):
		if key in self.dict:
			self.dict.pop(key)
		else:
			if self.cap > 0:
				self.cap -= 1
			else:
				self.dict.popitem(last=False)
		self.dict[key] = value

cache = LRUCache(2)
cache.set(1, 16)
cache.set(2, 32)
cache.set(3, 48)
print LRUCache

print cache.get(1)
print cache.get(2)
print cache.get(9)

