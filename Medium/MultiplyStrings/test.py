num1 = "456"
num2 = "123"

res = [0] * (len(num1) + len(num2))
for i, ei in enumerate(reversed(num1)):
	for j, ej in enumerate(reversed(num2)):
		res[i+j] += int(ei) * int(ej)
		print "i+j is",(i+j),
		print "value is:",res[i+j]
		res[i+j+1] += res[i+j]/10
		print "i+j+1 is",(i+j+1),
		print "value is:",res[i+j+1]
		res[i+j] %= 10
		print "i+j value is:", res[i+j]

ret_res = ''.join(str(i) for i in reversed(res))
print ret_res.lstrip('0')

