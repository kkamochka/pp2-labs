# import pygame
# import os
# import sys
# pygame.init()

# W, H = 850, 850

# display = pygame.display.set_mode([W, H])
# path = os.getcwd()
# list = os.listdir(os.path.join(path, "week_7/music")) 

# SONG_END = pygame.USEREVENT + 1
# pygame.mixer.music.set_endevent(SONG_END)

# # instasamka_zadengida = pygame.mixer.music.load(os.path.join(path, "week_7/music/INSTASAMKA – ЗА ДЕНЬГИ ДА.mp3"))
# # instasamka_otkltel = pygame.mixer.music.load(os.path.join(path, "week_7/music/INSTASAMKA – Отключаю телефон.mp3"))
# # doiacat_paintthetownred = pygame.mixer.music.load(os.path.join(path, "week_7/music/Doja Cat – Paint The Town Red.mp3"))
    
# def play_next_song():
#     global songs
#     songs = songs[1:] + [songs[0]] # move current song to the back of the list

#     pygame.mixer.music.load(songs[0])
#     pygame.mixer.music.play()

# def play_prev_song():
#     global songs, songs_len
#     songs = [songs[-1]] + songs[:songs_len] # get prev song from the end of the list

#     pygame.mixer.music.load(songs[0])
#     pygame.mixer.music.play()

# # Just get the current song name
# def get_song_name():
#     global songs
#     return songs[0]



# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == quit:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()
            
            
#     buttons = pygame.key.get_pressed()
#     if buttons[pygame.K_UP]:
#         pygame.mixer.music.play()
    
#     if buttons[pygame.K_DOWN]:
#         pygame.mixer.music.pause()
        
#     if buttons[pygame.K_LEFT]:
#         pygame.mixer.music.play()
                
    
    
# pygame.exit()

import pygame
import os
import sys

pygame.init()

W, H = 850, 850

# Создание окна Pygame
display = pygame.display.set_mode([W, H])

# Получение списка файлов из папки с музыкой
path = os.getcwd()
songs = os.listdir(os.path.join(path, "week_7/music"))

# Установка пользовательского события для конца песни
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

# Индекс текущей играющей песни
current_song_index = 0

# Функция для воспроизведения следующей песни
def play_next_song():
    global current_song_index, songs
    current_song_index = (current_song_index + 1) % len(songs) # перемещаем текущую песню в конец списка
    pygame.mixer.music.load(os.path.join(path, "week_7/music", songs[current_song_index]))
    pygame.mixer.music.play()

# Функция для воспроизведения предыдущей песни
def play_prev_song():
    global current_song_index, songs
    current_song_index = (current_song_index - 1) % len(songs) # перемещаем текущую песню в начало списка
    pygame.mixer.music.load(os.path.join(path, "week_7/music", songs[current_song_index]))
    pygame.mixer.music.play()

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Обработка закрытия окна
            running = False
        elif event.type == SONG_END: # Обработка конца текущей песни
            play_next_song()

    # Обновление экрана
    pygame.display.update()

    # Получение нажатых клавиш
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]: # Воспроизведение текущей песни
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(os.path.join(path, "week_7/music", songs[current_song_index]))
            pygame.mixer.music.play()

    if keys[pygame.K_DOWN]: # Пауза/возобновление текущей песни
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    if keys[pygame.K_LEFT]: # Воспроизведение предыдущей песни
        play_prev_song()

# Завершение Pygame
pygame.quit()
sys.exit()
