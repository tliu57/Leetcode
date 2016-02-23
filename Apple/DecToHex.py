def getHexChar(num):
	if 0 <= num <= 9:
		return chr(num + ord('0'))
	else:  #  10 <= num <= 15
		return chr(num - 10 + ord('A'))

def decimalToHex(decimal_input):
	ans = ""
	while decimal_input != 0:
		hexValue = decimal_input % 16
		ans = getHexChar(hexValue) + ans
		decimal_input = decimal_input / 16
	return ans

def main():
	decimal_input = 230
	print decimalToHex(decimal_input)

main()
