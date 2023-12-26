from slider import Slider
from slider_ud import Slider_ud
from slider_lr import Slider_lr
from blocker import Blocker


def level(screen, objects):
    slider = Slider(screen, 575, 250)
    slider2 = Slider(screen, 125, 100)
    slider3 = Slider(screen, 425, 400)
    blocker = Blocker(screen, 225, 200)
    slider_lr = Slider_lr(screen, 575, 100)
    slider_ud = Slider_ud(screen, 175, 400)
    slider_ud2 = Slider_ud(screen, 125, 400)

    slider_lr2 = Slider_lr(screen, 575, 400)
    slider_lr3 = Slider_lr(screen, 525, 400)
    slider_ud3 = Slider_ud(screen, 425, 200)
    slider_ud4 = Slider_ud(screen, 425, 250)
    objects.add(slider, slider2, blocker, slider_lr, slider_ud, slider_ud2)
    objects.add(slider_lr2, slider_lr3, slider_ud3, slider_ud4,slider3)

    return objects
