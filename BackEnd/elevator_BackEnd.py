
class Elevator_BackEnd:

    FLOOR = False
    ELEVATOR = True

    def __init__(self, floors):
        self.__cur_floor = 1  # Bajo
        self.__doorsOpen = False
        self.__floor_buttons = []
        self.__elevator_buttons = []

        self.__floors = floors
        self.__targets = []

        for b in range(self.__floors):
            self.__floor_buttons.append(False)
            self.__elevator_buttons.append(False)

    def add_target(self, target, source):
        if len(self.__targets) < 2 or not self.__targets[-1] == target:
            self.__targets.append(target)
        if source == Elevator_BackEnd.FLOOR:
            self.__floor_buttons[self.__floors-target] = True
        elif source == Elevator_BackEnd.ELEVATOR:
            self.__elevator_buttons[self.__floors-target] = True

    def next_step(self):
        if self.__doorsOpen:
            self.__doorsOpen = False
        else:
            if len(self.__targets) > 0:
                if self.__targets[0] == self.__cur_floor:
                    self.__doorsOpen = True
                    self.__floor_buttons[self.__floors-self.__targets[0]] = False
                    self.__elevator_buttons[self.__floors-self.__targets[0]] = False
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

    @property
    def cur_floor(self):
        return self.__cur_floor

    @property
    def doorsOpen(self):
        return self.__doorsOpen
