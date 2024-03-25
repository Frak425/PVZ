import pygame

from Plants.cherrybomb import Cherrybomb
from Plants.chomper import Chomper
from Plants.doomshroom import Doomshroom
from Plants.fumeshroom import Fumeshroom
from Plants.gravebuster import Gravebuster
from Plants.hypnoshroom import Hypnoshroom
from Plants.iceshroom import Iceshroom
from Plants.jalapeno import Jalapeno
from Plants.lilypad import Lilypad
from Plants.peashooter import Peashooter
from Plants.potatomine import Potatomine
from Plants.puffshroom import Puffshroom
from Plants.repeater import Repeater
from Plants.scardeyshroom import Scaredyshroom
from Plants.snowpea import Snowpea
from Plants.spikeweed import Spikeweed
from Plants.squash import Squash
from Plants.sunflower import Sunflower
from Plants.sunshroom import Sunshroom
from Plants.tallnut import Tallnut
from Plants.tanglekelp import Tanglekelp
from Plants.threepeater import Threepeater
from Plants.torchwood import Torchwood
from Plants.wallnut import wallnut

from Zombies.bobsled import Bobsled
from Zombies.buckethead import Buckethead
from Zombies.cone import Cone
from Zombies.dancer import Dancer
from Zombies.disco import Disco
from Zombies.dolphin import Dolphin
from Zombies.door import Door
from Zombies.ducky import Ducky
from Zombies.flag import Flag
from Zombies.football import Football
from Zombies.newspaper import Newspaper
from Zombies.pole import Pole
from Zombies.snorkel import Snorkel
from Zombies.zombie import Zombie
from Zombies.zomboni import Zomboni

#constants
frame_rate = 60
display_screen = ''

pygame.init()

screen = pygame.display.set_mode((1280, 720))

#pygame.display.set_caption('')

#icon = pygame.image.load('')
#pygame.display.set_icon(icon)

clock = pygame.time.Clock()

def find_button(x, y):
    if x < 640 and y < 360:
        pass
    elif x >= 640 and y >= 360:
        pass
    elif x >= 640 and y < 360:
        pass
    else:
        pass

running = True
while running:
    clock.tick(frame_rate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x = event.pos[0]
            y = event.pos[1]
            location = find_button(x, y)
            if location == "nothing important":
                continue
            elif location == "" and display_screen == "":
                pass
    tall_nut = Tallnut("body_normal", 100, 100, screen)
    tall_nut.update_position(100, 100)
    tall_nut.draw()
    tall_nut1 = Tallnut("body_sad", 200, 100, screen)
    tall_nut1.update_position(300, 100)
    tall_nut1.draw()
    tall_nut2 = Tallnut("body_crying", 300, 100, screen)
    tall_nut2.update_position(500, 100)
    tall_nut2.draw()



    pygame.display.flip()

pygame.quit()



