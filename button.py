import pygame
import pyautogui


class Button():
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.image_normal = pygame.Surface((width, height))
        self.image_normal.fill((200, 200, 200))

        self.image_hovered = pygame.Surface((width, height))
        self.image_hovered.fill((200, 200, 200))

        self.image = self.image_normal
        self.rect = self.image.get_rect()

        font_normal = pygame.font.SysFont(None, 25)
        font_hovered = pygame.font.SysFont(None, 30)
        text_image_normal = font_normal.render(text, True, (0, 0, 0))
        text_image_hovered = font_hovered.render(text, True, (50, 50, 50))
        text_rect = text_image_normal.get_rect(center=self.rect.center)

        self.image_normal.blit(text_image_normal, text_rect)
        self.image_hovered.blit(text_image_hovered, text_rect)

        self.rect.topleft = (x, y)
        self.hovered = False

    def update(self):
        if self.hovered:
            self.image = self.image_hovered
        else:
            self.image = self.image_normal

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                print('clicked:', self.text)
                mes = ''
                with open('rules.txt', encoding="utf-8") as inf:
                    for line in inf:
                        line = line.strip()
                        mes += line + '\n'
                pyautogui.alert(text=mes, title='Правила', button='OK')
