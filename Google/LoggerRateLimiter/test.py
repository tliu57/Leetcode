class Logger(object):
    def __init__(self):
	self.ok = {}

    def shouldPrintMessage(self, timestamp, message):
	retValue = True
	if message in self.ok:
		ok_time = self.ok[message]
		if timestamp < ok_time:
			retValue = False
	self.ok[message] = timestamp + 10
	return retValue

logger = Logger()
print logger.shouldPrintMessage(1, "foo")
print logger.shouldPrintMessage(2, "bar")
print logger.shouldPrintMessage(3, "foo")
print logger.shouldPrintMessage(8, "bar")
print logger.shouldPrintMessage(10, "foo")
print logger.shouldPrintMessage(11, "foo")
		
