def stripDoubleQuotes(testStr):
	if '\"\"' in testStr:
		currStr = ""
		i = 0
		while i + 2 <= len(testStr):
			if testStr[i:i+2] != '\"\"':
				currStr += testStr[i]
			else:
				currStr += '\"'
				i += 1
			i += 1
		return currStr
	else:
		return testStr			

def parseString(s):
	NumOfQuotes = 0
	result = []
	start = 0
	end = 0
	while end < len(s):
		if s[end] == "\"":
			NumOfQuotes += 1
		elif s[end] == ",":
			if NumOfQuotes%2 == 0:
				currStr = s[start:end]
				stripDoubleQuotes(currStr)
				result.append(currStr)
				start = end+1
			else:
				end += 1
		end += 1
	currStr = s[start:end]
	currStr = stripDoubleQuotes(currStr)
	result.append(currStr)
	return result

exmString = "Ford, 2016, \"super, luxurious\""
print parseString(exmString)

string2 = "This, is, example, of, \"\"multiple\"\" quotes"
print parseString(string2)


testStr = "Double \"\"quotes\"\""
print stripDoubleQuotes(testStr)
