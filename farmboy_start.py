import pygame
class Farmboy_start(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.moving = False

        idle1 = pygame.image.load('graphics/warrior/idle/1.png').convert_alpha()
        idle2 = pygame.image.load('graphics/warrior/idle/2.png').convert_alpha()
        idle3 = pygame.image.load('graphics/warrior/idle/3.png').convert_alpha()
        idle4 = pygame.image.load('graphics/warrior/idle/4.png').convert_alpha()
        idle5 = pygame.image.load('graphics/warrior/idle/5.png').convert_alpha()
        self.idle = [idle1, idle2, idle3, idle4, idle5]
        self.frame_index = 0
        self.image = self.idle[self.frame_index]
        self.rect = self.image.get_rect(center=(300, 265))

    def idling(self):
        self.frame_index += 0.2
        if self.frame_index >= len(self.idle):
            self.frame_index = 0
        self.image = self.idle[int(self.frame_index)]

    def update(self):
        self.idling()