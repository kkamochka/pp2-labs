
import pygame, sys
from pygame.locals import *
import random, time


pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
MONEY_SCORE = 0
earned_coins = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("week_9//ex_1//pictures//AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() #для вызова конструктора базового класса
        self.image = pygame.image.load("week_9//ex_1//pictures//Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE # для доступа к глобальной переменной
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("week_9//ex_1//pictures//Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0: #предотвращает от выхода за левую часть экрана.
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH: #предотвращает от выхода за правую часть экрана.       
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self, coin_image, weight):
            super().__init__() 
            self.image = pygame.image.load(coin_image)
            self.image = pygame.transform.scale(self.image, (50, 50))

            self.weight = weight

            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(50,SCREEN_WIDTH-50), 0)

            self.flag = False #для отслеживания состояния монеты
    
    def move(self):
        self.rect.move_ip(0,SPEED)
        self.flag = 0
        if (self.rect.bottom > 600):
            self.flag = True
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin("week_9//ex_1//pictures//Coin.png", 1) 
C2 = Coin("week_9//ex_1//pictures//Coin2.png", 5)


#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

money = pygame.sprite.Group()
money.add(C1)
money.add(C2)

money_to_move = 0

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1  # USEREVENT - значение для пользовательских событий.
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if earned_coins - 3 == 0:
        earned_coins = 0
        SPEED += 0.5


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    money_score = font_small.render(str(MONEY_SCORE), True, BLACK)
    DISPLAYSURF.blit(money_score, (SCREEN_WIDTH - 50, 10))

    for entity in all_sprites:   #обновление и перемещение всех спрайтов с помощью move и его изображение  отрисовывается на экране по его прямоугольнику.
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    i = 0
    for entity in money:
        if i == money_to_move:
            entity.move()
            DISPLAYSURF.blit(entity.image, entity.rect)

            if entity.flag:
                entity.rect.center = (random.randint(-50, SCREEN_WIDTH - 40), 0)
                money_to_move = random.randrange(0, 2) # 2 is len of my coins
        i += 1
                

        

    #Обработка столкновений и действий при окончании игры:
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('week_9//ex_1//songs//crash.wav').play()
        time.sleep(1)
                
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        
        for entity in money:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()    

    # Commented
    
    for entity in money:
        if pygame.Rect.colliderect(entity.rect, P1.rect):  #толкновение монеты с игроком 
            entity.rect.center = (random.randint(-50, SCREEN_WIDTH - 40), 0)
            money_to_move = random.randrange(0, 2) 
            MONEY_SCORE += entity.weight
            earned_coins += 1
        
        
    pygame.display.update()
    FramePerSec.tick(FPS)