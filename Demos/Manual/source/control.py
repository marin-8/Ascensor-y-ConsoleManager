
# ===== IMPORTS ==================================================================================================== #

from global_stuff import GlobalStuff
from Console_Manager.console_manager import *

# ===== COMMAND CONTROL ==================================================================================================== #

class Control:

    play = False
    playbackSpeed = 2
    running = True
    addTarget = [False, -1, False]

    # ================================================== #

    def __play(args):
        Control.play = True

    def __pause(args):
        Control.play = False

    def __setspeed(args):
        try:
            inputSpeed = int(args[0])
            assert (0 < inputSpeed <= 60)
            Control.playbackSpeed = inputSpeed
        except (ValueError, IndexError):
            ConsoleManager.LOG_ERROR('Incorrect syntax. Try the "help" command for the correct syntax.')
        except AssertionError:
            ConsoleManager.LOG_ERROR("You must enter an integer between 1 and 60 (included).")

    def __getspeed(args):
        ConsoleManager.LOG_INFO("speed = " + str(Control.playbackSpeed))

    def __pushbutton(args):
        try:
            Control.addTarget[1] = int(args[0])
            if args[1] == "floor" or args[1] == "f":
                Control.addTarget[2] = False
            elif args[1] == "elevator" or args[1] == "e":
                Control.addTarget[2] = True
            else:
                raise SyntaxError
            assert (0 <= Control.addTarget[1] <= GlobalStuff.NUM_FLOORS())
            Control.addTarget[0] = True
        except (ValueError, IndexError, SyntaxError):
            ConsoleManager.LOG_ERROR('Incorrect syntax. Try the "help" command for the correct syntax.')
        except AssertionError:
            ConsoleManager.LOG_ERROR("For the <floorNumber> you must enter an integer between 0 and " + str(GlobalStuff.NUM_FLOORS() - 1) + " (included).")

    def __exit(args):
        Control.running = False

    # ================================================== #

    ConsoleManager.addCommand(Command("PLAY", "PL", __play, "PLAY|PL", "Starts the simulation of the elevator"))
    ConsoleManager.addCommand(Command("PAUSE", "PS", __pause, "PAUSE|PS", "Stops the simulation of the elevator"))
    ConsoleManager.addCommand(Command("GETSPEED", "GS", __getspeed, "GETSPEED|GS", "Shows you the current speed of the simulation"))
    ConsoleManager.addCommand(Command("SETSPEED", "SS", __setspeed, "SETSPEED|SS <stepsPerSecond>", "Modifies the speed of the simulation"))
    ConsoleManager.addCommand(Command("PUSHBUTTON", "PB", __pushbutton, "PUSHBUTTON|PB <floorNumber> <{FLOOR|F}|{ELEVATOR|E}>", "Ads a new destination for the elevator"))
    ConsoleManager.addCommand(Command("EXIT", "EX", __exit, "EXIT|EX", "Terminates the program"))

    # ================================================== #

    def __testmsg(args):
        ConsoleManager.LOG_MESSAGE("This is just a test message because at the moment there aren't any messages in the program.")

    ConsoleManager.addCommand(Command("TESTMSG", "TM", __testmsg, "TESTMSG|TM", "Displays a test message to show the color of the command"))

# ===== ========== ==================================================================================================== #
