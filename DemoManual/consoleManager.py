
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
    echo = True

    __USER = "    [USER] > "
    __ALERT = "   [ALERT] > "
    __ERROR = "   [ERROR] > "
    __MESSAGE = " [MESSAGE] > "
    __INFO = "    [INFO] > "

    def __play(self, args):
        CM.play = True
        if CM.echo:
            print(CM.__INFO + "Resumed the simulation.")

    def __pause(self, args):
        CM.play = False
        if CM.echo:
            print(CM.__INFO + "Paused the simulation.")

    def __setspeed(self, args):
        try:
            inputSpeed = int(args[0])
            assert (0 < inputSpeed <= 60)
            CM.playbackSpeed = inputSpeed
            if CM.echo:
                print(CM.__INFO + "Modified the speed of the simulation to " + str(CM.playbackSpeed) + ".")
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
            if CM.echo:
                if CM.addTarget[2]: # elevator
                    print(CM.__INFO + "Pushed the button for the " + str(CM.addTarget[1]) + "th floor from inside the elevator.")
                else: # floor
                    print(CM.__INFO + "Called the elevator from the " + str(CM.addTarget[1]) + "th floor.")
        except (ValueError, IndexError, SyntaxError):
            print(CM.__ERROR + 'Incorrect syntax. Try the "help" command for the correct syntax.')
        except AssertionError:
            print(CM.__ERROR + "For the <floor> you must enter an integer between 0 and " + str(
                GB.NUM_FLOORS() - 1) + " (included).")

    def __echo(self, args):
        try:
            if args[0] == "true" or args[0] == "on" or args[0] == "t":
                CM.echo = True
                if CM.echo:
                    print(CM.__INFO + 'Activated the "echo" mode.')
            elif args[0] == "false" or args[0] == "off" or args[0] == "f":
                CM.echo = False
            else:
                print(CM.__ERROR + 'Incorrect syntax. Try the "help" command for the correct syntax.')
        except:
            print(CM.__ERROR + 'Incorrect syntax. Try the "help" command for the correct syntax.')

    def __clear(self, args):
        system('cls')
        print()

    def __exit(self, args):
        if CM.echo:
            print(CM.__MESSAGE + "Exiting... Bye!")
        CM.running = False

    __commands =\
    [
      # Command("name", "short", "action", "syntax", "description")
        Command("play", "pl", __play, "play|pl", "Starts the simulation of the elevator."),
        Command("pause", "ps", __pause, "pause|ps", "Stops the simulation of the elevator."),
        Command("getSpeed", "gs", __getspeed, "getSpeed|gs", "Shows you the current speed of the simulation."),
        Command("setSpeed", "ss", __setspeed, "setSpeed|ss <stepsPerSecond>", "Modifies the speed of the simulation."),
        Command("pushButton", "pb", __pushbutton, "pushButton|pb <floorNumber> <{floor|f}|{elevator|e}>", "Ads a new destination for the elevator."),
        Command("echo", "ec", __echo, "echo|ec <{true|t|on}|{false|f|off}>", "Enables or disables an info message about every command you execute successfully."),
        Command("clear", "cl", __clear, "clear|cl", "Clears the screen from all previous commands."),
        Command("exit", "ex", __exit, "exit|ex", "Terminates the program.")
    ]

    # __commands.sort(key=lambda c: c.name)

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
                if command[0] == "help":
                    print(CM.__INFO + "List of all the commands and their syntax:" + "\n")
                    for c in CM.__commands:
                        print(" -- " + c.syntax)
                        print("    " + "    " + c.description + "\n")
                else:
                    print(CM.__ALERT + 'The command entered does not exist. Try the "help" command for a list with all the commands and their syntax.')

# ===== ========== ==================================================================================================== #
