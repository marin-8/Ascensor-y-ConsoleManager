
# ===== IMPORTS ==================================================================================================== #

import os
import pygame
import threading
from os import system

from globalStuff import GB
from control import Control
from consoleManager import ConsoleManager

#from tests import Tests
from elevator import Elevator
from floors import Floors
from BackEnd.elevator_BackEnd import Elevator_BackEnd

# ===== MAIN ==================================================================================================== #

if __name__ == "__main__":

# ===== SCREEN POSITION ==================================================================================================== #

    screen_position_x = GB.SCREEN_WIDTH() - GB.WINDOW_WIDTH()
    screen_position_y = 0

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_position_x, screen_position_y)

# ===== PYGAME INIT ==================================================================================================== #

    pygame.init()

    SCREEN = pygame.display.set_mode((GB.WINDOW_WIDTH(), GB.WINDOW_HEIGHT()), pygame.NOFRAME)

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Consolas", 16)

    system('cls')
    print()

# ===== NUMBER OF FLOORS INPUT ==================================================================================================== #

    GB.SET_NUM_FLOORS()

# ===== ELEVATOR INIT ==================================================================================================== #

    elevator = Elevator_BackEnd(GB.NUM_FLOORS())

# ===== LOOP ==================================================================================================== #

    threading.Thread(target=ConsoleManager.consoleManager, args=(Control.running,), daemon=True).start()

    while Control.running:

        SCREEN.fill((192, 192, 192))
        pygame.draw.rect(SCREEN, (64, 64, 64), (0, 0, GB.WINDOW_WIDTH(), GB.FPS_BAR_HEIGHT()))
        SCREEN.blit(font.render("Speed: " + str(int(clock.get_fps())), True, (192, 192, 192)), (8, 8))

        DT = clock.tick(Control.playbackSpeed)

        pygame.event.get()

        #for event in pygame.event.get():
        #    if event.type == pygame.KEYDOWN:
        #        if event.key == pygame.K_ESCAPE:
        #            CM.running = False

        if Control.play:
            elevator.next_step()

        if Control.addTarget[0]:
            Control.addTarget[0] = False
            elevator.add_target(Control.addTarget[1], Control.addTarget[2])

        #Tests.tests(pygame, SCREEN, DT)
        Elevator.Draw(pygame, SCREEN, elevator.cur_floor, elevator.doorsOpen)
        Floors.Draw(pygame, SCREEN, elevator.floor_buttons, elevator.elevator_buttons)

        pygame.display.update()

# ===== ========== ==================================================================================================== #
