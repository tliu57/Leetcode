class ValidWordAbbr(object):
	def __init__(self, dictionary):
		"""
		initialize your data structure here.
		:type dictionary: List[str]
		"""
		self.dict = {}
		for elem in dictionary:
			abbr = elem[0] + str(len(elem)-2) + elem[len(elem)-1] if len(elem) > 2 else elem
			if abbr not in self.dict:
				self.dict[abbr] = elem 
			else:
				if self.dict[abbr] != elem:
					self.dict[abbr] = ''

		print self.dict

	def isUnique(self, word):
		"""
		check if a word is unique.
		:type word: str
		:rtype: bool
		"""
		abbr = word[0] + str(len(word)-2) + word[len(word)-1] if len(word) > 2 else word
		return abbr not in self.dict or self.dict[abbr] == word



# Your ValidWordAbbr object will be instantiated and called as such:
dictionary = ["deer", "door","cake", "card"]
vwa = ValidWordAbbr(dictionary)
print vwa.isUnique("dear")
print vwa.isUnique("door")
print vwa.isUnique("cart")
print vwa.isUnique("cake")
