
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
    __WARNING = " [WARNING] > "
    __ERROR = "   [ERROR] > "
    __MESSAGE = " [MESSAGE] > "
    __INFO = "    [INFO] > "

    __commands = []

    # ================================================== #

    def __help(args):
        ConsoleManager.LOG_INFO("List of all the commands and their syntax:")
        lines_CS = Fore.BLUE + Style.NORMAL
        header_CS = Fore.GREEN + Style.NORMAL
        rows_CS = Fore.CYAN + Style.BRIGHT
        tableData = [[header_CS + "Command" + lines_CS, header_CS + "Short" + lines_CS, header_CS + "Description" + lines_CS, header_CS + "Syntax" + lines_CS]]
        for c in ConsoleManager.__commands:
            tableRow = [rows_CS + c.name + lines_CS, rows_CS + c.short + lines_CS, rows_CS + c.description + lines_CS, rows_CS + c.syntax + lines_CS]
            tableData.append(tableRow)
        table = SingleTable(tableData)
        table.inner_row_border = True
        print(lines_CS + " " + str(table.table).replace("\n", "\n ") + Style.RESET_ALL)

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
                    ConsoleManager.LOG_WARNING('The command entered does not exist. Try the "help" command for a list with all the commands and their syntax.')

    # ================================================== #

    @staticmethod
    def INPUT_USER(caption):
        userInput = input(Style.BRIGHT + ConsoleManager.__USER  + caption)
        print(Style.RESET_ALL, end="")
        return userInput

    @staticmethod
    def LOG_WARNING(alert):
        print(Fore.YELLOW + ConsoleManager.__WARNING + alert + Style.RESET_ALL)

    @staticmethod
    def LOG_ERROR(error):
        print(Fore.RED + ConsoleManager.__ERROR + error + Style.RESET_ALL)

    @staticmethod
    def LOG_MESSAGE(message):
        print(Fore.GREEN + Style.BRIGHT + ConsoleManager.__MESSAGE + message + Style.RESET_ALL)

    @staticmethod
    def LOG_INFO(info):
        print(Fore.BLUE + Style.BRIGHT + ConsoleManager.__INFO + info + Style.RESET_ALL)

# ===== ========== ==================================================================================================== #
