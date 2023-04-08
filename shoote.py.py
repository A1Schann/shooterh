#Создай собственный Шутер!
from random import *
from pygame import *

window  = display.set_mode((700,500))
display.set_caption("шутер")


background =transform.scale(image.load("galaxy.jpg"), (700,500))
game = True
finish = True
mixer.init()



font.init()
font1 = font.Font(None, 35)
font2 = font.Font(None, 35)
font3 = font.Font(None,350)
font4 = font.Font(None,350)

lost = 0
win = 0
clock = time.Clock()
FPS = 60




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def update(self):
        global lost
        global win
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -40
            self.rect.x = randint(25,500)
            lost += 1
            win += 0
    def fire(self):
        bullet = Bullet("bullet.png",self.rect.centerx -5, self.rect.y -15,19,23, randint(4,7))
        bullets.add(bullet)

     

        

    def showhero(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def uprav(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 5:
            self.kill()    

player = GameSprite('ship-B1T_qSU44-transformed.png', 250 ,400,60,60, 10)
monsters = sprite.Group()
bullets = sprite.Group()

if win < 10:
    for i in range(4):
        monster = GameSprite('stardeath-transformed.png', randint(25,500), -140,55,46, randint(1,5))
        monsters.add(monster)
else:
    monster.rect.y =1000
    monster.rect.x = 1000


while game:    
    window.blit(background,(0,0))
    player.showhero()
    monster.showhero()
    player.uprav()
    monsters.draw(window)
    monsters.update()
    losetxt = font1.render('Пропущено:' + str(lost), 1, (255,215,0))   
    wintxt = font2.render('Cбито:' + str(win), 1, (255,225,0))   
    window.blit(losetxt,(5,10))
    window.blit(wintxt,(20,40))
    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if kp[K_SPACE]:
            player.fire()


    bullets.update()
    bullets.draw(window)
    if sprite.groupcollide(monsters, bullets, True, True):
            win = win + 1
            monster = GameSprite("stardeath-transformed.png", randint(80, 620), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
            if win > 3:
                finish = True
                showhero = False
                update = False
                player.rect.y = 900
                player.rect.x = 900
                background =transform.scale(image.load("Death_star_2png-transformed.png"), (700,500))
                
                
                
                
                
            if lost > 10:
                loser = font4.render("Вы проиграли!",1,(70,70,0))
                window.blit(loser,(50,90))
                time.delay(1000)
                exit()



    clock.tick(FPS)         
    display.update()