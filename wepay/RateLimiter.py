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

    def parse(self, string):
	for line in string.split("\n"):
		parsed_out = line.split("\ ")
		timestamp = parsed_out[0]
		url = parsed_out[1]
		self.hit(url, timestamp)
	return
		

rl = RateLimiter(10)
test_str = """
2016.01.01-12:01:01 graybox.apple.com:4567
2016.01.01-12:01:13 whitebox.apple.com:4567
2016.01.01-12:01:45 graybox.apple.com:4567
2016.01.01-12:01:46 graybox.apple.com:4567
"""
rl.parse(test_str)
