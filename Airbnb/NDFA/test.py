class NDFA(object):
	def accept(self, input, target, transitions):
		if len(input) == 1:
			return input in target
		prcs_str = input[:2]
		new_states = transitions[int(prcs_str[0])][int(prcs_str[1])]
		for st in new_states:
			new_input = str(st) + input[2:]
			if self.accept(new_input, target, transitions):
				return True
		return False



transitions = [ [[1], [0, 2], [0]],
		[[2], [0], [2]],
		[[1], [2], [0]]
		]

input = "0122"
target = "0"
print NDFA().accept(input, target, transitions)

input2 = "02"
target2 = "1"
print NDFA().accept(input2, target2, transitions)
