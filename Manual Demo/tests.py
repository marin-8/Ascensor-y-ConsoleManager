
# ===== TESTS ==================================================================================================== #

class Tests:

    speed = 1000 # px/s

    i = 0
    d = False

    @staticmethod
    def tests(pygame, SCREEN, DT):
        if Tests.d:
            Tests.i -= Tests.speed * DT / 1000
            pygame.draw.rect(SCREEN, (255, 0, 255), (20, 37 + 20 + Tests.i, 100, 100))
            if Tests.i < 1:
                Tests.d = False
        else:
            Tests.i += Tests.speed * DT / 1000
            pygame.draw.rect(SCREEN, (255, 0, 255), (20, 37 + 20 + Tests.i, 100, 100))
            if Tests.i > 999:
                Tests.d = True

# ===== ========== ==================================================================================================== #
