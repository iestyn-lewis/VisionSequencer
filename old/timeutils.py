import threading, time

tuTimers = {}
	
def createTimer(name, rate, swing=0.0):
	tuTimers[name] = {}
	timer = tuTimers[name]
	timer['rate'] = rate
	
def timerExpired(name):
	ret = False
	timer = tuTimers[name]
	if 'lastTime' not in timer:
		timer['lastTime'] = time.clock()
		ret = True
	else:
		rate = timer['rate']
		now = time.clock()
		elapsed = now - timer['lastTime']
		if elapsed > rate:
			timer['lastTime'] = now
			ret = True
	return ret
	