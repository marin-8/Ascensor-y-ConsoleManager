
# ===== IMPORTS ==================================================================================================== #

from os import system
from globalStuff import GB

# ===== CONSOLE MANAGER ==================================================================================================== #

class CM:

    __commands = ("play", "pause",
                  "setspeed", "getspeed",
                  #"nextstep", #"nexttarget",
                  "pushbutton",
                  "help", "clear", "exit")

    __USER = "    [USER] > "
    __ALERT = "   [ALERT] > "
    __ERROR = "   [ERROR] > "
    __MESSAGE = " [MESSAGE] > "
    __INFO = "    [INFO] > "

    play = False
    playbackSpeed = 2
    running = True
    addTarget = [False, -1, False]

    @staticmethod
    def consoleManager():
        while CM.running:
            command = input(CM.__USER).lower().split()

            if command[0] not in CM.__commands:
                print(CM.__ALERT + 'The command entered does not exist. Try the "help" command for a list with all the commands and their syntax.')
            else:


                if command[0] == "play":
                    CM.play = True


                elif command[0] == "pause":
                    CM.play = False


                elif command[0] == "setSpeed".lower():
                    try:
                        inputSpeed = int(command[1])
                        assert(0 < inputSpeed <= 60)
                        CM.playbackSpeed = inputSpeed
                    except (ValueError, IndexError):
                        print(CM.__ERROR + 'Incorrect syntax. Try the "help" command for the correct syntax.')
                    except AssertionError:
                        print(CM.__ERROR + "You must enter an integer between 1 and 60 (included).")


                elif command[0] == "getSpeed".lower():
                    print(CM.__INFO + "speed = " + str(CM.playbackSpeed))


                elif command[0] == "pushButton".lower():
                    try:
                        CM.addTarget[1] = int(command[1])
                        if command[2] == "floor":
                            CM.addTarget[2] = False
                        elif command[2] == "elevator":
                            CM.addTarget[2] = True
                        else:
                            raise SyntaxError
                        assert(0 <= CM.addTarget[1] <= GB.NUM_FLOORS())
                        CM.addTarget[0] = True
                    except (ValueError, IndexError, SyntaxError):
                        print(CM.__ERROR + 'Incorrect syntax. Try the "help" command for the correct syntax.')
                    except AssertionError:
                        print(CM.__ERROR + "For the <floor> you must enter an integer between 0 and " + str(GB.NUM_FLOORS()-1) + " (included).")


                elif command[0] == "help":
                    print(CM.__INFO + "List of all the commands and their syntax:")
                    print()
                    print(" -- " + "play")
                    print("    " + "    " + "Starts the simulation of the elevator.")
                    print(" -- " + "pause")
                    print("    " + "    " + "Stops the simulation of the elevator.")
                    print(" -- " + "setSpeed <stepsPerSecond>")
                    print("    " + "    " + "Modifies the speed of the simulation.")
                    print(" -- " + "getSpeed")
                    print("    " + "    " + "Shows you the current speed of the simulation.")
                    print(" -- " + "pushButton <floorNumber> <floor|elevator>")
                    print("    " + "    " + "Ads a new destination for the elevator.")
                    print(" -- " + "help")
                    print("    " + "    " + 'Try the "help" command for the syntax of this command (meta).')
                    print(" -- " + "clear")
                    print("    " + "    " + "Clears the screen from all previous commands.")
                    print(" -- " + "exit")
                    print("    " + "    " + "Terminates the program.")
                    print()


                elif command[0] == "clear":
                    system('cls')
                    print()


                elif command[0] == "exit":
                    print(CM.__MESSAGE + "Exiting... Bye!")
                    CM.running = False


# ===== ========== ==================================================================================================== #
