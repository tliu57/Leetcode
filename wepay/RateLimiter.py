class RateLimiter():
    def __init__(self, limit):
	self.maxRequest = limit
	self.map = {}

    def hit(self, url, timestamp):
	if url in self.map:
		oldest_timestamp = self.map[url][0]
		if timestamp - oldest_timestamp > 1:
			self.map[url].remove(0)
		self.map[url].append(timestamp)
		if len(self.map[url]) > self.maxRequest:
			print "reject url {}".format(url)
	else:
		self.map[url] = [timestamp]


rl = RateLimiter()

