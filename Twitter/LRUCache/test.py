from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
	self.dic = OrderedDict()
	self.remain = capacity

    def get(self, key):
	if key not in self.dic:
		return -1
	print "xxx, before dic is: {}".format(self.dic)
	v = self.dic.pop(key)
    	self.dic[key] = v
	print "xxx, after write dic is: {}".format(self.dic)
	return v

    def put(self, key, value):
	if key in self.dic:
	    self.dic.pop(key)
	else:
	    if self.remain > 0:
	    	self.remain -= 1
	    else:
	    	self.dic.popitem(last=False)
	self.dic[key] = value

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)

