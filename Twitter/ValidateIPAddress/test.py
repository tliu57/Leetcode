class Solution(object):
	def validIPAddress(self, IP):
		if "." in IP:
			if self.validateIPV4Address(IP):
				return "IPv4"
		elif ":" in IP:
			if self.validateIPV6Address(IP):
				return "IPv6"
		return "Neither"

	def validateIPV4Address(self, IP):
		components = IP.split(".")
		if len(components) != 4:
			return False
		for comp in components:
			print comp
			if len(comp) == 0:
				return False
			if len(comp) != 1 and comp.startswith("0"):
				return False
			try:
				comp_num = int(comp)
				if comp_num > 255 or comp_num < 0:
					return False
				if comp_num == 0 and comp != '0':
					return False
			except:
				return False	
		return True

	def validateIPV6Address(self, IP):
		components = IP.split(":")
		if len(components) != 8:
			return False
		for comp in components:
			if not self.isValidIPV6Token(comp):
				return False
		return True

	def isValidIPV6Token(self, token):
		if len(token) > 4 or len(token) == 0:
			return False
		for c in token:
			ascii_c = ord(c)
			isDigit = ascii_c >=48 and ascii_c <= 57
			isUppercase = ascii_c >= 56 and ascii_c <= 70
			isLowercase = ascii_c >= 97 and ascii_c <= 102
			if not (isDigit or isUppercase or isLowercase):
				return False
		return True 
		

sol = Solution()
# print sol.validIPAddress("256.256.256.256")
# print sol.validIPAddress("172.16.254.1")
# print sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")	
# print sol.validIPAddress("1.0.1.")		
# print sol.validIPAddress("15.16.-0.1")
print sol.validIPAddress("192.0.0.1")
