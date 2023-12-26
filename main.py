import pygame, controls

from player import Player
from pygame.sprite import Group
from button import Button


def run(lvl):
    pygame.init()
    screen = pygame.display.set_mode((750, 550))
    frame = pygame.Rect((50, 50, 650, 450))
    screen_rect = screen.get_rect()
    pygame.display.set_caption("CyberBox")
    bg_color = (200, 200, 200)
    FPS = 10
    player = Player(screen, frame)

    objects = Group()
    level = lvl

    font1 = pygame.font.SysFont(None, 30)
    font2 = pygame.font.SysFont(None, 25)
    text1 = font1.render('Level ' + str(lvl), True, (0, 0, 0))
    text2 = font2.render('Arrows to move.', True, (0, 0, 0))
    text3 = font2.render('R to retry this level.', True, (0, 0, 0))
    button = Button('Rules', 38, 505, 70, 30)

    controls.create_objects(screen, objects, level)
    clock = pygame.time.Clock()

    while True:
        button.update()
        cond = controls.events(player, button)
        if cond != 0:
            if cond == 1:
                level += 1
            run(level)
        player.update_player()

        controls.collide_blocks(objects, player, frame)

        controls.update_screen(frame, bg_color, screen, player, objects, text1, text2, text3, button)

        clock.tick(FPS)


run(1)
