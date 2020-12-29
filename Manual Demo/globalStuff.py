
# ===== IMPORTS ==================================================================================================== #

from win32api import GetSystemMetrics

# ===== GLOBAL STUFF ==================================================================================================== #

class GB:

    __SCREEN_WIDTH = GetSystemMetrics(0)
    __SCREEN_HEIGHT = GetSystemMetrics(1)

    __WINDOW_WIDTH = 180
    __WINDOW_HEIGHT = __SCREEN_HEIGHT - 40

    __FPS_BAR_HEIGHT = 37

    __NUM_FLOORS = -1

    # ================================================== #

    @staticmethod
    def SET_NUM_FLOORS():
        GB.__NUM_FLOORS = int(input(
            "    [USER] > " +
            "Input the number of floors for the elevator: "
        ))

    # ================================================== #

    @staticmethod
    def SCREEN_WIDTH():
        return GB.__SCREEN_WIDTH

    @staticmethod
    def SCREEN_HEIGHT():
        return GB.__SCREEN_HEIGHT

    @staticmethod
    def WINDOW_WIDTH():
        return GB.__WINDOW_WIDTH

    @staticmethod
    def WINDOW_HEIGHT():
        return GB.__WINDOW_HEIGHT

    @staticmethod
    def FPS_BAR_HEIGHT():
        return GB.__FPS_BAR_HEIGHT

    @staticmethod
    def NUM_FLOORS():
        return GB.__NUM_FLOORS

# ===== ========== ==================================================================================================== #
