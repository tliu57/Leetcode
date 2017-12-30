class Solution(object):
    def reconstructQueue(self, people):
	height = []
	dic = {}
	for person in people:
		if person[0] in dic:
			dic[person[0]].append(person)
    		else:
			height.append(person[0])
    			dic[person[0]] = [person]

	height.sort(reverse=True)
	resultQ = []
	for h in height:
		h_persons = dic[h]
		h_persons.sort()
    		for p in h_persons:
			resultQ.insert(p[1], p)
    	return resultQ
    
people = [[7,0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
sol = Solution()
print sol.reconstructQueue(people)
