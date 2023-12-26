import pygame


class Slider(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        super(Slider, self).__init__()
        self.screen = screen
        self.slider = pygame.image.load('images/slider_lurd.png')
        self.rect = self.slider.get_rect()
        self.rect.centerx = x
        self.rect.top = y

    def draw(self):
        self.screen.blit(self.slider, self.rect)
