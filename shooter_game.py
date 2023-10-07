from pygame import *
from random import randint
# подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('ТЫ ПОБЕДИЛ!', True, (255, 255, 255))
lose = font1.render('ТЫ ПРОИГРАЛ!', True, (180, 0, 0))

r = 0
font2 = font.SysFont('Arial', 36)

img_back = "galaxy.jpg" # фон игры
img_bullet = "bullet.png" # пуля
img_hero = "rocket.png" # герой
img_enemy = "ufo.png" # враг
img_asteroid = "asteroid.png"
 
score = 0 # сбито кораблей
goal = 10 # столько кораблей нужно сбить для победы
lost = 0 # пропущено кораблей
max_lost = 3 # проиграли, если пропустили столько
 
# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    #def relout(self):
        #if keys[R]:
            #r = 35 

    def fire1(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
    def fire2(self):
        bullet = Bullet(img_bullet, self.rect.centerx-10, self.rect.top, 15, 20, -15)
        bullet1 = Bullet(img_bullet, self.rect.centerx+10, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
        bullets.add(bullet1)
    def fire3(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullet1 = Bullet(img_bullet, self.rect.centerx-10, self.rect.top, 15, 20, -15)
        bullet2 = Bullet(img_bullet, self.rect.centerx+10, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
        bullets.add(bullet2)
        bullets.add(bullet1)
    def fire4(self):
        bullet2 = Bullet(img_bullet, self.rect.centerx-20, self.rect.top, 15, 20, -15)
        bullet3 = Bullet(img_bullet, self.rect.centerx-10, self.rect.top, 15, 20, -15)
        bullets.add(bullet3)
        bullets.add(bullet2)
        bullet = Bullet(img_bullet, self.rect.centerx+20, self.rect.top, 15, 20, -15)
        bullet1 = Bullet(img_bullet, self.rect.centerx+10, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
        bullets.add(bullet1)
    def fire5(self):
        bullet2 = Bullet(img_bullet, self.rect.centerx-20, self.rect.top, 15, 20, -15)
        bullet3 = Bullet(img_bullet, self.rect.centerx-10, self.rect.top, 15, 20, -15)
        bullet4 = Bullet(img_bullet, self.rect.centerx+20, self.rect.top, 15, 20, -15)
        bullets.add(bullet2)
        bullets.add(bullet3)
        bullets.add(bullet4)
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullet1 = Bullet(img_bullet, self.rect.centerx+10, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
        bullets.add(bullet1)
   
   
class Enemy(GameSprite):
    # движение врага
    def update(self):
        self.rect.y += self.speed
        global lost
        # исчезает, если дойдет до края экрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
 
# класс спрайта-пули   
class Bullet(GameSprite):
    # движение врага
    def update(self):
        self.rect.y += self.speed
        # исчезает, если дойдет до края экрана
        if self.rect.y < 0:
            self.kill()
 
# Создаем окошко
win_width = 1000
win_height = 700
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
 
# создаем спрайты
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
 
# создание группы спрайтов-врагов
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)
 
bullets = sprite.Group()
# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
        # событие нажатия на пробел - спрайт стреляет
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                    a = randint(1,5)
                    if a == 1:
                        ship.fire1()
                        r += 1
                    elif a == 2:
                        ship.fire2()
                        r += 2
                    elif a == 3:
                        ship.fire3()
                        r += 3
                    elif a == 4:
                        ship.fire4()
                        r += 4
                    elif a == 5:
                        ship.fire5()
                        r += 5
                
 
  # сама игра: действия спрайтов, проверка правил игры, перерисовка
    if not finish:
        # обновляем фон
        window.blit(background,(0,0))

        # пишем текст на экране
        text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        text_lose = font2.render("Кол-во патрон потрачено: " + str(r), 1, (255, 255, 255))
        window.blit(text_lose, (10, 80))

        # производим движения спрайтов
        ship.update()
        monsters.update()
        bullets.update()

        # обновляем их в новом местоположении при каждой итерации цикла
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
 
        # проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            # этот цикл повторится столько раз, сколько монстров подбито
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
            if score >= 2:
                ship.fire1()


        # возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True # проиграли, ставим фон и больше не управляем спрайтами.
            window.blit(lose, (200, 200))

        # проверка выигрыша: сколько очков набрали?
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))

        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)