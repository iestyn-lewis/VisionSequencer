import os
import numpy as np
from scipy.io import wavfile

wavs = {}
rates = {}

def makeWaves(clipName):
	print "processing " + clipName
	fps, sound = wavfile.read('samples/' + clipName + ".wav")
	# transpose 1 octave down and 1 octave up
	tones = range(-12,24)
	# create all pitch-shifted tones 
	transposed= []
	for n in tones:
		pitch_shifted= []
		# cycle through channels
		for ch in range(sound.shape[1]):
			sound_channel = sound[:, ch]
			origMax = np.amax(sound_channel)
			shift = pitchshift(sound_channel, n)
			newMax = np.amax(shift)
			multiplier = origMax / newMax - 1
			#print multiplier
			pitch_shifted.append( multiplier * np.array(shift) )
		# now that all channels are collected in a list
		# combine into a single numpy array
		transposed.append(np.transpose(np.array(pitch_shifted)).copy(order='C'))
	wavs[clipName] = transposed
	rates[clipName] = fps
	
def createTposedClips(clipNames):
	for clipName in clipNames:
		makeWaves(clipName)
		w = wavs[clipName]
		r = rates[clipName]
		directory = 'samples/' + clipName
		if not os.path.exists(directory):
			os.makedirs(directory)
		for i in range(len(w)):
			wavfile.write(directory + '/' + clipName + '_' + str(i) + '.wav', rates[clipName], w[i])
			
def pitchshift(snd_array, n, window_size=2**13, h=2**11):
    """ Changes the pitch of a sound by ``n`` semitones. """
    factor = 2**(1.0 * n / 12.0)
    stretched = stretch(snd_array, 1.0/factor, window_size, h)
    return speedx(stretched[window_size:], factor)

def stretch(sound_array, f, window_size, h):
    """ Stretches the sound by a factor `f` """

    phase  = np.zeros(window_size)
    hanning_window = np.hanning(window_size)
    result = np.zeros( len(sound_array) /f + window_size)

    for i in np.arange(0, len(sound_array)-(window_size+h), h*f):

        # two potentially overlapping subarrays
        a1 = sound_array[i: i + window_size]
        a2 = sound_array[i + h: i + window_size + h]

        # resynchronize the second array on the first
        s1 =  np.fft.fft(hanning_window * a1)
        s2 =  np.fft.fft(hanning_window * a2)
        phase = (phase + np.angle(s2/s1)) % 2*np.pi
        a2_rephased = np.fft.ifft(np.abs(s2)*np.exp(1j*phase))

        # add to result
        i2 = int(i/f)
        result[i2 : i2 + window_size] += hanning_window*a2_rephased

    result = ((2**(16-4)) * result/result.max()) # normalize (16bit)

    return result.astype('int16')
    
def speedx(sound_array, factor):
    """ Multiplies the sound's speed by some `factor` """
    indices = np.round( np.arange(0, len(sound_array), factor) )
    indices = indices[indices < len(sound_array)].astype(int)
    return sound_array[ indices.astype(int) ]