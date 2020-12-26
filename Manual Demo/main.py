
# ===== IMPORTS ==================================================================================================== #

import os
import pygame
import threading

from globalStuff import GB
from consoleManager import CM

from tests import Tests
from floors import Floors

# ===== SCREEN POSITION ==================================================================================================== #

screen_position_x = GB.SCREEN_WIDTH() - GB.WINDOW_WIDTH()
screen_position_y = 0

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_position_x, screen_position_y)

# ===== PYGAME INIT ==================================================================================================== #

pygame.init()

SCREEN = pygame.display.set_mode((GB.WINDOW_WIDTH(), GB.WINDOW_HEIGHT()), pygame.NOFRAME)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 24)

# ===== LOOP ==================================================================================================== #

RUNNING = True
while RUNNING:

    SCREEN.fill((192, 192, 192))
    pygame.draw.rect(SCREEN, (64, 64, 64), (0, 0, GB.WINDOW_WIDTH(), GB.FPS_BAR_HEIGHT()))
    SCREEN.blit(font.render("FPS: " + str(int(clock.get_fps())), True, (192, 192, 192)), (8, 8))

    DT = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False
            if event.key == pygame.K_0:
                t = threading.Thread(target=CM.testThread)
                t.start()

    #Tests.tests(pygame, SCREEN, DT)
    Floors.Draw(pygame, SCREEN)

    pygame.display.update()

# ===== ========== ==================================================================================================== #
