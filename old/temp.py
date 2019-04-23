WAVFILE = 'Hip-Hop-Snare-2.wav'
import pygame
from pygame import *
import sys

mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.init()
print pygame.mixer.get_init() 
screen=pygame.display.set_mode((400,400),0,32) 

while True:
    for event in pygame.event.get():
        if event.type == QUIT:                                                    
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_ESCAPE:
                 pygame.quit()
                 sys.exit()
            elif event.key==K_UP:
                s = pygame.mixer.Sound(WAVFILE)
                ch = s.play()
                while ch.get_busy():
                    pygame.time.delay(100)
    pygame.display.update()