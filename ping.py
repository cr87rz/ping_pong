from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed_x, player_speed_y):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.size_x = size_x
        self.size_y = size_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
    
        if keys_pressed[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed_y
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
    
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed_y
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
            
class Ball(GameSprite):
    global finish, puntos
    def update(self):
        global puntos
        
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.x > 670:
            Game_over = font2.render('P2 LOSE',1,(255,255,255))
            window.blit(Game_over, (430,400))
            finish = True
        if self.rect.x < -10:
            Game_over = font2.render('P1 LOSE',1,(255,255,0))
            window.blit(Game_over, (50,50))
            finish = True
            
        if self.rect.y > 450:
            self.speed_y *= -1
        if self.rect.y < 0:
            self.speed_y *= -1
            
        collision_ball_player1 = sprite.collide_rect(barrera1, self)
        collision_ball_player2 = sprite.collide_rect(barrera2, self)
        
        if collision_ball_player1:
            puntos += 1
            self.speed_x *= -1

        if collision_ball_player2:
            self.speed_x *= -1
            puntos += 1

font.init()
font1 = font.SysFont('Arial',36)
font2 = font.SysFont('Arial',70)

win_height = 500
win_width = 700
window = display.set_mode((win_width,win_height))
display.set_caption('Pong')

background = transform.scale(image.load('espacio.jpg'), (win_width,win_height))

clock = time.Clock()



barrera1 = Player1('barrera1.png', 10, 200, 15, 105, 0, 15)
barrera2 = Player2('barrera2.png', 675, 200, 15, 105, 0, 15)

pelota = sprite.Group()
pelota.add(Ball('lunaa.png', 322, 200, 80, 80, 5, 5))


puntos = 0
fps = 40
game = True
finish = False

crear_bola = False 
    
while game:
    clock.tick(fps)
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish == False:
            
        window.blit(background,(0, 0))
        
        barrera1.update()
        barrera2.update()
        pelota.update()
        
        if puntos %10 == 2:
            crear_bola = True
        if crear_bola and puntos %10 == 3:
            pelota.add(Ball('lunaa.png', 200, 100, 80, 80, 5, 5))
            crear_bola = False
            
            
        
        barrera1.reset()
        barrera2.reset()
        
        pelota.draw(window)
        
        display.update()
    elif finish == True:
        display.update()

        
    #else:  
        #time.delay(2000)
        #finish = False
        
        #barrera1.empty()
        #barrera2.empty()
        #pelota.empty()