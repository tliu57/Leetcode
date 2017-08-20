import requests
def get_speed():
	response = requests.get("http://tina-server.apple.com:4567/status")	
	curr_speed = response.split(".")[1]
	return curr_speed	

def put_gas(force):
	response = requests.post("http://tina-server.apple.com:4567/Throttle {}".format(force))
	if response = 200:
		return True
	return False

def tune_speed(target_speed):
	v = get_speed()
	left = 0
	right = 100
	press = right
	while v != target_speed:
		if v < target_speed:
			put_gas(press)
			press = left + (right - left)/2
		else:
			put_gas(press)
			press = right - (right - left)/2
		time.sleep(1)
		v = get_speed()
	return True			

