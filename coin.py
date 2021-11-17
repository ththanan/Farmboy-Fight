import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        coin1 = pygame.image.load('graphics/coin/1.png').convert_alpha()
        coin2 = pygame.image.load('graphics/coin/2.png').convert_alpha()
        self.coin = [coin1, coin2]
        self.frame_index = 0
        self.image = self.coin[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        self.coin_stay_time = 500

    def coin_animation(self):
        self.frame_index += 0.08
        if self.frame_index >= len(self.coin):
            self.frame_index = 0
        self.image = self.coin[int(self.frame_index)]

    def coin_delete(self):
        self.coin_stay_time -= 1
        if self.coin_stay_time<= 0:
            self.kill()
            self.coin_stay_time = 500

    def update(self):
        self.coin_animation()
        self.coin_delete()