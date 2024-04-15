import pygame
import sys
import os


# Path to the songs + list of songs + playlist len
path_lab = os.path.join(os.getcwd(), "week_7//music//songs")
songs = [os.path.join("week_7//music//songs", i) for i in os.listdir(path_lab)]
songs_len = len(songs)

pygame.init()

my_font = pygame.font.SysFont('uuu', 30)

# Some event
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

# The display that we will see
W, H = 500, 500
display = pygame.display.set_mode([W, H])
pygame.display.set_caption("uuu")

# Check paused song or not
is_paused = False

# Simple methods to play next and prev song
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


# Main code
run = True
while run:
    for event in pygame.event.get():
        if event.type == SONG_END:
            play_next_song() 
        elif event.type == pygame.QUIT:
            run = False
        # Pressed once
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed() 

            # check for left arrow (prev_song)
            if keys[pygame.K_LEFT]:
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                play_prev_song()
            
            # check for right arrow (next_song)
            elif keys[pygame.K_RIGHT]:
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                play_next_song()
            
            # check for space (pause song or unpause)
            elif keys[pygame.K_SPACE]:
                print(is_paused)
                if is_paused == False:
                    pygame.mixer.music.pause()
                    is_paused = True
                else:
                    pygame.mixer.music.unpause()
                    is_paused = False

   
    if not run:
        break


    if not pygame.mixer.music.get_busy() and not is_paused:
        pygame.mixer.music.load(songs[0])
        pygame.mixer.music.play()
    
    # Text of current playing music
    text_surface = my_font.render(f'playing: {get_song_name()[16:]}', False, (255, 255, 255))
    display.fill((0, 0, 0))
    display.blit(text_surface, (150, 250))

    # Update the display
    pygame.display.flip()

# End of code
pygame.quit()
sys.exit()