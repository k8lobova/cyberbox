import pygame


class Player():
    def __init__(self, screen, frame):

        self.screen = screen
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.screen_rect = frame
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = self.mleft = self.mup = self.mdown = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_player(self):
        end_gran_right = self.screen_rect.right / 2 + self.screen_rect.left + 5
        end_gran_left = self.screen_rect.right / 2 - 5
        moving = self.rect.width

        if self.mup and self.rect.right < end_gran_right and self.rect.left > end_gran_left:
            self.rect.bottom -= moving

        elif self.mright and self.rect.right < self.screen_rect.right and self.rect.top > self.screen_rect.top - 1:
            self.rect.centerx += moving
        elif self.mleft and self.rect.left > self.screen_rect.left and self.rect.top > self.screen_rect.top - 1:
            self.rect.centerx -= moving
        elif self.mup and self.rect.top > self.screen_rect.top:
            self.rect.bottom -= moving
        elif self.mdown and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += moving
