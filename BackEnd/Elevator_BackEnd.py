
class Elevator:

    def __init__(self, floors):
        #self.__cur_instruction = "IDLE"
        #self.__pre_instruction = "IDLE"

        self.__cur_floor = 1  # Bajo
        self.__doorsOpen = False
        self.__floor_buttons = []
        self.__elevator_buttons = []

        self.__floors = floors
        self.__targets = []

        for b in range(self.__floors):
            self.__floor_buttons.append(False)
            self.__elevator_buttons.append(False)

        #self.__floor_buttons[self.__floors-5] = True
        #self.__elevator_buttons[self.__floors - 5] = True
        #self.__floor_buttons[self.__floors - 7] = True
        #self.__elevator_buttons[self.__floors - 3] = True

    def add_target(self, target):
        self.__targets.append(target)

    def next_instruction(self):
        #self.__pre_instruction = self.__cur_instruction
        if self.__doorsOpen:
            self.__doorsOpen = False
        else:
            if len(self.__targets) > 0:
                if self.__targets[0] == self.__cur_floor:
                    self.__doorsOpen = True
                    del self.__targets[0]
                else:
                    if self.__targets[0] > self.__cur_floor:
                        self.__cur_floor += 1
                    else:
                        self.__cur_floor -= 1
            else:
                pass

    @property
    def floor_buttons(self):
        return self.__floor_buttons

    @property
    def elevator_buttons(self):
        return self.__elevator_buttons
