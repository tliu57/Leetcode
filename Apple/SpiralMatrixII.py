n = 3
imin = 0
imax = n-1
jmin = 0
jmax = n-1
val = 1

matrix = [ [0 for i in range(n)] for x in range(n)]
while val <= n*n:
	for j in range(jmin, jmax+1):
		matrix[imin][j] = val
		val += 1
	imin += 1
	for i in range(imin, imax+1):
		matrix[i][jmax] = val
		val += 1
	jmax -= 1
	for j in range(jmax, jmin-1, -1):
		matrix[imax][j] = val
		val += 1
	jmin += 1
	for i in range(imax, imin-1, -1):
		matrix[i][jmin] = val
		val += 1
	imax -= 1
print matrix
