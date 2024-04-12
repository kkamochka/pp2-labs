import pygame
import os
pygame.init()

W, H = 850, 850

display = pygame.display.set_mode([W, H])
path = os.getcwd()
list = os.listdir(os.path.join(path, "week_7/music")) 

# instasamka_zadengida = pygame.mixer.music.load(os.path.join(path, "week_7/music/INSTASAMKA – ЗА ДЕНЬГИ ДА.mp3"))
# instasamka_otkltel = pygame.mixer.music.load(os.path.join(path, "week_7/music/INSTASAMKA – Отключаю телефон.mp3"))
# doiacat_paintthetownred = pygame.mixer.music.load(os.path.join(path, "week_7/music/Doja Cat – Paint The Town Red.mp3"))
    

running = True
while running:
    
    pygame.display.update()
    
    for i in pygame.i.get():
        if i.type == quit:
            running = False
            pygame.quit()
            
            
    buttons = pygame.key.get_pressed()
    if buttons[pygame.K_UP]:
        pygame.mixer.music.play()
    
    if buttons[pygame.K_DOWN]:
        pygame.mixer.music.pause()
        
    if buttons[pygame.K_LEFT]:
        pygame.mixer.music.play()
                
    
    
pygame.exit()