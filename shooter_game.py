#Создай собственный Шутер!
#тест

#суперкрутоеприложение

from pygame import *
from random import randint
mixer.init()
#mixer.music.load('94150.mp3')
#mixer.music.play()
fire_sound = mixer.Sound('fike.ogg')
font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN OMG', True, (225, 225, 225))
lose = font1.render("You lose!! it's sad!", True, (180, 0, 0))
font2 = font.SysFont('Arial', 36)

win_width = 700
win_height = 500
lost = 0
score = 0
goal = 500
max_lost = 100
img_bullet = ('patrone.png')
display.set_caption('НЛО ШУТЕР')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('fone.png'), (win_width, win_height))
run = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x    
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update (self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 60, 100, -15)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update (self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

            

ship = Player('python.png', 5, win_height - 100, 80, 80, 10)
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy('kosta.png', randint(80, win_width -80), -40, 50, 50, randint(1, 5))
    monsters.add(monster)

bullets = sprite.Group()

while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                fire_sound.play()
                ship.fire()
    if not finish:
        
        window.blit(background, (0, 0))

        text = font2.render('Счёт:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        text_lose = font2.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        ship.update()
        monsters.update()
        bullets.update()
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy('kosta.png', randint(80, win_width -80), -40, 50, 50, randint(1, 5))
            monsters.add(monster)
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (80, 200))
        if score >= goal:
            finish = True
            window.blit(win, (100, 200))
        display.update()
    time.delay (50)









