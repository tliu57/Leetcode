from fractions import Fraction
import itertools
class Solution(object):
	def judgePoint24(self, nums):
		if len(nums) == 1:
			return abs(nums[0] - 24) < 1e-10
		for a, b, *rest in itertools.permutations(nums):
			next = [a+b, a-b, b-a, a*b]
			next.append(Fraction(b, a) if a != 0 else 0)
			next.append(Fraction(a, b) if b != 0 else 0)
			for x in next:
				if self.judgePoint24([x]+rest):
					return True
		return False

sol = Solution()
print (sol.judgePoint24([4, 1, 8, 7]))
print (sol.judgePoint24([1, 2, 1, 2]))
print (sol.judgePoint24([1, 5, 9, 1]))
print (sol.judgePoint24([3, 9, 7, 7]))
