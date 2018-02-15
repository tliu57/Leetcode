words = ["This", "is", "an", "example", "of", "text", "justification."]
L = 16

expected = [
		"This    is    an",
   		"example of  text",
   		"justification.  "
	]

def rightAlign(words, maxWidth):
	curr = []
	res = []
	curr_len = 0
	for w in words:
		if len(curr) + curr_len + len(w) > maxWidth:
			for i in range(maxWidth - curr_len):
				curr[(len(curr) - 2) - i%(len(curr) - 1 or 1)] += " "
			res.append("".join(curr))
			curr = []
			curr_len = 0
		curr.append(w)
		curr_len += len(w)
	res.append(" ".join(curr).ljust(maxWidth))
	return res

words2 = ["This", "is", "an", "example", "of", "text", "a", "note"]
print rightAlign(words, L)
