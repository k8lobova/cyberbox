import pygame
import sys
import importlib
from slider import Slider
from slider_lr import Slider_lr
from slider_ud import Slider_ud


def events(player, button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif player.rect.top <= 0:
            print("next level")
            return 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print("restart")
                return 2
            # вправо
            if event.key == pygame.K_RIGHT:
                player.mright = True
            # влево
            elif event.key == pygame.K_LEFT:
                player.mleft = True
            # вниз
            elif event.key == pygame.K_DOWN:
                player.mdown = True
            # вверх
            elif event.key == pygame.K_UP:
                player.mup = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP]:
                player.mright = player.mleft = player.mdown = player.mup = False
        button.handle_event(event)
    return 0


def update_screen(frame, bg_color, screen, player, objects, text1, text2, text3, button):
    screen.fill(bg_color)
    pygame.draw.rect(screen, (0, 0, 0), frame, 2)
    pygame.draw.line(screen, (200, 200, 200), (345, 50), (405, 50), 2)

    for ob in objects:
        ob.draw()

    # blockSize = 50  # Set the size of the grid block
    # for x in range(750):
    #     for y in range(550):
    #         rect = pygame.Rect(x * blockSize, y * blockSize,
    #                            blockSize, blockSize)
    #         pygame.draw.rect(screen, (0, 255, 0), rect, 1)

    button.draw(screen)

    draw_text(screen, text1, 83, 30)
    draw_text(screen, text2, 623, 510)
    draw_text(screen, text3, 623, 535)

    player.output()
    pygame.display.flip()


def create_objects(screen, objects, num):
    n = str(num)
    s = "levels.level" + n
    my_module = importlib.import_module(s).level
    my_module(screen, objects)
    num += 1


def collide_blocks(objects, player, frame):
    ob_list = []
    for ob in objects:
        ob_list.append(ob.rect)

    for ob in objects:
        pl = player.rect
        o = ob.rect
        collide = pygame.Rect.colliderect(pl, o)
        horizontal = get_way(ob, Slider_lr)
        vertical = get_way(ob, Slider_ud)
        # вправо
        if collide and player.mright:
            if horizontal and frame.right - pl.right > 0:
                first = ob_list.index(o)
                pygame.Rect.move_ip(o, o.width, 0)
                list_move_ob = []
                new_list = try_to_punch(first, o, objects, ob_list, o.width, 0, pl,
                                        frame.right - pl.right, Slider_lr, list_move_ob)
                max = 0
                for new in new_list:
                    max = new.right
                if max >= frame.right + o.width:
                    check_border(new_list, o, pl, -o.width, 0)
            else:
                pygame.Rect.move_ip(pl, -pl.width, 0)
        # влево
        if collide and player.mleft:
            if horizontal and pl.left - frame.left > 0:
                first = ob_list.index(o)
                pygame.Rect.move_ip(o, -o.width, 0)
                list_move_ob = []
                new_list = try_to_punch(first, o, objects, ob_list, -o.width, 0, pl,
                                        pl.left - frame.left, Slider_lr, list_move_ob)
                max = o.width
                for new in new_list:
                    max = new.left
                if max <= frame.left - o.width:
                    check_border(new_list, o, pl, o.width, 0)
            else:
                pygame.Rect.move_ip(pl, pl.width, 0)
        # вверх
        if collide and player.mup:
            if vertical and pl.top - frame.top > 0:
                first = ob_list.index(o)
                pygame.Rect.move_ip(o, 0, -o.height)
                list_move_ob = []
                new_list = try_to_punch(first, o, objects, ob_list, 0, -o.height, pl,
                                        pl.top - frame.top, Slider_ud, list_move_ob)
                max = o.height
                for new in new_list:
                    max = new.top
                if max <= frame.top - o.height:
                    check_border(new_list, o, pl, 0, o.height)
            else:
                pygame.Rect.move_ip(pl, 0, pl.height)
        # вниз
        if collide and player.mdown:
            if vertical and frame.bottom - pl.bottom > 0:
                first = ob_list.index(o)
                pygame.Rect.move_ip(o, 0, o.height)
                list_move_ob = []
                new_list = try_to_punch(first, o, objects, ob_list, 0, o.height, pl,
                                        frame.bottom - pl.bottom, Slider_ud, list_move_ob)
                max = 0
                for new in new_list:
                    max = new.bottom
                if max >= frame.bottom + o.height:
                    check_border(new_list, o, pl, 0, -o.height)
            else:
                pygame.Rect.move_ip(pl, 0, -pl.height)


def get_object(objects, n):
    i = 0
    for ob in objects:
        if i == n:
            return ob
        else:
            i += 1


def get_way(ob, Slider2):
    return isinstance(ob, Slider) or isinstance(ob, Slider2)


def check_border(new_list, o, pl, x, y):
    for i in range(len(new_list)):
        pygame.Rect.move_ip(new_list[i], x, y)
    pygame.Rect.move_ip(o, x, y)
    pygame.Rect.move_ip(pl, x, y)


def try_to_punch(first, o, objects, ob_list, x, y, pl, frame, type, list_move_ob):
    collide2 = pygame.Rect.collidelistall(o, ob_list)
    if len(collide2) > 1:
        if collide2[0] != first:
            ob_move = ob_list[collide2[0]]
            ob_dont = ob_list[collide2[1]]
            first = collide2[0]
        elif collide2[1] != first:
            ob_move = ob_list[collide2[1]]
            ob_dont = ob_list[collide2[0]]
            first = collide2[1]

    if len(collide2) > 1 and frame > 0:
        if get_way(get_object(objects, collide2[0]), type) and get_way(get_object(objects, collide2[1]), type):
            if pygame.Rect.contains(ob_list[collide2[0]], ob_list[collide2[1]]):
                pygame.Rect.move_ip(ob_move, x, y)
                list_move_ob.append(ob_move)
                try_to_punch(first, ob_move, objects, ob_list, x, y, pl, frame, type, list_move_ob)
        else:
            for i in range(len(list_move_ob)):
                pygame.Rect.move_ip(list_move_ob[i], -x, -y)
            pygame.Rect.move_ip(ob_dont, -x, -y)
            pygame.Rect.move_ip(pl, -x, -y)

    return list_move_ob


def draw_text(screen, text, x, y):
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def end_game():
    pygame.font.init()
    pygame.font.get_init()
    display_surface = pygame.display.set_mode((752, 552))

    font = pygame.font.SysFont(None, 48)
    text = font.render('Вы прошли все уровни! Поздравляем!!!', True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (375, 275)

    while True:
        display_surface.fill((200, 200, 200))
        display_surface.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
