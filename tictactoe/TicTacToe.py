from multiprocessing.sharedctypes import Value


class TicTacToe:
    def __init__(self, x_start: bool=True):
        self.__x_start = x_start
        self.__field = [["", "", ""], ["", "", ""], ["", "", ""]]

    def x_turn(self) -> bool:
        turns = 9 - sum([line.count("") for line in self.__field])
        if self.__x_start:
            return True if turns % 2 == 0 else False
        if not self.__x_start:
            return True if turns % 2 == 1 else False

    def set(self, x, y) -> bool:
        if not 0 <= x <= 2 and not not 0 <= y <= 2:
            raise ValueError("The position does not exist.")
        if not self.__field[y][x] == "":
            return False
        else:
            if self.x_turn():
                self.__field[y][x] = "x"
            else:
                self.__field[y][x] = "o"
    
    def is_finished(self) -> bool:
        return True if sum([line.count("") for line in self.__field]) == 0 else False

    def is_won(self) -> tuple:
        for player in ["x", "o"]:
            # TODO: check verticly
            for row in range(3):
                if self.__field[0][row] == player and self.__field[1][row] == player and self.__field[2][row] == player:
                    return (True, player)
            # check horizontily
            for layer in self.__field:
                if layer.count(player) == 3:
                    return (True, player)
            # check cross
            if self.__field[1][1] == player and ((self.__field[0][0] == player  and self.__field[2][2] == player) or \
                (self.__field[2][0] == player  and self.__field[0][2] == player)):
                return (True, player)
        return (False,)

    def get_field(self) -> tuple:
        return tuple(tuple(line) for line in self.__field)

    def get_x_start(self) -> bool:
        return self.__x_start
