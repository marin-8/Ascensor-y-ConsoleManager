
# ===== IMPORTS ==================================================================================================== #

from os import system
from win32api import GetSystemMetrics

# ===== GLOBAL STUFF ==================================================================================================== #

class GlobalStuff:

    __SCREEN_WIDTH = GetSystemMetrics(0)
    __SCREEN_HEIGHT = GetSystemMetrics(1)

    __WINDOW_WIDTH = 180
    __WINDOW_HEIGHT = __SCREEN_HEIGHT - 40

    __FPS_BAR_HEIGHT = 30

    __MAX_FLOORS = int(-__FPS_BAR_HEIGHT/65+__SCREEN_HEIGHT/65-4/13)
    __NUM_FLOORS = -1

    # ================================================== #

    @staticmethod
    def SET_NUM_FLOORS():
        while True:
            try:
                inputFloors = int(input(
                    "    [USER] > " +
                    "Input the number of floors for the elevator (between 2 and " + str(GlobalStuff.__MAX_FLOORS) + " (included) for your vertical resolution): "
                ))
                assert(2 <= inputFloors <= GlobalStuff.__MAX_FLOORS)
                GlobalStuff.__NUM_FLOORS = inputFloors
                break
            except:
                system('cls')
                print("\n" + "   [ERROR] > " + "You must enter an integer between 2 and " + str(GlobalStuff.__MAX_FLOORS) + " (included).")

    # ================================================== #

    @staticmethod
    def SCREEN_WIDTH():
        return GlobalStuff.__SCREEN_WIDTH

    @staticmethod
    def SCREEN_HEIGHT():
        return GlobalStuff.__SCREEN_HEIGHT

    @staticmethod
    def WINDOW_WIDTH():
        return GlobalStuff.__WINDOW_WIDTH

    @staticmethod
    def WINDOW_HEIGHT():
        return GlobalStuff.__WINDOW_HEIGHT

    @staticmethod
    def FPS_BAR_HEIGHT():
        return GlobalStuff.__FPS_BAR_HEIGHT

    @staticmethod
    def NUM_FLOORS():
        return GlobalStuff.__NUM_FLOORS

# ===== ========== ==================================================================================================== #

