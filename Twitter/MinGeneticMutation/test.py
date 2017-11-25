class Solution(object):
	def minMutation(self, start, end, bank):
		if start == end:
			return 0
		steps = 0
		queue = [start]
		visited = set()
		options = ["A", "C", "G", "T"]
		while queue:
			q_size = len(queue)
			for index in range(q_size):
				curr = queue.pop(0)
				visited.add(curr)
				if curr == end:
					return steps
				for i in range(len(curr)):
					for c in options:
						curr_arr = list(curr)
						if c != curr_arr[i]:
							curr_arr[i] = c
						else:
							continue
						new_curr = "".join(curr_arr)
						if new_curr in bank and new_curr not in visited:
							queue.append(new_curr)
			steps += 1
		return -1

sol = Solution()
print sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])
print sol.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])
print sol.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"])
