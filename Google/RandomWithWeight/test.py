import random

class Solution():
    def __init__(self):
	self.choice_weight = [1, 2, 3, 4]

    def getRandom(self):
	self.sum_weight = 0
	for i in range(len(self.choice_weight)):
	    self.sum_weight += self.choice_weight[i]

	rnd = random.randrange(self.sum_weight)
    	for i in range(len(self.choice_weight)):
	    if (rnd) < i:
	    	return i
	    rnd -= self.choice_weight[i]
	return -1

sol = Solution()
print sol.getRandom()
