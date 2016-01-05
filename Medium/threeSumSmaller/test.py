nums = [-2, 0, 1, 3]
target = 2
ans = 0
nums = sorted(nums)
for i in xrange(len(nums)-2):
	j, k = i+1, len(nums)-1
	while j<k:
		if nums[i] + nums[j] + nums[k] < target:
			ans += (k - j)
			j += 1
		else:
			k -= 1
print ans
