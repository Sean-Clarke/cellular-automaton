""" This is a module docstring

"""

import time
import Grid

class CellGame:
    """ This is a class docstring

    """
    def __init__(self, size):
        self.grid = Grid.Grid(size, size)
        self.pause = True

    def draw_grid(self):
        """ This is a function docstring

        """
        self.grid.draw_cells()

    def update_game(self):
        """ This is a function docstring

        """
        self.grid.update_cells()
        self.draw_grid()

    def game_cycle(self, cycles: int, delay: float):
        """ This is a function docstring

        """
        cycles_left = cycles
        while cycles_left > 0:
            self.update_game()
            time.sleep(delay)
            cycles_left -= 1

    def process_input(self, user_input):
        """ This is a function docstring

        """
        command, pos = user_input

        if command == "a":
            xpos, ypos = pos.split(",")
            self.grid.activate_cell(int(xpos), int(ypos))
            self.draw_grid()
        elif command == "d":
            xpos, ypos = pos.split(",")
            self.grid.deactivate_cell(int(xpos), int(ypos))
            self.draw_grid()
        elif command == "r":
            self.grid.randomize_cells()
            self.draw_grid()
        elif command == "c":
            self.grid.clear_grid()
            self.draw_grid()
        elif command == "g":
            self.make_glider()
            self.draw_grid()
        elif command == "p":
            self.make_pulsar()
            self.draw_grid()
        elif command == "$":
            self.grid.clear_grid()
            self.grid.activate_cell(30, 31)
            self.grid.activate_cell(30, 32)
            self.grid.activate_cell(30, 33)
            self.grid.activate_cell(30, 35)
            self.grid.activate_cell(30, 36)
            self.grid.activate_cell(30, 37)
            self.grid.activate_cell(31, 31)
            self.grid.activate_cell(32, 31)
            self.grid.activate_cell(31, 37)
            self.grid.activate_cell(32, 37)
            self.grid.activate_cell(33, 32)
            self.grid.activate_cell(33, 36)
            self.grid.activate_cell(34, 33)
            self.grid.activate_cell(34, 34)
            self.grid.activate_cell(34, 35)
            self.draw_grid()
        elif command == "s":
            cycles, delay = pos.split(" ")
            self.game_cycle(int(cycles), float(delay))
        elif command == "q":
            return False
        return True

    def get_input(self):
        """ This is a function docstring

        """
        user_input = input()
        command = user_input[:1]
        arg = user_input[2:]

        return command, arg

    def make_glider(self):
        """ This is a function docstring

        """
        self.grid.clear_grid()
        self.grid.activate_cell(3, 0)
        self.grid.activate_cell(3, 1)
        self.grid.activate_cell(3, 2)
        self.grid.activate_cell(2, 2)
        self.grid.activate_cell(1, 1)

    def make_pulsar(self):
        """ This is a function docstring

        """
        self.grid.clear_grid()
        self.grid.activate_cell(5, 1)
        self.grid.activate_cell(5, 2)
        self.grid.activate_cell(5, 3)
        self.grid.activate_cell(6, 3)
        self.grid.activate_cell(10, 3)
        self.grid.activate_cell(11, 1)
        self.grid.activate_cell(11, 2)
        self.grid.activate_cell(11, 3)
        self.grid.activate_cell(1, 5)
        self.grid.activate_cell(2, 5)
        self.grid.activate_cell(3, 5)
        self.grid.activate_cell(3, 6)
        self.grid.activate_cell(6, 5)
        self.grid.activate_cell(7, 5)
        self.grid.activate_cell(5, 6)
        self.grid.activate_cell(7, 6)
        self.grid.activate_cell(5, 7)
        self.grid.activate_cell(6, 7)
        self.grid.activate_cell(9, 5)
        self.grid.activate_cell(10, 5)
        self.grid.activate_cell(9, 6)
        self.grid.activate_cell(11, 6)
        self.grid.activate_cell(10, 7)
        self.grid.activate_cell(11, 7)
        self.grid.activate_cell(13, 5)
        self.grid.activate_cell(14, 5)
        self.grid.activate_cell(15, 5)
        self.grid.activate_cell(13, 6)
        self.grid.activate_cell(1, 11)
        self.grid.activate_cell(2, 11)
        self.grid.activate_cell(3, 11)
        self.grid.activate_cell(3, 10)
        self.grid.activate_cell(6, 11)
        self.grid.activate_cell(7, 11)
        self.grid.activate_cell(5, 10)
        self.grid.activate_cell(7, 10)
        self.grid.activate_cell(5, 9)
        self.grid.activate_cell(6, 9)
        self.grid.activate_cell(9, 11)
        self.grid.activate_cell(10, 11)
        self.grid.activate_cell(9, 10)
        self.grid.activate_cell(11, 10)
        self.grid.activate_cell(10, 9)
        self.grid.activate_cell(11, 9)
        self.grid.activate_cell(13, 11)
        self.grid.activate_cell(14, 11)
        self.grid.activate_cell(15, 11)
        self.grid.activate_cell(13, 10)
        self.grid.activate_cell(5, 13)
        self.grid.activate_cell(6, 13)
        self.grid.activate_cell(5, 14)
        self.grid.activate_cell(5, 15)
        self.grid.activate_cell(10, 13)
        self.grid.activate_cell(11, 13)
        self.grid.activate_cell(11, 14)
        self.grid.activate_cell(11, 15)

C1 = CellGame(60)
print("You have started playing a game!")

C1.draw_grid()

print("Enter 'a x,y' to activate cell at x, y")
print("Enter 'd x,y' to deactivate cell at x, y")
print("Enter 's 1 0' to iterate 1 game cycle")
print("Enter 'r' to initialize a random game seed")
print("Enter 'c' to deactivate all cells")
print("Enter 'g' to create a glider on an otherwise empty grid")
print("Enter 'p' to create a pulsar on an otherwise empty grid")
print("Enter '$' to create a spaceship on an otherwise empty grid")
print("Enter 'q' to stop playing.")

while True:
    user_input = C1.get_input()
    if not C1.process_input(user_input):
        break

print("Thank you for playing!")
