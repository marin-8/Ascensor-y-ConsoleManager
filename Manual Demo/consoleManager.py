
# ===== IMPORTS ==================================================================================================== #

from os import system

# ===== CONSOLE MANAGER ==================================================================================================== #

class CM:

    __commands = ("play", "pause",
                  "setplaybackspeed",
                  "nextstep", "nexttarget",
                  "addtarget",
                  "clear", "exit")

    __USER = "    [USER] > "
    __ALERT = "   [ALERT] > "
    __ERROR = "   [ERROR] > "
    __MESSAGE = " [MESSAGE] > "
    __INFO = "    [INFO] > "

    play = False
    playbackSpeed = 2
    running = True

    @staticmethod
    def consoleManager():
        while CM.running:
            command = input(CM.__USER).lower().split()

            if command[0] not in CM.__commands:
                print(CM.__ALERT + "The command entered does not exist. Try again.")
            else:
                if command[0] == "play":
                    CM.play = True
                elif command[0] == "pause":
                    CM.play = False
                elif command[0] == "setPlaybackSpeed".lower():
                    CM.playbackSpeed = int(command[1])
                elif command[0] == "clear":
                    system('cls')
                elif command[0] == "exit":
                    CM.running = False

# ===== ========== ==================================================================================================== #
