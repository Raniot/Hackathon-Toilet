# from playsound import playsound
# playsound('gongs.mp3')

# from pydub import AudioSegment
# from pydub.playback import play

# sound = AudioSegment.from_mp3('gongs.mp3')
# play(sound)

# import os
# os.system("aplay sound.wav")

# import pygame
# pygame.init()
# drum = pygame.mixer.Sound("sound.wav")
# drum.play()
# while pygame.mixer.music.get_busy() == True:
#     continue
# drum = pygame.mixer.Sound("sound.wav")
# drum.play()
# drum = pygame.mixer.Sound("sound.wav")
# drum.play()
# drum = pygame.mixer.Sound("sound.wav")
# drum.play()
# while pygame.mixer.music.get_busy() == True:
#     continue

import pygame
pygame.mixer.init()
pygame.mixer.music.load("sound.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue