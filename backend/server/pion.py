class Pion:
    def __init__(self, value, x, y):
        self.value = value
        self.moved = False

        self.abs = x
        self.ord = y

    def get_value(self):
        return self.value
    # --- Checkup de places ---
    def empty_left(self, grid):
        if self.abs != 0:
            if grid[self.ord][self.abs - 1].value == 0:
                return True
        return False

    def empty_right(self, grid):
        if self.abs != 3:
            if grid[self.ord][self.abs + 1].value == 0:
                return True
        return False

    def empty_up(self, grid):
        if self.ord != 0:
            if grid[self.ord-1][self.abs].value == 0:
                return True
        return False

    def empty_down(self, grid):
        if self.ord != 3:
            if grid[self.ord + 1][self.abs].value == 0:
                return True
        return False

    # --- Mouvements ---
    def move_left(self, grid):
        if self.empty_left(grid):
            grid[self.ord][self.abs] = Pion(0, self.abs, self.ord)
            self.abs -= 1
            grid[self.ord][self.abs] = self
        return grid

    def move_right(self, grid):
        if self.empty_right(grid):
            grid[self.ord][self.abs] = Pion(0, self.abs, self.ord)
            self.abs += 1
            grid[self.ord][self.abs] = self
        return grid

    def move_up(self, grid):
        if self.empty_up(grid):
            grid[self.ord][self.abs] = Pion(0, self.abs, self.ord)
            self.ord -= 1
            grid[self.ord][self.abs] = self
        return grid

    def move_down(self, grid):
        if self.empty_down(grid):
            grid[self.ord][self.abs] = Pion(0, self.abs, self.ord)
            self.ord += 1
            grid[self.ord][self.abs] = self
        return grid


t_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(len(t_grid)):
    for j in range(len(t_grid)):
        t_grid[i][j] = Pion(0, i, j)

assert not Pion(4, 0, 0).empty_left(t_grid), 'C\'est un non pour le joueur français.'
assert Pion(4, 1, 0).empty_left(t_grid), 'C\'est un non pour le joueur français.'

assert not Pion(4, 3, 0).empty_right(t_grid), 'C\'est un non pour le joueur français.'
assert Pion(4, 2, 0).empty_right(t_grid), 'C\'est un non pour le joueur français.'

assert not Pion(4, 0, 0).empty_up(t_grid), 'C\'est un non pour le joueur français.'
assert Pion(4, 0, 1).empty_up(t_grid), 'C\'est un non pour le joueur français.'

assert not Pion(4, 0, 3).empty_down(t_grid), 'C\'est un non pour le joueur français.'
assert Pion(4, 0, 0).empty_down(t_grid), 'C\'est un non pour le joueur français.'
