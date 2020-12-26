
# ===== IMPORTS ==================================================================================================== #

from globalStuff import GB

# ===== FLOORS ==================================================================================================== #

class Floors:

    __floor_height = (GB.WINDOW_HEIGHT()-GB.FPS_BAR_HEIGHT()-(GB.NUM_FLOORS()+1)*20) // GB.NUM_FLOORS()

    @staticmethod
    def Draw(pygame, SCREEN):
        for f in range(GB.NUM_FLOORS()):

            x = 20+40+20
            y = GB.FPS_BAR_HEIGHT()+20+f*(Floors.__floor_height+20)
            w = 100
            h = Floors.__floor_height
            t = 4

            pygame.draw.rect(SCREEN, (0,0,0), (x, y, w, t))
            pygame.draw.rect(SCREEN, (0,0,0), (x+w-t, y, t, h))
            pygame.draw.rect(SCREEN, (0,0,0), (x, y+h-t, w, t))
            pygame.draw.rect(SCREEN, (0,0,0), (x, y, t, h))

            font = pygame.font.SysFont("Consolas", 32)
            text = font.render(str(GB.NUM_FLOORS()-f), True, (0,0,0))
            text_rect = text.get_rect(center=(x+w/2, y+h/2+2))
            SCREEN.blit(text, text_rect)

# ===== ========== ==================================================================================================== #
