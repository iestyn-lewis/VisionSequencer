import threading, time

class Timer:
	def __init__(self, name, rate, swing=0.0):
		self.name = name
		self.rate = rate
		self.swing = swing
		self.lastTime = None
		
	def expired(self):
		ret = False
		if self.lastTime is None:
			self.lastTime = time.clock()
			ret = True
		else:
			now = time.clock()
			elapsed = now - self.lastTime
			if elapsed > self.rate:
				self.lastTime = now
				ret = True
		return ret
	