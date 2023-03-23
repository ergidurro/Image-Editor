from pygame import *

class loja(sprite.Sprite):
    def __init__(self, player,size1, size2, x1, y1, shpejtesi, x2, x3, y2, y3):
        super().__init__()

        self.imazh = transform.scale(image.load(player), (size1, size2))
        self.speed = shpejtesi

        self.rect = self.imazh.get_rect()
        self.rect.x = x1
        self.rect.y = y1

        self.x2 = x2
        self.x3 = x3
        self.y2 = y2
        self.y3 = y3

    def reset(self):
        game_window.blit(self.imazh, (self.rect.x,self.rect.y))

class Player(loja):
    def move(self):
        press_key = key.get_pressed()
        if press_key[K_UP] and self.rect.y > 5:
            self.rect.y -= x
        if press_key[K_DOWN] and self.rect.y < 405:
            self.rect.y += x
        if press_key[K_RIGHT] and self.rect.x < 605:
            self.rect.x += x
        if press_key[K_LEFT] and self.rect.x > 5:
            self.rect.x -= x

class Enemy(loja):
    ana_e_lojtarit = 'left'
    def move(self):
        if self.rect.x <= 520:
            self.ana_e_lojtarit = 'right'
        if self.rect.x >= 615:
            self.ana_e_lojtarit = 'left'
        if self.ana_e_lojtarit == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, ngjyra_1, ngjyra_2, ngjyra_3, muri_x, muri_y, muri_lartesi, muri_gjeresi):
        self.ngjyra_1 = ngjyra_1
        self.ngjyra_2 = ngjyra_2
        self.ngjyra_3 = ngjyra_3
        self.muri_lartesi = muri_lartesi
        self.muri_gjeresi = muri_gjeresi

        self.imazh = Surface([self.muri_gjeresi, self.muri_lartesi])
        self.imazh.fill((ngjyra_1, ngjyra_2, ngjyra_3))

        self.rect = self.imazh.get_rect()
        self.rect.x = muri_x
        self.rect.y = muri_y

    def draw(self):
        draw.rect(game_window, (self.ngjyra_1, self.ngjyra_2, self.ngjyra_3), (self.rect.x, self.rect.y, self.muri_gjeresi, self.muri_lartesi))

game_window = display.set_mode((700, 500))
display.set_caption('Catch')
background = transform.scale(image.load('background1.png'), (700, 500))
player1 = Player('sprite3.png',60,60, 0, 355, 2, 5, 355, 605, 5)
player2 = Enemy('sprite1.png',60, 60, 600, 200, 2, 5, 355, 605, 5)
treasure = loja('treasure.png',100, 100, 600, 370, 2, 5, 355, 605, 5)
muri = Wall(102, 255, 255, 100, 20, 300, 20)
muri2 = Wall(102, 255, 255, 100, 5, 20, 550)
muri3 = Wall(102, 255, 255, 100, 450, 20, 500)
muri4 = Wall(102, 255, 255, 210, 150, 300, 20)
muri5 = Wall(102, 255, 255, 370, 20, 300, 20)
muri6 = Wall(102, 255, 255, 500, 150, 300, 20)

finish = False

x = 10
clock = time.Clock()
FPS = 60
font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!', True, (51, 255, 51))
lose = font.render('YOU LOSE!', True, (255, 0, 0))

mixer.init()
mixer.music.load('mariotheme.ogg')
mixer.music.play()

winner = mixer.Sound('victory.ogg')
loser = mixer.Sound('lose.ogg')

game = True
while game == True:
    if finish != True:
        game_window.blit(background, (0,0))
        player1.reset()
        player1.move()
        player2.reset()
        player2.move()
        treasure.reset()
        muri.draw()
        muri2.draw()
        muri3.draw()
        muri4.draw()
        muri5.draw()
        muri6.draw()

    if sprite.collide_rect(player1, player2) or sprite.collide_rect(player1, muri) or sprite.collide_rect(player1, muri2) or sprite.collide_rect(player1, muri3) or sprite.collide_rect(player1, muri4) or sprite.collide_rect(player1, muri5) or sprite.collide_rect(player1, muri6):
        finish = True
        game_window.blit(lose, (200, 200))
        winner.play()

    if sprite.collide_rect(player1, treasure):
        finish = True
        game_window.blit(win, (200, 200))
        loser.play()

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()