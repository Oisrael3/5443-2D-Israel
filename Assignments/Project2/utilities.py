import pygame

def background_music():
    pygame.mixer.init()
    #load the music from my files
    pygame.mixer.music.load('battle_music/battle-metal.mp3')
    pygame.mixer.music.queue('battle_music/battle-dragons.mp3')
    pygame.mixer.music.queue('battle_music/slavic-music.mp3')
    pygame.mixer.music.queue('battle_music/forever-viking-music.mp3')
    pygame.mixer.music.queue('battle_music/prepare-to-die-music.mp3')
    pygame.mixer.music.queue('battle_music/viking-music.mp3')
    #set the volume so it doesnt blast anyones ear drums
    pygame.mixer.music.set_volume(.04)
    # tell it to play continuously
    pygame.mixer.music.play(-1)
    

    
    
