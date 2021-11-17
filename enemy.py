import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        vec = pygame.math.Vector2
        run1 = pygame.image.load('graphics/enemy/run/1.png').convert_alpha()
        run2 = pygame.image.load('graphics/enemy/run/2.png').convert_alpha()
        run3 = pygame.image.load('graphics/enemy/run/3.png').convert_alpha()
        run4 = pygame.image.load('graphics/enemy/run/4.png').convert_alpha()
        run5 = pygame.image.load('graphics/enemy/run/5.png').convert_alpha()
        # run6 = pygame.image.load('graphics/enemy/run/6.png').convert_alpha()
        # run7 = pygame.image.load('graphics/enemy/run/7.png').convert_alpha()
        # run8 = pygame.image.load('graphics/enemy/run/8.png').convert_alpha()
        self.run = [run1, run2, run3, run4, run5]

        self.frame_index = 0
        self.image = self.run[self.frame_index]
        self.rect = self.image.get_rect(center=(pos))

        self.enemy_speed = 1
        self.vel = vec(0, 0)

    def running(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.run):
            self.frame_index = 0
        self.image = self.run[int(self.frame_index)]

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 600:
            self.rect.right = 600
        if self.rect.top <= 20:
            self.rect.top = 20
        if self.rect.bottom >= 390:
            self.rect.bottom = 390

    def update(self):
        self.running()
        self.constraint()
