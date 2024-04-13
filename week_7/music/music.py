import pygame
import os
import sys
pygame.init()

W, H = 850, 850

display = pygame.display.set_mode([W, H])
path = os.getcwd()
list = os.listdir(os.path.join(path, "week_7/music")) 

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

# instasamka_zadengida = pygame.mixer.music.load(os.path.join(path, "week_7/music/INSTASAMKA – ЗА ДЕНЬГИ ДА.mp3"))
# instasamka_otkltel = pygame.mixer.music.load(os.path.join(path, "week_7/music/INSTASAMKA – Отключаю телефон.mp3"))
# doiacat_paintthetownred = pygame.mixer.music.load(os.path.join(path, "week_7/music/Doja Cat – Paint The Town Red.mp3"))
    
def play_next_song():
    global songs
    songs = songs[1:] + [songs[0]] # move current song to the back of the list

    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

def play_prev_song():
    global songs, songs_len
    songs = [songs[-1]] + songs[:songs_len] # get prev song from the end of the list

    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

# Just get the current song name
def get_song_name():
    global songs
    return songs[0]



running = True
while running:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()
            sys.exit()
    pygame.display.update()
            
            
    buttons = pygame.key.get_pressed()
    if buttons[pygame.K_UP]:
        pygame.mixer.music.play()
    
    if buttons[pygame.K_DOWN]:
        pygame.mixer.music.pause()
        
    if buttons[pygame.K_LEFT]:
        pygame.mixer.music.play()
                
    
    
pygame.exit()