#! /usr/bin/env python

import csv

f = open('data.csv')
data = csv.reader(f)

target_column = 3

labels = next(data)    # Don't sort headers

data = list(data)
for i in range(len(data)):
	data[i][target_column] = float(data[i][target_column])

data.sort(key=lambda x: x[target_column])

for label in labels: 	# print to screen
	print label, 
print "\n"

for row in data:
	for value in row:
		print value,
	print '\n'

