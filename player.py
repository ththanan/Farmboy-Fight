import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, max_x, max_y):
        super().__init__()
        self.moving = False

        idle1 = pygame.image.load('graphics/warrior/idle/1.png').convert_alpha()
        idle2 = pygame.image.load('graphics/warrior/idle/2.png').convert_alpha()
        idle3 = pygame.image.load('graphics/warrior/idle/3.png').convert_alpha()
        idle4 = pygame.image.load('graphics/warrior/idle/4.png').convert_alpha()
        idle5 = pygame.image.load('graphics/warrior/idle/5.png').convert_alpha()
        self.idle = [idle1, idle2, idle3, idle4, idle5]

        run1 = pygame.image.load('graphics/warrior/run/1.png').convert_alpha()
        run2 = pygame.image.load('graphics/warrior/run/2.png').convert_alpha()
        run3 = pygame.image.load('graphics/warrior/run/3.png').convert_alpha()
        run4 = pygame.image.load('graphics/warrior/run/4.png').convert_alpha()
        run5 = pygame.image.load('graphics/warrior/run/5.png').convert_alpha()
        run6 = pygame.image.load('graphics/warrior/run/6.png').convert_alpha()
        run7 = pygame.image.load('graphics/warrior/run/7.png').convert_alpha()
        run8 = pygame.image.load('graphics/warrior/run/8.png').convert_alpha()
        run9 = pygame.image.load('graphics/warrior/run/9.png').convert_alpha()
        run10 = pygame.image.load('graphics/warrior/run/10.png').convert_alpha()
        self.run = [run1, run2, run3, run4, run5, run6, run7, run8, run9, run10]

        self.frame_index = 0
        self.image = self.idle[self.frame_index]
        self.rect = self.image.get_rect(center=(300, 265))

        self.max_x = max_x
        self.max_y = max_y

        self.speed = 4
        self.facing_right = True

        # laser
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 300
        self.lasers = pygame.sprite.Group()
        self.shoot_sound = pygame.mixer.Sound('sound/shoot.wav')
        self.shoot_sound.set_volume(0.5)

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.shoot_sound.play()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = self.run[int(self.frame_index)]
            self.facing_right = True
            self.running()
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = self.run[int(self.frame_index)]
            self.facing_right = False
            self.running()
        elif keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.image = self.run[int(self.frame_index)]
            self.running()
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.image = self.run[int(self.frame_index)]
            self.running()
        else:
            self.moving = False
            self.idling()
            self.image = self.idle[int(self.frame_index)]


    def left_right(self):
        if self.facing_right:
            self.image = self.image
        else:
            self.image = pygame.transform.flip(self.image, True, False)

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x:
            self.rect.right = self.max_x
        if self.rect.top <= 70:
            self.rect.top = 70
        if self.rect.bottom >= 390:
            self.rect.bottom = 390

    def idling(self):
        self.frame_index += 0.2
        if self.frame_index >= len(self.idle):
            self.frame_index = 0
        self.image = self.idle[int(self.frame_index)]

    def running(self):
        self.rect.x += 0.3
        self.frame_index += 0.1
        if self.frame_index >= len(self.run):
            self.frame_index = 0
        self.image = self.run[int(self.frame_index)]

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def shoot_laser(self):
        # print('shoot')
        self.lasers.add(Laser(self.rect.center,self.facing_right))

    def update(self):
        self.get_input()
        self.left_right()
        self.constraint()
        self.recharge()
        self.lasers.update()
