
# ===== IMPORTS ==================================================================================================== #

from os import system
from globalStuff import GB
from command import Command

# ===== CONSOLE MANAGER ==================================================================================================== #

class CM:

    play = False
    playbackSpeed = 2
    running = True
    addTarget = [False, -1, False]

    __USER = "    [USER] > "
    __ALERT = "   [ALERT] > "
    __ERROR = "   [ERROR] > "
    __MESSAGE = " [MESSAGE] > "
    __INFO = "    [INFO] > "

    def __play(self, args):
        CM.play = True

    def __pause(self, args):
        CM.play = False

    def __setspeed(self, args):
        try:
            inputSpeed = int(args[0])
            assert (0 < inputSpeed <= 60)
            CM.playbackSpeed = inputSpeed
        except (ValueError, IndexError):
            print(CM.__ERROR + 'Incorrect syntax. Try the "help" command for the correct syntax.')
        except AssertionError:
            print(CM.__ERROR + "You must enter an integer between 1 and 60 (included).")

    def __getspeed(self, args):
        print(CM.__INFO + "speed = " + str(CM.playbackSpeed))

    def __pushbutton(self, args):
        try:
            CM.addTarget[1] = int(args[0])
            if args[1] == "floor" or args[1] == "f":
                CM.addTarget[2] = False
            elif args[1] == "elevator" or args[1] == "e":
                CM.addTarget[2] = True
            else:
                raise SyntaxError
            assert (0 <= CM.addTarget[1] <= GB.NUM_FLOORS())
            CM.addTarget[0] = True
        except (ValueError, IndexError, SyntaxError):
            print(CM.__ERROR + 'Incorrect syntax. Try the "help" command for the correct syntax.')
        except AssertionError:
            print(CM.__ERROR + "For the <floor> you must enter an integer between 0 and " + str(
                GB.NUM_FLOORS() - 1) + " (included).")

    def __clear(self, args):
        system('cls')
        print()

    def __exit(self, args):
        print(CM.__MESSAGE + "Exiting... Bye!")
        CM.running = False

    __commands =\
    [
      # Command("name", "short", "action", "syntax", "description")
        Command("play", "pl", __play, "play|pl", "Starts the simulation of the elevator."),
        Command("pause", "ps", __pause, "pause|ps", "Stops the simulation of the elevator."),
        Command("getSpeed", "gs", __getspeed, "getSpeed|gs", "Shows you the current speed of the simulation."),
        Command("setSpeed", "ss", __setspeed, "setSpeed|ss <stepsPerSecond>", "Modifies the speed of the simulation."),
        Command("pushButton", "pb", __pushbutton, "pushButton|ps <floorNumber> <floor|elevator>", "Ads a new destination for the elevator."),
        Command("clear", "cl", __clear, "clear|cl", "Clears the screen from all previous commands."),
        Command("exit", "ex", __exit, "exit|ex", "Terminates the program.")
    ]

    @staticmethod
    def consoleManager():
        while CM.running:
            command = input(CM.__USER).lower().split()

            commandExists = False
            for c in CM.__commands:
                if command[0] == str(c.name).lower() or command[0] == str(c.short).lower():
                    commandExists = True
                    c.action(None, command[1:])
                    break

            if not commandExists:
                print(CM.__ALERT + 'The command entered does not exist. Try the "help" command for a list with all the commands and their syntax.')

# ===== ========== ==================================================================================================== #
