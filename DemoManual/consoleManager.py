
# ===== IMPORTS ==================================================================================================== #

from os import system
#from textwrap import wrap
from terminaltables import SingleTable

# ===== COMMAND ==================================================================================================== #

class Command:

    def __init__(self, name, short, action, syntax, description):
        self.__name = name
        self.__short = short
        self.action = action
        self.__syntax = syntax
        self.__description = description

    def execute(self, arguments):
        self.action(arguments)

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

    def __help(args):
        print(ConsoleManager.__INFO + "List of all the commands and their syntax:")
        tableData = [["Command", "Description", "Syntax"]]
        for c in ConsoleManager.__commands:
            # '\n'.join(wrap(c.description, 40))
            tableRow = [c.name, c.description, c.syntax]
            tableData.append(tableRow)
        table = SingleTable(tableData)
        table.inner_row_border = True
        print(" " + str(table.table).replace("\n", "\n "))

    def __clear(args):
        system('cls')
        print()

    __commands.append(Command("CLEAR", "CL", __clear, "CLEAR|CL", "Clears the screen from all previous commands."))
    __commands.append(Command("HELP", "HL", __help, "HELP|HL", "You already know what this command does (meta)."))

    @staticmethod
    def addCommand(command):
        ConsoleManager.__commands.append(command)
        ConsoleManager.__commands.sort(key=lambda c: c.name)

    @staticmethod
    def consoleManager(running):
        while running:
            command = input(ConsoleManager.__USER).lower().split()

            commandExists = False
            for c in ConsoleManager.__commands:
                if command[0] == str(c.name).lower() or command[0] == str(c.short).lower():
                    commandExists = True
                    c.action(command[1:])
                    break

            if not commandExists:
                print(ConsoleManager.__ALERT + 'The command entered does not exist. Try the "help" command for a list with all the commands and their syntax.')

    @staticmethod
    def LOG_USER():
        return ConsoleManager.__USER

    @staticmethod
    def LOG_ALERT():
        return ConsoleManager.__ALERT

    @staticmethod
    def LOG_ERROR():
        return ConsoleManager.__ERROR

    @staticmethod
    def LOG_MESSAGE():
        return ConsoleManager.__MESSAGE

    @staticmethod
    def LOG_INFO():
        return ConsoleManager.__INFO

# ===== ========== ==================================================================================================== #
