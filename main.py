import pygame, sys
from random import randint, choice
from player import Player
from enemy import Enemy
from coin import Coin
from blood import Blood
from vegetable import Tomato, Banana, Beetroot
from farmboy_start import Farmboy_start

class Game():
    def __init__(self):
        # background
        self.bg_image = pygame.image.load('graphics/bg.png').convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))

        # player
        player_sprite = Player(screen_width, screen_height)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # enemy
        self.random_x = choice([0, 600])
        self.random_y = randint(30,370)
        enemy_sprite = Enemy((self.random_x, self.random_y))
        self.enemy = pygame.sprite.Group(enemy_sprite)
        self.enemy_adding_time = 100

        # lives
        self.life_grid = pygame.Surface((124, 18))
        self.life_grid.fill('#986372')
        self.life = pygame.Surface((12, 14))
        self.life.fill('#F7EDDC')
        self.player_live = 10
        self.life_pos = 12

        # all vegs
        self.my_banana = 0
        self.my_beetroot = 0
        self.my_tomato = 0
        self.banana = pygame.sprite.Group()
        self.banana_adding_time = randint(100, 300)
        self.beetroot = pygame.sprite.Group()
        self.beetroot_adding_time = randint(100, 300)
        self.tomato = pygame.sprite.Group()
        self.tomato_adding_time = randint(100, 300)

        self.num_banana = pygame.image.load('graphics/veg/banana/1.png').convert_alpha()
        self.num_beetroot = pygame.image.load('graphics/veg/beetroot/1.png').convert_alpha()
        self.num_tomato = pygame.image.load('graphics/veg/tomato/1.png').convert_alpha()

        # sell veg
        self.sell_ready = True
        self.sell_time = 1
        self.sell_cooldown = 400
        self.want_banana = randint(1, 10)
        self.want_beetroot = randint(1, 10)
        self.want_tomato = randint(1, 10)

        # coin
        self.coin = pygame.sprite.Group()
        self.coin_adding_time = 200

        # blood
        self.blood = pygame.sprite.Group()
        self.blood_adding_time = 400

        # score
        self.score = 0

        # level
        self.level = 1

        # font
        self.font1 = pygame.font.Font('graphics/font/Carnevalee Freakshow.TTF', 70)
        self.font2 = pygame.font.Font('graphics/font/Carnevalee Freakshow.TTF', 30)
        self.font3 = pygame.font.Font('graphics/font/Carnevalee Freakshow.TTF', 40)

        # audio
        music = pygame.mixer.Sound('sound/music.wav')
        music.set_volume(0.2)
        music.play(loops=-1)
        self.hurt_sound = pygame.mixer.Sound('sound/hurt.wav')
        self.hurt_sound.set_volume(0.3)
        self.coin_sound = pygame.mixer.Sound('sound/coin.wav')
        self.coin_sound.set_volume(0.5)
        self.blood_sound = pygame.mixer.Sound('sound/blood.wav')
        self.blood_sound.set_volume(0.4)
        self.veg_sound = pygame.mixer.Sound('sound/veg.wav')
        self.veg_sound.set_volume(0.5)
        self.sell_sound = pygame.mixer.Sound('sound/sell.wav')
        self.sell_sound.set_volume(0.5)

    def enemy_move(self):
        for enemy in self.enemy:
            if enemy.rect.x >= self.player.sprite.rect.x:
                enemy.rect.x -= 1
            if enemy.rect.x < self.player.sprite.rect.x:
                enemy.rect.x += 1
            if enemy.rect.y >= self.player.sprite.rect.y:
                enemy.rect.y -= 1
            if enemy.rect.y < self.player.sprite.rect.y:
                enemy.rect.y += 1

    def add_enemy(self):
        self.enemy_adding_time -= 1
        if self.enemy_adding_time <= 0:
            self.enemy.add(Enemy((choice([-70, 650]), randint(70,300))))
            self.get_enemy_adding_time_new()
            self.enemy_adding_time = self.enemy_adding_time_new

    def add_banana(self):
        self.banana_adding_time -= 1
        if self.banana_adding_time <= 0:
            self.banana.add(Banana((randint(50, 550), randint(100, 300))))
            self.banana_adding_time = randint(350, 700)

    def add_beetroot(self):
        self.beetroot_adding_time -= 1
        if self.beetroot_adding_time <= 0:
            self.beetroot.add(Beetroot((randint(50, 550), randint(100, 300))))
            self.beetroot_adding_time = randint(400, 700)

    def add_tomato(self):
        self.tomato_adding_time -= 1
        if self.tomato_adding_time <= 0:
            self.tomato.add(Tomato((randint(50,550), randint(100,300))))
            self.tomato_adding_time = randint(300, 700)

    def add_coin(self):
        self.coin_adding_time -= 1
        if self.coin_adding_time <= 0:
            self.coin.add(Coin((randint(50,550), randint(100,300))))
            self.coin_adding_time = randint(200, 500)

    def add_blood(self):
        self.blood_adding_time -= 1
        if self.blood_adding_time <= 0:
            self.blood.add(Blood((randint(50,550), randint(100,300))))
            self.blood_adding_time = randint(400, 600)

    def collision(self):
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:

                if pygame.sprite.spritecollide(laser, self.enemy, True):
                    laser.kill()
                    self.hurt_sound.play()
                    self.score += 5

        if self.enemy:
            for enemy in self.enemy:

                if pygame.sprite.spritecollide(enemy, self.player, False):
                    enemy.kill()
                    self.hurt_sound.play()
                    self.player_live -= 1

        if self.banana:
            for banana in self.banana:
                if pygame.sprite.spritecollide(banana, self.player, False):
                    banana.kill()
                    self.veg_sound.play()
                    self.my_banana += 1
                    # print(f"banana ={self.my_banana}")

        if self.beetroot:
            for beetroot in self.beetroot:
                if pygame.sprite.spritecollide(beetroot, self.player, False):
                    beetroot.kill()
                    self.veg_sound.play()
                    self.my_beetroot += 1
                    # print(f"beetroot ={self.my_beetroot}")

        if self.tomato:
            for tomato in self.tomato:
                if pygame.sprite.spritecollide(tomato, self.player, False):
                    tomato.kill()
                    self.veg_sound.play()
                    self.my_tomato += 1
                    # print(f"tomato ={self.my_tomato}")

        if self.coin:
            for coin in self.coin:
                if pygame.sprite.spritecollide(coin, self.player, False):
                    coin.kill()
                    self.coin_sound.play()
                    self.score += 10

        if self.blood:
            for blood in self.blood:
                if pygame.sprite.spritecollide(blood, self.player, False):
                    blood.kill()
                    self.blood_sound.play()
                    if self.player_live < 10:
                        self.player_live += 1

    def display_lives(self):
        for each_life in range(self.player_live):
            x = self.life_pos + (each_life * (self.life.get_size()[0]))
            screen.blit(self.life, (x, 372))

    def display_score(self):
        score_surf = self.font2.render(f'score: {self.score}', False, '#F7EDDC')
        score_rect = score_surf.get_rect(midtop = (300 ,360))
        screen.blit(score_surf, score_rect)

    def display_level(self):
        if self.level <= 9:
            level_surf = self.font2.render(f'level {self.level}', False, '#F7EDDC')
        else:
            level_surf = self.font2.render('level legendary', False, '#F7EDDC')
        level_rect = level_surf.get_rect(topright = (570 ,360))
        screen.blit(level_surf, level_rect)

    def display_want_veg(self):
        num_want_banana = self.font2.render(f'{self.want_banana}', False, '#F7EDDC')
        num_want_banana_rect = num_want_banana.get_rect(midtop=(125, 58))
        screen.blit(num_want_banana, num_want_banana_rect)

        num_want_beetroot= self.font2.render(f'{self.want_beetroot}', False, '#F7EDDC')
        num_want_beetroot_rect = num_want_beetroot.get_rect(midtop=(304, 58))
        screen.blit(num_want_beetroot, num_want_beetroot_rect)

        num_want_tomato = self.font2.render(f'{self.want_tomato}', False, '#F7EDDC')
        num_want_tomato_rect = num_want_tomato.get_rect(midtop = (482, 58))
        screen.blit(num_want_tomato,num_want_tomato_rect)

    def display_my_veg(self):
        num_my_banana = self.font2.render(f'{self.my_banana}', False, '#F7EDDC')
        num_my_banana_rect = num_my_banana.get_rect(midtop=(43, 273))
        screen.blit(num_my_banana, num_my_banana_rect)

        num_my_beetroot = self.font2.render(f'{self.my_beetroot}', False, '#F7EDDC')
        num_my_beetroot_rect = num_my_beetroot.get_rect(midtop=(43, 303))
        screen.blit(num_my_beetroot, num_my_beetroot_rect)

        num_my_tomato = self.font2.render(f'{self.my_tomato}', False, '#F7EDDC')
        num_my_tomato_rect = num_my_tomato.get_rect(midtop=(43, 333))
        screen.blit(num_my_tomato, num_my_tomato_rect)

    def get_enemy_adding_time_new(self):
        if self.level == 1:
            self.enemy_adding_time_new = randint(80, 180)
        elif self.level == 2:
            self.enemy_adding_time_new = randint(70, 160)
        elif self.level == 3:
            self.enemy_adding_time_new = randint(60, 140)
        elif self.level == 4:
            self.enemy_adding_time_new = randint(60, 130)
        elif self.level == 5:
            self.enemy_adding_time_new = randint(50, 130)
        elif self.level == 6:
            self.enemy_adding_time_new = randint(40, 130)
        elif self.level == 7:
            self.enemy_adding_time_new = randint(40, 100)
        elif self.level == 8:
            self.enemy_adding_time_new = randint(30, 100)
        elif self.level == 9:
            self.enemy_adding_time_new = randint(20, 100)
        elif self.level == 10:
            self.enemy_adding_time_new = randint(20, 80)

    def check_level(self):
        if 151 <= self.score <= 400:
            self.level = 2
        elif 401 <= self.score <= 800:
            self.level = 3
        elif 801 <= self.score <= 1500:
            self.level = 4
        elif 1501 <= self.score <= 3000:
            self.level = 5
        elif 3001 <= self.score <= 4500:
            self.level = 6
        elif 4501 <= self.score <= 6000:
            self.level = 7
        elif 6001 <= self.score <= 8000:
            self.level = 9
        elif 8001 <= self.score <= 10000:
            self.level = 9
        elif self.score >= 10001:
            self.level = 10

    def check_life(self):
        if self.player_live <= 0:
            for enemy in self.enemy:
                enemy.kill()
            for banana in self.banana:
                banana.kill()
            for beetroot in self.beetroot:
                beetroot.kill()
            for tomato in self.tomato:
                tomato.kill()
            for coin in self.coin:
                coin.kill()
            for blood in self.blood:
                blood.kill()
            self.gameover()

    def sell_recharge(self):
        if not self.sell_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.sell_time >= self.sell_cooldown:
                self.sell_ready = True

    def player_sell_veg(self):
        keys = pygame.key.get_pressed()
        if 70 <= self.player.sprite.rect.y <= 90:
            if 60 <= self.player.sprite.rect.x <= 180 and keys[pygame.K_s] and self.sell_ready:
                if self.my_banana >= self.want_banana:
                    self.sell_sound.play()
                    # print('sell banana')
                    self.my_banana -= self.want_banana
                    self.score += ((int(self.want_banana)) * 10)
                    self.want_banana = randint(1, 10)
                self.sell_ready = False
                self.sell_time = pygame.time.get_ticks()

            elif 230 <= self.player.sprite.rect.x <= 350 and keys[pygame.K_s] and self.sell_ready:
                if self.my_beetroot>= self.want_beetroot:
                    # print('sell beetroot')
                    self.sell_sound.play()
                    self.my_beetroot -= self.want_beetroot
                    self.score += ((int(self.want_beetroot)) * 10)
                    self.want_beetroot = randint(1, 10)
                self.sell_ready = False
                self.sell_time = pygame.time.get_ticks()

            elif 410 <= self.player.sprite.rect.x <= 530 and keys[pygame.K_s] and self.sell_ready:
                if self.my_tomato >= self.want_tomato:
                    # print('sell tomato')
                    self.sell_sound.play()
                    self.my_tomato -= self.want_tomato
                    self.score += ((int(self.want_tomato)) * 10)
                    self.want_tomato = randint(1, 10)
                self.sell_ready = False
                self.sell_time = pygame.time.get_ticks()

    def gameover(self):
        self.bg_image = pygame.image.load('graphics/bg.png').convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))
        screen.blit(self.bg_image, (0,0))

        gameover2_surf = self.font1.render('Game over', False, '#77987A')
        gameover2_rect = gameover2_surf.get_rect(midtop=(302, 162))
        screen.blit(gameover2_surf, gameover2_rect)
        gameover_surf = self.font1.render('Game over', False, '#F7EDDC')
        gameover_rect = gameover_surf.get_rect(midtop=(300, 160))
        screen.blit(gameover_surf, gameover_rect)

        score_surf = self.font3.render(f'score: {self.score}', False, '#F7EDDC')
        score_rect = score_surf.get_rect(midtop=(300, 250))
        screen.blit(score_surf, score_rect)

        exit_surf = self.font2 .render('Exit (E)', False, '#F7EDDC')
        exit_rect = exit_surf.get_rect(midtop=(300, 300))
        screen.blit(exit_surf, exit_rect)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            pygame.quit()
            sys.exit()

    def run(self):
        screen.blit(self.bg_image, (0, 0))

        self.player.update()
        self.enemy.update()
        self.banana.update()
        self.beetroot.update()
        self.tomato.update()
        self.coin.update()
        self.blood.update()

        self.display_want_veg()
        self.player.draw(screen)
        self.player.sprite.lasers.draw(screen)
        self.banana.draw(screen)
        self.beetroot.draw(screen)
        self.tomato.draw(screen)
        self.coin.draw(screen)
        self.blood.draw(screen)
        self.enemy.draw(screen)

        # lives on screen
        screen.blit(self.life_grid, (10, 370))
        screen.blit(self.num_banana, (10, 280))
        screen.blit(self.num_beetroot, (10, 310))
        screen.blit(self.num_tomato, (10, 340))
        self.display_my_veg()
        self.display_lives()
        self.display_score()
        self.display_level()

        self.enemy_move()
        self.add_enemy()
        self.collision()
        self.add_banana()
        self.add_beetroot()
        self.add_tomato()
        self.add_coin()
        self.add_blood()
        self.check_level()
        self.check_life()
        self.player_sell_veg()
        self.sell_recharge()

