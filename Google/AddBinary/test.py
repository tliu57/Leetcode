short_str = "10"
long_str = "11011"
res_list = []


for i in range(len(short_str)-1, -1, -1):
	res_list.insert(0, int(short_str[i]) + int(long_str[i]))


for i in range(len(long_str) - len(short_str)-1, -1, -1):
	res_list.insert(0, int(long_str[i]))

for i in range(len(res_list)-1, 0, -1):
	if res_list[i] >= 2:
		res_list[i] -= 2
		res_list[i-1] += 1
if res_list[0] >= 2:
	res_list[0] -= 2
	res_list = [1] + res_list

string = ""
for i in range(len(res_list)):
	string += str(res_list[i])

print string
