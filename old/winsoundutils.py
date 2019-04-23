import winsound, threading

def loadClips(dummy):
    pass

def playClip(clipName):
    s = threading.Timer(0, doPlayClip, [clipName])
    s.start()
    
def doPlayClip(clipName):
    winsound.PlaySound("W:\\" + clipName, winsound.SND_NOSTOP)
    
    