class Homepage():
    def __init__(self):
        farmboy_sprite = Farmboy_start()
        self.farmboy = pygame.sprite.GroupSingle(farmboy_sprite)

        self.font1 = pygame.font.Font('graphics/font/Carnevalee Freakshow.TTF', 70)
        self.font2 = pygame.font.Font('graphics/font/Carnevalee Freakshow.TTF', 25)
        self.font3 = pygame.font.Font('graphics/font/Carnevalee Freakshow.TTF', 20)

        self.bg_image = pygame.image.load('graphics/bg.png').convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))
        self.tutorial_image = pygame.image.load('graphics/tutorial1.jpeg').convert_alpha()
        self.tutorial_on_screen = False

        self.button_sound = pygame.mixer.Sound('sound/button.wav')
        self.button_sound.set_volume(0.4)
        self.button_ready = True
        self.button_time = 0
        self.button_cooldown = 300

    def gamename(self):
        gamename2_surf = self.font1.render('Farmboy Fight', False, '#77987A')
        gamename2_rect = gamename2_surf.get_rect(center=(303, 193))
        screen.blit(gamename2_surf, gamename2_rect)
        gamename_surf = self.font1.render('Farmboy Fight', False, '#F7EDDC')
        gamename_rect = gamename_surf.get_rect(center = (300 ,190))
        screen.blit(gamename_surf, gamename_rect)

    def press_space(self):
        press_space_surf = self.font2.render('press space to start', False, '#F7EDDC')
        press_space_rect = press_space_surf.get_rect(center = (300 ,320))
        screen.blit(press_space_surf, press_space_rect)

    def press_tutorial(self):
        press_tutorial_surf = self.font3.render("tutorial (t)", False, '#F7EDDC')
        press_tutorial_rect = press_tutorial_surf.get_rect(center=(300, 345))
        screen.blit(press_tutorial_surf, press_tutorial_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_t] and self.button_ready:
            self.tutorial_on_screen = True
            self.button_sound.play()

    def display_tutorial(self):
        if self.tutorial_on_screen:
            screen.blit(self.tutorial_image, (0, 0))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.tutorial_on_screen = False
                self.button_sound.play()

    def run(self):
        screen.blit(self.bg_image, (0, 0))
        self.gamename()
        self.press_space()
        self.press_tutorial()
        self.farmboy.update()
        self.farmboy.draw(screen)
        self.display_tutorial()

pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Farmboy Fight')
clock = pygame.time.Clock()

game_active = False
homepage_active = True
game = Game()
homepage = Homepage()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
            background_active = False

    screen.fill('white')
    if homepage_active:
        homepage.run()

    if game_active:
        game.run()

    pygame.display.flip()
    clock.tick(60)