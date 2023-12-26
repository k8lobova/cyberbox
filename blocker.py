import pygame


class Blocker(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        super(Blocker, self).__init__()
        self.screen = screen
        self.blocker = pygame.image.load('images/blocker.png')
        self.rect = self.blocker.get_rect()
        self.rect.centerx = x
        self.rect.top = y

    def draw(self):
        self.screen.blit(self.blocker, self.rect)
