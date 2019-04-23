import pyaudio
import wave, threading

streams = {}
files = {}
p = pyaudio.PyAudio()  

def loadClips(clipNames):
    for clipName in clipNames:    
        #open a wav format music
        files[clipName] = wave.open("W:/" + clipName, "rb")
        f = files[clipName]
        streams[clipName] = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                            channels = f.getnchannels(),  
                            rate = f.getframerate(),  
                            frames_per_buffer = 256,
                            output = True)

def playClip(clipName):
    s = threading.Timer(0, doPlayClip, [clipName])
    s.start()

def doPlayClip(clipName):
    #f = clips[clipName
    f = wave.open("W:/" + clipName, "rb")
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                            channels = f.getnchannels(),  
                            rate = f.getframerate(),  
                            frames_per_buffer = 256,
                            output = True)
    chunk = 1024  
    data = f.readframes(chunk)  
    
    #paly stream  
    while data != '':  
        stream.write(data)  
        data = f.readframes(chunk)  
    
    stream.stop_stream()  
    stream.close()  


