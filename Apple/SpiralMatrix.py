matrix = [
	  [ 1, 2, 3],
	  [ 4, 5, 6],
	  [ 7, 8, 9]
	 ]

spiral_matrix = []

imin = 0
jmin = 0
imax = len(matrix)-1
jmax = len(matrix[0])-1

while imin <= imax and jmin <= jmax:
	for j in range(jmin, jmax+1):
		spiral_matrix.append(matrix[imin][j])
	imin += 1
	if imin > imax:
	 	break
	for i in range(imin, imax+1):
		spiral_matrix.append(matrix[i][jmax])
	jmax -= 1
	if jmax < jmin:
	 	break
	for j in range(jmax, jmin-1, -1):
		spiral_matrix.append(matrix[imax][j])
	imax -= 1
	if imax < imin:
	 	break
	for i in range(imax, imin-1, -1):
		spiral_matrix.append(matrix[i][jmin])
	jmin +=1

print spiral_matrix

test_order = []
for i in range(8, 2, -1):
	test_order.append(i)
print test_order
