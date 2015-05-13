#! /usr/local/bin/python
from test import Timer

# Test case 1: when breakpoints are set in relatively large period
def testCase1():
	mytimer = Timer()
	mytimer.EnvironmentStart()

	for i in range(1, 120000000):
		j = i

	mytimer.SetBreakPoint()

	for i in range(300, 50000000):
		j = i

	mytimer.SetBreakPoint()

	for i in range(400, 90000000):
		j = i + i

	mytimer.EnvironmentEnd()
	return



# Test case 2: when breakpoints are set in relatively small period
def testCase2():
	mytimer = Timer()
	mytimer.EnvironmentStart()

	for i in range(1, 120):
		j = i

	mytimer.SetBreakPoint()

	for i in range(300, 500):
		j = i

	mytimer.SetBreakPoint()

	for i in range(400, 900):
		j = i + i
	mytimer.EnvironmentEnd()

# Test case 3: when two periods are almost equal
def testCase3():
	mytimer = Timer()
	mytimer.EnvironmentStart()

	for i in range(1, 120000000):
		j = i

	mytimer.SetBreakPoint()


	for i in range(1, 120000000):
		j = i + i

	mytimer.EnvironmentEnd()

# Test case 4: when one period is relatively small compared to the other
def testCase4():
	mytimer = Timer()
	mytimer.EnvironmentStart()

	for i in range(1, 120):
		j = i

	mytimer.SetBreakPoint()


	for i in range(400, 9000000):
		j = i + i

	mytimer.EnvironmentEnd()

# Test case 5: when one period is extremely small compared to the other
def testCase5():
	mytimer = Timer()
	mytimer.EnvironmentStart()

	for i in range(1, 120):
		j = i
	mytimer.SetBreakPoint()

	for i in range(400, 9000000000):
		j = i + 1
	mytimer.EnvironmentEnd()

# Test case 6: when there is no breakpoint 
def testCase6():
	mytimer = Timer()
	mytimer.EnvironmentStart()

	for i in range(100, 90000000):
		j = i
	mytimer.EnvironmentEnd()




# To run test cases, simply put the corresponding function of the test case down here
testCase1()
testCase3()
