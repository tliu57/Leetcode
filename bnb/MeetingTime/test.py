def cmp_moment(m1, m2):
	if m1[0] != m2[0]:
		return m1[0] - m2[0]
	return int(m1[1]) - int(m2[1])

def find_free_time(schedules):
	from collections import OrderedDict
	status = OrderedDict()
	res = []
	for person_schedule in schedules:
		for interval in person_schedule:
			if interval[0] not in status:
				status[interval[0]] = True
			else:
				status[interval[0]] = True
			if interval[1] not in status:
				status[interval[1]] = False
			else:
				status[interval[1]] |= False
	status = sorted(status.items())
	for i in range(1, len(status)):
		if status[i][1] and not status[i-1][1]:
			res.append([status[i-1][0], status[i][0]])
	return res
		
			
schedules = [
		[[1, 3], [6, 7]],
		[[2, 4]],
		[[2, 3], [9, 12]]
]

print find_free_time(schedules)

