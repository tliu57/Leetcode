#! /usr/local/bin/python

from timeit import default_timer as timer
from pylab import *

class Timer:
	# constructor
	def __init__(self):							
		self.prevTime = 0.0
		self.currTime = 0.0
		self.listPeriod = []
	
	# timer starts  
	def EnvironmentStart(self):
		self.prevTime = timer()
	
	# The previous subsection ends. The next subsection begins.
	def SetBreakPoint(self):
		self.currTime = timer()
		self.listPeriod.append(self.currTime - self.prevTime)
		self.prevTime = self.currTime

	# timer ends
	def EnvironmentEnd(self):
		self.currTime = timer()
		self.listPeriod.append(self.currTime - self.prevTime)
		self.drawPieChart()

	# generate a piechart, save it to pie1.png and shows
	def drawPieChart(self):
		figure(1, figsize=(4, 4))
		axes([0.1, 0.1, 0.8, 0.8])
		fracs = self.listPeriod
		pie(fracs)

		savefig('./pie1')
		show()






