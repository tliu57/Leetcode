class RateLimiter(object):
	def __init__(self):
		self.mp = {}

	def isRateLimited(self, timestamp, event, rate, increment):
		index = rate.find("/")
		times = int(rate[:index])
		unit = rate[index:]
		
		time_diff = 1
		if unit == "m":
			time_diff *= 60
		elif unit == "h":
			time_diff *= 60 * 60
		elif unit == "d":
			time_diff *= 60 * 60 * 24

		last_time = timestamp - time_diff

		if event not in self.mp:
			self.mp[event] = []

		return_value = False
		counts = self.find_event(self.mp[event], last_time)
		if counts <= times:
			return_value = True

		if increment and not return_value:
			self.insert_event(self.mp[event], timestamp)
		return return_value
	
	def insert_event(eventlist, timestamp):
		eventlist.append(timestamp)

	def find_event(self, eventlist, last_time):
		l = 0
		r = len(eventlist)-1
		if r < 0 or eventlist[r] < last_time:
			return 0
		ans = 0
		while l <= r:
			mid = (l + r) >> 1
			if eventlist[mid] >= last_time:
				ans = mid
				r = mid - 1
			else:
				l = mid + 1
		return len(eventlist) - 1 - ans + 1


rt = RateLimiter()
print rt.isRateLimited(1, "login", "3/m", True)
