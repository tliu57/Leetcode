ans = 0
nums = sorted(nums)
for i in xrange(len(nums)-2):
	prev_ans = ans
	j, k = i+1, len(nums)-1
	while j<k:
		if nums[i] + nums[j] + nums[k] < target:
			ans += (k-j)
			j += 1
		else:
			k -= 1
	if prev_ans == ans:
		break
return ans
