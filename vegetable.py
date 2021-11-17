import pygame

class Tomato(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        tomato1 = pygame.image.load('graphics/veg/tomato/1.png').convert_alpha()
        tomato2 = pygame.image.load('graphics/veg/tomato/2.png').convert_alpha()
        tomato3 = pygame.image.load('graphics/veg/tomato/3.png').convert_alpha()
        self.tomato = [tomato1, tomato2, tomato3]
        self.frame_index = 0
        self.image = self.tomato[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        self.tomato_stay_time = 500

    def tomato_animation(self):
        self.frame_index += 0.08
        if self.frame_index >= len(self.tomato):
            self.frame_index = 0
        self.image = self.tomato[int(self.frame_index)]

    def tomato_delete(self):
        self.tomato_stay_time -= 1
        if self.tomato_stay_time <= 0:
            self.kill()
            self.tomato_stay_time = 500

    def update(self):
        self.tomato_animation()
        self.tomato_delete()

class Banana(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        banana1 = pygame.image.load('graphics/veg/banana/1.png').convert_alpha()
        banana2 = pygame.image.load('graphics/veg/banana/2.png').convert_alpha()
        banana3 = pygame.image.load('graphics/veg/banana/3.png').convert_alpha()
        self.banana = [banana1, banana2, banana3]
        self.frame_index = 0
        self.image = self.banana[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        self.banana_stay_time = 500

    def banana_animation(self):
        self.frame_index += 0.08
        if self.frame_index >= len(self.banana):
            self.frame_index = 0
        self.image = self.banana[int(self.frame_index)]

    def banana_delete(self):
        self.banana_stay_time -= 1
        if self.banana_stay_time <= 0:
            self.kill()
            self.banana_stay_time = 500

    def update(self):
        self.banana_animation()
        self.banana_delete()

class Beetroot(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        beetroot1 = pygame.image.load('graphics/veg/beetroot/1.png').convert_alpha()
        beetroot2 = pygame.image.load('graphics/veg/beetroot/2.png').convert_alpha()
        beetroot3 = pygame.image.load('graphics/veg/beetroot/3.png').convert_alpha()
        self.beetroot = [beetroot1, beetroot2, beetroot3]
        self.frame_index = 0
        self.image = self.beetroot[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        self.beetroot_stay_time = 500

    def beetroot_animation(self):
        self.frame_index += 0.08
        if self.frame_index >= len(self.beetroot):
            self.frame_index = 0
        self.image = self.beetroot[int(self.frame_index)]

    def beetroot_delete(self):
        self.beetroot_stay_time -= 1
        if self.beetroot_stay_time <= 0:
            self.kill()
            self.beetroot_stay_time = 500

    def update(self):
        self.beetroot_animation()
        self.beetroot_delete()