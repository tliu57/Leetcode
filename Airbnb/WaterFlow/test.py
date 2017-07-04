class Solution(object):
	def pour_water(self, bumps, waterVolume):
		waters = [0] * len(bumps)
		water_to_pour = waterVolume
		while water_to_pour:
			for i in range(len(waters)-1):
				if bumps[i] + waters[i] + 1 <= bumps[i+1] + waters[i+1]:
					waters[i] += 1
					water_to_pour -= 1
					break
		return waters

sol = Solution()
bumps = [5, 4, 2, 1, 2, 3, 2, 1, 0, 1, 2, 4]
waterVolume = 8
print sol.pour_water(bumps, waterVolume)
			
			
		
