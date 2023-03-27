import pygame

def background_music():
    pygame.mixer.init()
    #load the music from my files
    pygame.mixer.music.queue('Griffin SpaceBattle/space_rocks/pew-pew-two-102442.mp3')
    #set the volume so it doesnt blast anyones ear drums
    pygame.mixer.music.set_volume(.04)
    # tell it to play continuously
    pygame.mixer.music.play(-1)
    