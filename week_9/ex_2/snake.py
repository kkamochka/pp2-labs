import pygame
import random
import datetime

def game_over(red,w,h):
    text = font.render("Press space to play again",True, red) 
    text_rect = text.get_rect(center = (w//2,h//2))
    screen.blit(text,text_rect)
def score(counter,white):
    text = font_for_score.render(f"Score: {counter}",True,white)
    text_rect = text.get_rect(center = (60,20))
    screen.blit(text,text_rect)
def level(lev,white):
    text = font_for_score.render(f"lv: {lev}",True,white)
    text_rect = text.get_rect(center = (50,45))
    screen.blit(text,text_rect)
    
w, h = 900,700
pygame.init()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Snake")
run = True
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
x,y = w//2,h//2
pos = (x,y,50,50)
z,t = random.choice(range(1,800)),random.choice(range(1,600))

font = pygame.font.SysFont('Times New Roman',70)
font_for_score = pygame.font.SysFont("Times New Roman",30)

apple = pygame.image.load("week_8/ex_2/pictures/apple.png")
apple_rect = apple.get_rect(center = (z,t))

apple_green = pygame.image.load("week_8/ex_2/pictures/green_apple.png")
green_rect = apple_green.get_rect(center = (z,t))

apple_yellow = pygame.image.load("week_8/ex_2/pictures/yellow_apple.png")
yellow_rect = apple_yellow.get_rect(center = (z,t))

flag_left = False
flag_right = False
flag_up = False
flag_down = False
game = True
clock = pygame.time.Clock()
fps = 20
once = True
counter = 0
lev = 0
length = False
g,a = 50,50
q = 10
segments = [pos]
press_r = True #эти флаги нужны чтобы не двигаться в обратном направление если движется вправо то нажать на лево нельзя
press_up = True
press_down = True
press_l = True
flag = False
number = 1 #служит для смены яблока
seconds = datetime.timedelta(seconds = 10)
current_time = datetime.datetime.now()
current_seconds = current_time.second
change_cord_apple = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                counter = 0
                lev = 0
                q = 10
                game = True
                x,y = w//2,h//2
                pos = (x,y,50,50)
                segments.clear()
                
            if event.key == pygame.K_LEFT and press_l:
                if game:
                   flag_left = True
                   flag_right = False
                   flag_up = False
                   flag_down = False
                
            elif event.key == pygame.K_RIGHT and press_r:
                if game:
                   flag_left = False
                   flag_right = True
                   flag_up = False
                   flag_down = False
                
            elif event.key == pygame.K_UP and press_up:   
                if game:
                   flag_left = False
                   flag_right = False
                   flag_up = True
                   flag_down = False
                   
            elif event.key == pygame.K_DOWN and press_down:
                if game:
                   flag_left = False
                   flag_right = False
                   flag_up = False
                   flag_down = True
                
    screen.fill(black)
    score(counter,white)
    level(lev,white)

    if current_time + datetime.timedelta(seconds = 5) <= datetime.datetime.now():
        if game:
           change_cord_apple = True
        

    if once: #once нужен для того чтобы шарик рисовался в одном месте пока змейка не соприкоснется с ним
        apple_rect = apple.get_rect(center = (z,t))
        green_rect = apple_green.get_rect(center = (z,t))
        yellow_rect = apple_yellow.get_rect(center = (z,t))
        if number == 1:
           screen.blit(apple,apple_rect)
        elif number == 2:
            screen.blit(apple_green,green_rect)
        elif number == 3:
            screen.blit(apple_yellow,yellow_rect)

    
    if abs(x - z) <= 60 and abs(y - t) <= 62:
        counter += 1
        if counter % 5 == 0:
           lev += 1
           flag = True
        once = False
        if number == 2:
            q += 0.5 #если съел зеленое яблоко то скорость увеличивается на 0.5 и размер на 0.5 станет больше
        elif number == 3:
            q += 1
        change_cord_apple = True
        
    else:
        once = True
        if len(segments) != 0:# из за того что очищаю список когда нажимаю на пробел пришлось сделать это условие когда только есть элементы в списке только тогда удалять
           segments.pop(0)

    if change_cord_apple:
        r,i = z,t
        z,t = random.choice(range(50,840)),random.choice(range(50,640))
        number = random.choice(range(1,4))
        if (r == z and i == t) or (z == x and t == y): #меняем координаты заново если шарик создался на змейке или на том же месте где только что съели
           z,t = random.choice(range(1,800)),random.choice(range(1,600))
           apple_rect = apple.get_rect(center = (z,t))
           screen.blit(apple,apple_rect)
        current_time = datetime.datetime.now()
        current_seconds = current_time.second
        change_cord_apple = False

        
    if game == False: #означает змейка дошла границ экрана и отображается текст, в случаи нажатии кнопки пробел game станет true a это значит дальше не будет рисоваться текст а оставшийся текст закрасит черный цвет
       game_over(white,w,h)
       flag_left = False
       flag_right = False
       flag_up = False
       flag_down = False

    if flag_left:
       if x <= 7:
          game = False
          continue
       press_r = False
       press_up = True
       press_down = True
       if counter % 5 == 0 and counter != 0 and flag:
           q += 1
       flag = False
       x -= q
       pos = (x,y,g,a)
    elif flag_right:
        if x >= w - 50:
           game = False
           continue
        press_l = False
        press_up = True
        press_down = True
        if counter % 5 == 0 and counter != 0 and flag:
           q += 1
        flag = False
        x += q
        pos = (x,y,g,a)
    elif flag_up:
        if y <= 7:
           game = False
           continue
        press_r = True
        press_l = True
        press_down = False
        if counter % 5 == 0 and counter != 0 and flag:
           q += 1
        flag = False
        y -= q
        pos = (x,y,g,a)
    elif flag_down:
        if y >= h - 50:
           game = False
           continue
        press_r = True
        press_up = False
        press_l = True
        if counter % 5 == 0 and counter != 0 and flag:
           q += 1
        flag = False
        y += q
        pos = (x, y, g,a)
    segments.append(pos)
    
    for k in range(1, len(segments)):
        if segments[0] == segments[k]:
           game = False
           break
    for segment in segments:
        pygame.draw.rect(screen, green, (segment[0],segment[1], g, a))
        pygame.draw.rect(screen,black,(segment[0],segment[1],g,a),1)
    pygame.display.flip()
    clock.tick(fps)
    
pygame.quit()
            
"""При новым достижение уровня змейка движется на 1 пиксель больше тоесть начинает ускорятся"""