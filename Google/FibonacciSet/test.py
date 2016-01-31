def generateFibonacci(n):
	Fib_list = []
	f0 = 0
	f1 = 1
	Fib_list.append(f0)
	Fib_list.append(f1)
	while f0 + f1 < n:
		Fib_list.append(f0 + f1)
		tmp = f0
		f0 = f1
		f1 = tmp + f1
	return Fib_list

def genFibonacciSet(n):
	fib_list = generateFibonacci(n)
	low = 0
	high = len(fib_list)-1
	while low < high:
		if fib_list[low] + fib_list[high] == n:
			return [fib_list[low], fib_list[high]]
		elif fib_list[low] + fib_list[high] < n:
			low +=1
		else:
			high -= 1
	return []

print genFibonacciSet(9)


