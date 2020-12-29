
# ===== IMPORTS ==================================================================================================== #

from globalStuff import GB

# ===== ELEVATOR ==================================================================================================== #

class Elevator:

    @staticmethod
    def Draw(pygame, SCREEN, floor, doorsOpen):
        elevator_height = (GB.WINDOW_HEIGHT() - GB.FPS_BAR_HEIGHT() - (GB.NUM_FLOORS() + 1) * 20) // GB.NUM_FLOORS()

        x = 20+20+20
        y = GB.FPS_BAR_HEIGHT()+20+(GB.NUM_FLOORS()-floor-1)*(elevator_height+20)
        w = 50
        h = elevator_height

        pygame.draw.rect(SCREEN, (0,128,255), (x, y, w-25*int(doorsOpen), h))
        pygame.draw.rect(SCREEN, (0,128,255), (x+w+25*int(doorsOpen), y, w-25*int(doorsOpen), h))

# ===== ========== ==================================================================================================== #
