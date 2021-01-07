
# ===== IMPORTS ==================================================================================================== #

from global_stuff import GlobalStuff

# ===== ELEVATOR ==================================================================================================== #

class Elevator:

    @staticmethod
    def Draw(pygame, SCREEN, floor, doorsOpen):
        elevator_height = (GlobalStuff.WINDOW_HEIGHT() - GlobalStuff.FPS_BAR_HEIGHT() - (GlobalStuff.NUM_FLOORS() + 1) * 20) // GlobalStuff.NUM_FLOORS()

        x = 20+20+20
        y = GlobalStuff.FPS_BAR_HEIGHT() + 20 + (GlobalStuff.NUM_FLOORS() - floor - 1) * (elevator_height + 20)
        w = 50
        h = elevator_height

        pygame.draw.rect(SCREEN, (0,128,255), (x, y, w-25*int(doorsOpen), h))
        pygame.draw.rect(SCREEN, (0,128,255), (x+w+25*int(doorsOpen), y, w-25*int(doorsOpen), h))

# ===== ========== ==================================================================================================== #
