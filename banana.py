import pygame

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