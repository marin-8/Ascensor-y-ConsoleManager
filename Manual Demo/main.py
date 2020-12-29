
# ===== IMPORTS ==================================================================================================== #

import os
import pygame
import threading

from globalStuff import GB
from consoleManager import CM

from tests import Tests
from elevator import Elevator
from floors import Floors
from Ascensor.BackEnd.elevator_BackEnd import Elevator_BackEnd

# ===== SCREEN POSITION ==================================================================================================== #

screen_position_x = GB.SCREEN_WIDTH() - GB.WINDOW_WIDTH()
screen_position_y = 0

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_position_x, screen_position_y)

# ===== PYGAME INIT ==================================================================================================== #

pygame.init()

SCREEN = pygame.display.set_mode((GB.WINDOW_WIDTH(), GB.WINDOW_HEIGHT()), pygame.NOFRAME)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 24)

# ===== ELEVATOR INIT ==================================================================================================== #

elevator = Elevator_BackEnd(GB.NUM_FLOORS())

elevator.add_target(7)
elevator.add_target(5)
elevator.add_target(1)

# ===== LOOP ==================================================================================================== #

RUNNING = True
while RUNNING:

    SCREEN.fill((192, 192, 192))
    pygame.draw.rect(SCREEN, (64, 64, 64), (0, 0, GB.WINDOW_WIDTH(), GB.FPS_BAR_HEIGHT()))
    SCREEN.blit(font.render("FPS: " + str(int(clock.get_fps())), True, (192, 192, 192)), (8, 8))

    DT = clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False
            if event.key == pygame.K_0:
                threading.Thread(target=CM.testThread).start()

    elevator.next_instruction()

    #Tests.tests(pygame, SCREEN, DT)
    Elevator.Draw(pygame, SCREEN, elevator.cur_floor, elevator.doorsOpen)
    Floors.Draw(pygame, SCREEN, elevator.floor_buttons, elevator.elevator_buttons)

    pygame.display.update()

# ===== ========== ==================================================================================================== #
