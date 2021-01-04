
# ===== IMPORTS ==================================================================================================== #

from os import system
from colorama import Fore, Style
from terminaltables import SingleTable

# ===== COMMAND ==================================================================================================== #

class Command:

    def __init__(self, name, short, action, syntax, description):
        self.__name = name
        self.__short = short
        self.__action = action
        self.__syntax = syntax
        self.__description = description

    # ================================================== #

    def execute(self, arguments):
        self.__action(arguments)

    # ================================================== #

    @property
    def name(self):
        return self.__name

    @property
    def short(self):
        return self.__short

    @property
    def syntax(self):
        return self.__syntax

    @property
    def description(self):
        return self.__description

# ===== CONSOLE MANAGER ==================================================================================================== #

class ConsoleManager:

    __USER = "    [USER] > "
    __ALERT = "   [ALERT] > "
    __ERROR = "   [ERROR] > "
    __MESSAGE = " [MESSAGE] > "
    __INFO = "    [INFO] > "

    __commands = []

    # ================================================== #

    def __help(args):
        ConsoleManager.LOG_INFO("List of all the commands and their syntax:")
        tableData = [[Fore.GREEN + "Command" + Fore.CYAN, Fore.GREEN + "Description" + Fore.CYAN, Fore.GREEN + "Syntax" + Fore.CYAN]]
        for c in ConsoleManager.__commands:
            tableRow = [c.name, c.description, c.syntax]
            tableData.append(tableRow)
        table = SingleTable(tableData)
        table.inner_row_border = True
        print(Fore.CYAN + " " + str(table.table).replace("\n", "\n ") + Fore.RESET)

    def __clear(args):
        system('cls')
        print()

    # ================================================== #

    __commands.append(Command("CLEAR", "CL", __clear, "CLEAR|CL", "Clears the screen from all previous commands"))
    __commands.append(Command("HELP", "HL", __help, "HELP|HL", "You already know what this command does (meta)"))

    # ================================================== #

    @staticmethod
    def addCommand(command):
        ConsoleManager.__commands.append(command)
        ConsoleManager.__commands.sort(key=lambda c: c.name)

    @staticmethod
    def consoleManager():
        ConsoleManager.LOG_INFO('Try the "help" command for a list with all the commands and their syntax.')
        while True:
            command = ConsoleManager.INPUT_USER("").lower().split()

            if not command == []:
                commandExists = False
                for c in ConsoleManager.__commands:
                    if command[0] == str(c.name).lower() or command[0] == str(c.short).lower():
                        commandExists = True
                        c.execute(command[1:])
                        break

                if not commandExists:
                    ConsoleManager.LOG_ALERT('The command entered does not exist. Try the "help" command for a list with all the commands and their syntax.')

    # ================================================== #

    @staticmethod
    def INPUT_USER(caption):
        return input(ConsoleManager.__USER  + caption)

    @staticmethod
    def LOG_ALERT(alert):
        print(Fore.YELLOW + Style.BRIGHT + ConsoleManager.__ALERT + alert + Style.RESET_ALL)

    @staticmethod
    def LOG_ERROR(error):
        print(Fore.RED + Style.BRIGHT + ConsoleManager.__ERROR + error + Style.RESET_ALL)

    @staticmethod
    def LOG_MESSAGE(message):
        print(Fore.GREEN + Style.BRIGHT + ConsoleManager.__MESSAGE + message + Style.RESET_ALL)

    @staticmethod
    def LOG_INFO(info):
        print(Fore.BLUE + Style.BRIGHT + ConsoleManager.__INFO + info + Style.RESET_ALL)

# ===== ========== ==================================================================================================== #
