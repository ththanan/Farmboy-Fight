import pygame

class Blood(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        blood1 = pygame.image.load('graphics/blood/1.png').convert_alpha()
        blood2 = pygame.image.load('graphics/blood/2.png').convert_alpha()
        blood3 = pygame.image.load('graphics/blood/3.png').convert_alpha()
        blood4 = pygame.image.load('graphics/blood/4.png').convert_alpha()
        blood5 = pygame.image.load('graphics/blood/5.png').convert_alpha()
        self.blood = [blood1, blood2, blood3, blood4, blood5]
        self.frame_index = 0

        self.image = self.blood[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        self.blood_stay_time = 500

    def blood_animation(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.blood):
            self.frame_index = 0
        self.image = self.blood[int(self.frame_index)]

    def blood_delete(self):
        self.blood_stay_time -= 1
        if self.blood_stay_time <= 0:
            self.kill()
            self.blood_stay_time = 500

    def update(self):
        self.blood_animation()
        self.blood_delete()
