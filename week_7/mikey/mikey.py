import pygame  
import os
import datetime
pygame.init()

W, H = 850, 850

display = pygame.display.set_mode([W, H])
pygame.display.set_caption("Mikey")

clock = pygame.time.Clock()

path = os.getcwd()
mainclock_img = pygame.image.load(os.path.join(path, "week_7/mikey/mainclock.png"))
mainclock_rect = mainclock_img.get_rect(center = display.get_rect().center)

rightarm_img = pygame.image.load(os.path.join(path, "week_7/mikey/rightarm.png"))
rightarm_img = pygame.transform.rotate(rightarm_img, -55.5)
rightarm_rect = rightarm_img.get_rect(center = display.get_rect().center)

leftarm_img = pygame.image.load(os.path.join(path, "week_7/mikey/leftarm.png"))
leftarm_img = pygame.transform.rotate(leftarm_img, -4)
leftarm_rect = leftarm_img.get_rect(center = display.get_rect().center)

run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    
    if not run : 
        break
    
    display.blit(mainclock_img, mainclock_rect)
    
    curtime = datetime.datetime.now()
    cursec = curtime.second
    curmin = curtime.minute
    
    secang = cursec * 6 
    minang = (curmin * 60 + cursec) * 0.1
    
    
    sec_img = pygame.transform.rotate(leftarm_img, -secang)
    leftarm_rect = sec_img.get_rect(center = mainclock_rect.center)

    min_img = pygame.transform.rotate(rightarm_img, -minang)
    rightarm_rect = min_img.get_rect(center = mainclock_rect.center)
    
    display.blit(sec_img, leftarm_rect)
    display.blit(min_img, rightarm_rect)
    
    
    
    
    pygame.display.flip()
    clock.tick(1)


pygame.exit()