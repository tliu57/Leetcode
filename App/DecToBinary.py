def DecimalToBinary(num):
	# input: integer
	# output: string
	binaryVal = ""
	while num != 0:
		digit = num % 2
		binaryVal = binaryVal + str(digit)
		num /= 2
	return binaryVal

num = 5
print DecimalToBinary(num)
