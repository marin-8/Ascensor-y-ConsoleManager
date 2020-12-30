
# ===== IMPORTS ==================================================================================================== #
# ===== COMMAND ==================================================================================================== #

class Command:

    def __init__(self, name, short, action, syntax, description):
        self.name = name
        self.short = short
        self.action = action
        self.syntax = syntax
        self.description = description

    def execute(self, arguments):
        self.action(arguments)

# ===== ========== ==================================================================================================== #
