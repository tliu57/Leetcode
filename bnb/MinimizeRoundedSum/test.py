from math import floor

def roundNumbers(input):
	output = map(lambda x: int(floor(x)), input)
	remain = int(round(sum(input) - sum(output)))
	print "xxx", output
	print "xxx", remain
	it = sorted(enumerate(input), key=lambda i: i[1] - floor(i[1]))
	for _ in range(int(remain)):
		output[it.pop()[0]] += 1
	return output

input = [30.3, 2.4, 3.5]
print roundNumbers(input)
input2 = [30.9, 2.4, 3.9]
print roundNumbers(input2)
