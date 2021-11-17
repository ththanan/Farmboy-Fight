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