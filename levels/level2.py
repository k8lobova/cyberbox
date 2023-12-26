from slider import Slider
from slider_ud import Slider_ud
from slider_lr import Slider_lr
from blocker import Blocker


def level(screen, objects):
    blocker = Blocker(screen, 225, 200)
    blocker2 = Blocker(screen, 225, 300)
    blocker3 = Blocker(screen, 325, 200)
    blocker4 = Blocker(screen, 325, 300)
    blocker5 = Blocker(screen, 425, 200)
    blocker6 = Blocker(screen, 425, 300)
    blocker7 = Blocker(screen, 525, 200)
    blocker8 = Blocker(screen, 525, 300)
    objects.add(blocker, blocker2, blocker3, blocker4, blocker5, blocker6, blocker7, blocker8)

    slider_lr = Slider_lr(screen, 375, 50)
    slider_lr2 = Slider_lr(screen, 375, 100)
    slider_lr3 = Slider_lr(screen, 375, 150)
    objects.add(slider_lr, slider_lr2, slider_lr3)

    slider_ud = Slider_ud(screen, 175, 200)
    slider_ud2 = Slider_ud(screen, 125, 200)
    slider_ud3 = Slider_ud(screen, 75, 200)
    slider_ud4 = Slider_ud(screen, 575, 200)
    slider_ud5 = Slider_ud(screen, 625, 200)
    slider_ud6 = Slider_ud(screen, 675, 200)
    objects.add(slider_ud, slider_ud2, slider_ud3, slider_ud4, slider_ud5, slider_ud6)

    slider = Slider(screen, 275, 250)
    slider2 = Slider(screen, 375, 250)
    slider3 = Slider(screen, 475, 250)
    objects.add(slider, slider2, slider3)

    return objects
