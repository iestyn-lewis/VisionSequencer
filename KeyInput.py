import cv2

class KeyInput:
	def __init__(self):
		pass
		
	def processKeys(self, sq):
		# get key input
		ret = False
		key = cv2.waitKey(1) & 0xFF
		if key == ord('1'):
			sq.setCurrInst(0)
		elif key == ord('2'):
			sq.setCurrInst(1)
		elif key == ord('3'):
			sq.setCurrInst(2)
		elif key == ord('4'):
			sq.setCurrInst(3)
		elif key == ord('5'):
			sq.setCurrInst(4)
		elif key == ord('6'):
			sq.setCurrInst(5)
		elif key == ord('7'):
			sq.setCurrInst(6)
		elif key == ord('8'):
			sq.setCurrInst(7)
		elif key == ord('9'):
			sq.setCurrInst(8)
		elif key == ord('0'):
			sq.setCurrInst(9)
		if key == ord('!'):
			sq.toggleMute(0)
		elif key == ord('@'):
			sq.toggleMute(1)
		elif key == ord('#'):
			sq.toggleMute(2)
		elif key == ord('$'):
			sq.toggleMute(3)
		elif key == ord('%'):
			sq.toggleMute(4)
		elif key == ord('^'):
			sq.toggleMute(5)
		elif key == ord('&'):
			sq.toggleMute(6)
		elif key == ord('*'):
			sq.toggleMute(7)
		elif key == ord('('):
			sq.toggleMute(8)
		elif key == ord(')'):
			sq.toggleMute(9)
		elif key == ord('s'):
			sq.saveCurrInst()
		elif key == ord('q'):
			ret = True
		return ret