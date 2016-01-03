nums = [0,1,3, 50, 75]
lower = 0
upper = 99
dummy_head = lower - 1
dummy_end = upper + 1
nums.insert(0, dummy_head)
nums.append(dummy_end)

print nums

head = nums[0]

ret = []
for i in range(1, len(nums)):
	if nums[i] - nums[i-1] > 1:
		head = nums[i-1] + 1
		end = nums[i] - 1
		if end > head:
			ret.append(str(head) + "->" + str(end))
		else:
			ret.append(str(head))
print ret

