import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, shoot_right):
        super().__init__()
        laser1 = pygame.image.load('graphics/laser/1.png').convert_alpha()
        laser2 = pygame.image.load('graphics/laser/2.png').convert_alpha()
        laser3 = pygame.image.load('graphics/laser/3.png').convert_alpha()
        laser4 = pygame.image.load('graphics/laser/4.png').convert_alpha()
        laser5 = pygame.image.load('graphics/laser/5.png').convert_alpha()
        self.laser = [laser1, laser2, laser3, laser4, laser5]
        self.frame_index = 0

        self.image = self.laser[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.speed = -10
        self.shoot_right = shoot_right

    def laser_animation(self):
        self.frame_index += 0.5
        if self.frame_index >= len(self.laser):
            self.frame_index = 0
        self.image = self.laser[int(self.frame_index)]

    def destroy(self):
        if self.rect.x < -10 or self.rect.x > 610 or self.rect.y < -10 or self.rect.y > 410:
            self.kill()

    def update(self):
        if self.shoot_right:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        self.laser_animation()
        self.destroy()