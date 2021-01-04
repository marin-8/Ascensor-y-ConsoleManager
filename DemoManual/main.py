
# ===== IMPORTS ==================================================================================================== #

import os
import threading
from os import system

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

from globalStuff import GlobalStuff
from control import Control
from consoleManager import ConsoleManager

from elevator import Elevator
from floors import Floors
from BackEnd.elevator_BackEnd import Elevator_BackEnd

# ===== MAIN ==================================================================================================== #

if __name__ == "__main__":

# ===== SCREEN POSITION ==================================================================================================== #

    screen_position_x = GlobalStuff.SCREEN_WIDTH() - GlobalStuff.WINDOW_WIDTH()
    screen_position_y = 0

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_position_x, screen_position_y)

# ===== PYGAME INIT ==================================================================================================== #

    pygame.init()

    SCREEN = pygame.display.set_mode((GlobalStuff.WINDOW_WIDTH(), GlobalStuff.WINDOW_HEIGHT()), pygame.NOFRAME)

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Consolas", 16)

# ===== CONSOLE SETUP ==================================================================================================== #

    system('mode con: cols=147 lines=49')

# ===== NUMBER OF FLOORS INPUT ==================================================================================================== #

    print()

    GlobalStuff.SET_NUM_FLOORS()

    system('cls')
    print()

# ===== ELEVATOR INIT ==================================================================================================== #

    elevator = Elevator_BackEnd(GlobalStuff.NUM_FLOORS())

# ===== CONSOLE MANAGER INIT ==================================================================================================== #

    threading.Thread(target=ConsoleManager.consoleManager, daemon=True).start()

# ===== LOOP ==================================================================================================== #

    while Control.running:

        SCREEN.fill((192, 192, 192))
        pygame.draw.rect(SCREEN, (64, 64, 64), (0, 0, GlobalStuff.WINDOW_WIDTH(), GlobalStuff.FPS_BAR_HEIGHT()))
        SCREEN.blit(font.render("Speed: " + str(int(clock.get_fps())), True, (192, 192, 192)), (8, 8))

        clock.tick(Control.playbackSpeed)

        pygame.event.get()

        if Control.play:
            elevator.next_step()

        if Control.addTarget[0]:
            Control.addTarget[0] = False
            elevator.add_target(Control.addTarget[1], Control.addTarget[2])

        Elevator.Draw(pygame, SCREEN, elevator.cur_floor, elevator.doorsOpen)
        Floors.Draw(pygame, SCREEN, elevator.floor_buttons, elevator.elevator_buttons)

        pygame.display.update()

# ===== ========== ==================================================================================================== #
