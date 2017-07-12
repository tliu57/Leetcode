
def hilbert_curve(x, y, iter):
	if iter == 0:
		return 1
	halfLen = (1 << (iter - 1))
	halfNum = (1 << (2*iter - 2))
	if x >= halfLen and y >= halfLen:
		return 2*halfNum + hilbert_curve(x-halfLen, y-halfLen, iter-1)
	elif x < halfLen and y >= halfLen:
		return halfNum + hilbert_curve(x, y-halfLen, iter-1)
	elif x < halfLen and y < halfLen:
		return hilbert_curve(y, x, iter-1)
	else:
		return 3*halfNum + hilbert_curve(halfLen-1-y, 2*halfLen-1-x, iter-1)

print hilbert_curve(0, 1, 1)
print hilbert_curve(1, 1, 2)
print hilbert_curve(2, 2, 2)	
