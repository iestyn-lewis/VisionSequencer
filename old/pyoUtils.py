from pyo import *
import wave, threading

pyoTabs = {}
pyos = Server(sr=44100, nchnls=2, buffersize=256, duplex=0).boot()
pyos.start()

def loadClips(clipNames):
	for clipName in clipNames:
		pyoTabs[clipName] = SndTable('W:/' + clipName)
	
def doPlayClip2(clipName):
	snd = pyoTabs[clipName]
	freq = snd.getRate()
	a = TableRead(table=snd, freq=freq).out()
	print snd

def doPlayClip(clipName):
	sf = SfPlayer('W:/' + clipName)
 	sf2 = sf.mix(2).out()
	print clipName
	time.sleep(1)

def playClip(clipName):
    s = threading.Timer(0, doPlayClip2, [clipName])
    s.start()

met = Metro(.125, 12).play()
sounds = ["Open-Hi-Hat-1.wav", "Closed-Hi-Hat-1.wav", "Hip-Hop-Snare-2.wav", "Dry-Kick.wav"]
loadClips(sounds)
out = TrigFunc(met, playClip, ['Closed-Hi-Hat-1.wav'])
time.sleep(30)
#pyos.gui(locals())

	


def playClip3(clipName):
	s = Server().boot()
	a = Sine(440, 0, 0.1).out()
	s.start()
	time.sleep(1)
	
def doPlayClip2(clipName):
	snd = pyoTabs[clipName]
	freq = snd.getRate()
	a = TableRead(table=snd, freq=freq).out()
	time.sleep(1)