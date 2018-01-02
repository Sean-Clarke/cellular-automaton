""" This is a module docstring

"""

import random

class Grid:
    """ This is a class docstring

    """
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self._cells = dict()
        for x in range(0, self.width):
            for y in range(0, self.height):
                self._cells[(x, y)] = (False, False)

    def get_active(self, x, y) -> bool:
        """ This is a function docstring

        """
        if (x, y) in self._cells:
            current_state, next_state = self._cells[(x, y)]
            return current_state
        return False

    def get_next(self, x, y) -> bool:
        """ This is a function docstring

        """
        if (x, y) in self._cells:
            current_state, next_state = self._cells[(x, y)]
            return next_state
        return False

    def draw_cells(self):
        """ This is a function docstring

        """
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.get_active(x, y):
                    print("X ", end="")
                elif not self.get_active(x, y):
                    print("  ", end="")
            print("")
        print("")

    def activate_cell(self, x: int, y: int):
        """ This is a function docstring

        """
        self._cells[(x, y)] = (True, False)

    def deactivate_cell(self, x: int, y: int):
        """ This is a function docstring

        """
        self._cells[(x, y)] = (False, False)

    def clear_grid(self):
        """ This is a function docstring

        """
        for (x, y) in self._cells:
            self.deactivate_cell(x, y)

    def count_neighbours(self, x, y) -> int:
        """ This is a function docstring

        """
        count = 0
        if self.get_active(x + 1, y):
            count += 1
        if self.get_active(x + 1, y + 1):
            count += 1
        if self.get_active(x, y + 1):
            count += 1
        if self.get_active(x - 1, y + 1):
            count += 1
        if self.get_active(x - 1, y):
            count += 1
        if self.get_active(x - 1, y - 1):
            count += 1
        if self.get_active(x, y - 1):
            count += 1
        if self.get_active(x + 1, y - 1):
            count += 1
        return count

    def set_next(self, x, y):
        """ This is a function docstring

        """
        if self.get_active(x, y):
            neighbours = self.count_neighbours(x, y)
            if neighbours == 2 or neighbours == 3:
                self._cells[(x, y)] = (self.get_active(x, y), True)
            else:
                self._cells[(x, y)] = (self.get_active(x, y), False)
        elif not self.get_active(x, y):
            neighbours = self.count_neighbours(x, y)
            if neighbours == 3:
                self._cells[(x, y)] = (self.get_active(x, y), True)
            else:
                self._cells[(x, y)] = (self.get_active(x, y), False)

    def update_cell(self, x, y):
        """ This is a function docstring

        """
        if self.get_next(x, y):
            self.activate_cell(x, y)
        elif not self.get_next(x, y):
            self.deactivate_cell(x, y)

    def update_cells(self):
        """ This is a function docstring

        """
        for (x, y) in self._cells:
            self.set_next(x, y)

        for  (x, y) in self._cells:
            self.update_cell(x, y)

    def randomize_cells(self):
        """ This is a function docstring

        """
        for (x, y) in self._cells:
            self._cells[(x, y)] = (bool(random.getrandbits(1)), self.get_next(x, y))
