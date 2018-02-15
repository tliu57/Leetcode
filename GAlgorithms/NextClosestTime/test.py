import sys

class Solution(object):
    def __init__(self):
	self.diff = sys.maxint
	self.result = ""

    def nextClosestTime(self, time):
	digits = set()
	digits.add(int(time[0]))
	digits.add(int(time[1]))
	digits.add(int(time[3]))
	digits.add(int(time[4]))

	if len(digits) == 1:
		return time
	digits = list(digits)
    	target = int(time[:2]) * 60 + int(time[3:])
    	self.dfs(digits, "", 0, target)
	return self.result

    def dfs(self, digits, curr, pos, target):
	if pos == 4:
		curr_min = int(curr[:2])*60 + int(curr[2:])
		if curr_min == target:
			return
		if curr_min > target:
			d = curr_min - target
		else:
			d = 1440 + curr_min - target
		if d < self.diff:
			print "curr", curr
			print "target", target
			print "curr_min", curr_min
			self.diff = d
			self.result = curr[:2] + ":" + curr[2:]
		return

	for i in range(len(digits)):
		if pos == 0 and digits[i] > 2:
			continue
		if pos == 1 and int(curr)*10 + digits[i] > 23:
			continue
		if pos == 2 and digits[i] > 5:
			continue
		if pos == 3 and int(curr[2])*10 + digits[i] > 59:
			continue
		new_curr = curr + str(digits[i])
		self.dfs(digits, new_curr, pos+1, target)
		

sol = Solution()
print sol.nextClosestTime("19:34")
