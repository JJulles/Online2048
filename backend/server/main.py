import random
from pion import Pion

def same_grid(g1, g2):
    """
    Fonction servant à comparer deux grilles de valeurs
    En entrée: g1(list), g2(list)
    En sortie: Boolean
    """
    if len(g1) != len(g2):
        return False
    else:
        for i in range(len(g1)):
            for j in range(len(g1[0])):
                if g1[i][j].value != g2[i][j].value:
                    return False
    return True


def more_moves(grid):
    """
    Fonction servant à vérifier si on peut faire d'autres mouvements
    En entrée: grid(list)
    En sortie: Boolean
    """
    move = False
    # Lineaire
    for i in range(len(grid)):
        for k in range(len(grid)-1):
            if (grid[i][k].value == grid[i][k+1].value
                    or grid[i][k].value == 0 or grid[i][k+1].value==0):
                move = True

    # Verticale
    for j in range(len(grid[0])):
        for k in range(len(grid[0]) - 1):
            if (grid[k][j].value == grid[k+1][j].value
                    or grid[k][j].value == 0 or grid[k+1][j].value==0):
                move = True
    return move


def full(grid):
    """
    Fonction servant à vérifier si la grille est pleine ou non
    En entrée: grid(list)
    En sortie: Boolean
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j].value == 0:
                return False
    return True


def new_piece(grid):
    """
    Set a new tile in the game at an empty position

    :param grid:
    :return:
    """
    if not full(grid):
        r = random.randint(1, 2)
        x, y = random.randint(0, 3), random.randint(0, 3)
        while grid[y][x].value != 0:
            x, y = random.randint(0, 3), random.randint(0, 3)
        value = 2**r # Can be 2 or 4
        grid[y][x] = Pion(value,x,y)

    return grid

def order_leaderboard(leaderboard_list):
    """
    This function order a list of score, based on the following example:
    l = [("pseudo1",<scoreINT>),("pseudo2",<scoreINT>),("pseudo1",<scoreINT>)]

    This function orders the list by decreasing score, the weakest at the end

    :param leaderboard_list:
    :return: leaderboard_list_ordered
    """
    print(leaderboard_list)
    leaderboard_list_copy = []
    for i in range(len(leaderboard_list)):
        leaderboard_list_copy.append([leaderboard_list[i][0], leaderboard_list[i][1]])

    leaderboard_list_ordered = sorted(leaderboard_list_copy, key=lambda tup: tup[1], reverse=True)
    return leaderboard_list_ordered

class Arcade2048:
    def __init__(self):
        #  Create the grid
        self.grid = [[Pion(0,x,y) for x in range(4)] for y in range(4)]
        randomX = random.randint(0, 3)
        randomY = random.randint(0, 3)

        # Random piece to start the game
        self.grid[randomX][randomY].value = 2

        # Init score
        self.score = 0

        self.leaderboard = []

    def get_grid(self):
        grid = [[self.grid[y][x].value for x in range(len(self.grid[0]))] for y in range(len(self.grid))]
        return grid

    def get_score(self):
        return self.score

    def get_more_moves(self):
        return more_moves(self.grid)

    def get_leaderboard(self):
        return self.leaderboard

    def update_leaderboard(self, pseudo, score):
        try:
            self.leaderboard.append( [pseudo, score] )
            self.leaderboard = order_leaderboard(self.leaderboard)
            if len(self.leaderboard) > 10:
                self.leaderboard.pop()
            print("leaderboard: ", self.leaderboard)
            return True
        except:
            return False


    def won(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].value == 2048:
                    return True
        return False

    def reset(self):
        try:
            self.grid = [[Pion(0,x,y) for x in range(4)] for y in range(4)]
            randomX = random.randint(0, 3)
            randomY = random.randint(0, 3)

            # Random piece to start the game
            self.grid[randomX][randomY].value = 2

            # reset score
            self.score = 0
            return True
        except:
            return False

    def move_left(self):
        grid_before_changes, grid_after_changes = [], []
        # On remplit les listes c1 et c2 avec les valeurs de la grille de base afin de les comparer plus tard
        for i in range(len(self.grid)):
            t1, t2 = [], []
            for j in range(len(self.grid[0])):
                t1.append(Pion(self.grid[i][j].value, j, i))
                t2.append(Pion(self.grid[i][j].value, j, i))
            grid_before_changes.append(t1)
            grid_after_changes.append(t2)

        # Modification de la liste c2
        for k in range(3):
            for i in range(0, len(grid_after_changes)):
                for j in range(0, len(grid_after_changes[0])):
                    # Si la case actuelle n'est pas vide
                    if grid_after_changes[i][j].value != 0:
                        # Si cette case n'est pas déjà à gauche sur la grille
                        if grid_after_changes[i][j].abs == 0:
                            continue
                        # Si la case à gauche est vide
                        elif grid_after_changes[i][j].empty_left(grid_after_changes):
                            # alors, on déplace les pions
                            grid_after_changes = grid_after_changes[i][j].move_left(grid_after_changes)
                        # Sinon
                        else:
                            # Si la case de gauche a la même valeur que celle actuelle
                            if grid_after_changes[i][j - 1].value == grid_after_changes[i][j].value:
                                # Si les deux cases n'ont pas bougé
                                if not grid_after_changes[i][j - 1].moved and not grid_after_changes[i][j].moved:
                                    # On augmente le score avant de bouger les cases
                                    self.score += grid_after_changes[i][j - 1].value + grid_after_changes[i][j].value
                                    # La case de gauche prend la valeur de la case actuelle
                                    grid_after_changes[i][j - 1].value += grid_after_changes[i][j].value
                                    # La case actuelle se vide
                                    grid_after_changes[i][j] = Pion(0, j, i)
                                    grid_after_changes[i][j - 1].moved = True

        # Si la grille initiale (c1) et la grille modifiée (c2) sont différentes, le mouvement est vraiment utile alors
        # on réalise ce mouvement, le c2 étant une sorte de test
        if not same_grid(grid_before_changes, grid_after_changes):
            self.grid = []
            # On remplit les listes c1 et c2 avec les valeurs de la grille de base afin de les comparer plus tard
            for i in range(len(grid_after_changes)):
                temp = []
                for j in range(len(grid_after_changes[0])):
                    temp.append(Pion(grid_after_changes[i][j].value, j, i))
                self.grid.append(temp)

            self.grid = new_piece(self.grid)

    def move_right(self):
        c1, c2 = [], []
        for i in range(len(self.grid)):
            t1, t2 = [], []
            for j in range(len(self.grid[0])):
                t1.append(Pion(self.grid[i][j].value, j, i))
                t2.append(Pion(self.grid[i][j].value, j, i))
            c1.append(t1)
            c2.append(t2)

        for k in range(3):
            for i in range(len(c2)):
                for j in range(len(c2[0])-1, -1, -1):
                    # Si la case actuelle n'est pas vide
                    if c2[i][j].value != 0:
                        # Si la case actuelle n'est pas déjà tout à droite
                        if c2[i][j].abs == 3:
                            pass
                        # Sinon si la case de droite est vide
                        elif c2[i][j].empty_right(c2):
                            # On déplace à droite
                            c2 = c2[i][j].move_right(c2)
                        # sinon s'il y a déjà une case avec une valeur
                        else:
                            # Si la case de droite a la même valeur que celle actuelle
                            if c2[i][j + 1].value == c2[i][j].value:
                                # Si la case de droite et celle actuelle n'ont pas bougé
                                if not c2[i][j + 1].moved and not c2[i][j].moved:
                                    # On augmente le score avant de bouger les cases
                                    self.score += c2[i][j + 1].value + c2[i][j].value
                                    c2[i][j + 1].value += c2[i][j].value
                                    c2[i][j] = Pion(0, j, i)
                                    c2[i][j + 1].moved = True

        if not same_grid(c1, c2):
            self.grid = []
            for i in range(len(c2)):
                temp = []
                for j in range(len(c2[0])):
                    temp.append(Pion(c2[i][j].value, j, i))
                self.grid.append(temp)
            self.grid = new_piece(self.grid)

    def move_up(self):
        c1, c2 = [], []
        for i in range(len(self.grid)):
            t1, t2 = [], []
            for j in range(len(self.grid[0])):
                t1.append(Pion(self.grid[i][j].value, j, i))
                t2.append(Pion(self.grid[i][j].value, j, i))
            c1.append(t1)
            c2.append(t2)

        for k in range(3):
            for i in range(len(c2)):
                for j in range(len(c2[0])):
                    if c2[i][j].value != 0:
                        if c2[i][j].ord == 0:
                            pass
                        elif c2[i][j].empty_up(c2):
                            c2 = c2[i][j].move_up(c2)
                        else:
                            if c2[i - 1][j].value == c2[i][j].value:
                                if not c2[i - 1][j].moved and not c2[i][j].moved:
                                    # On augmente le score avant de bouger les cases
                                    self.score += c2[i - 1][j].value + c2[i][j].value
                                    c2[i - 1][j].value += c2[i][j].value
                                    c2[i][j] = Pion(0, j, i)
                                    c2[i - 1][j].moved = True

        if not same_grid(c1, c2):
            self.grid = []
            for i in range(len(c2)):
                temp = []
                for j in range(len(c2[0])):
                    temp.append(Pion(c2[i][j].value, j, i))
                self.grid.append(temp)
            self.grid = new_piece(self.grid)

    def move_down(self):
        c1, c2 = [], []
        # On remplit les listes c1 et c2 avec les valeurs de la grille pour les comparer plus tard
        for i in range(len(self.grid)):
            t1, t2 = [], []
            for j in range(len(self.grid[0])):
                t1.append(Pion(self.grid[i][j].value, j, i))
                t2.append(Pion(self.grid[i][j].value, j, i))
            c1.append(t1)
            c2.append(t2)

        for k in range(3):
            for i in range(len(c2)-1, -1, -1):
                for j in range(len(c2[0])-1, -1, -1):
                    if c2[i][j].value != 0:
                        if c2[i][j].ord == 3:
                            pass
                        elif c2[i][j].empty_down(c2):
                            c2 = c2[i][j].move_down(c2)
                        else:
                            if c2[i + 1][j].value == c2[i][j].value:
                                if not c2[i + 1][j].moved and not c2[i][j].moved:
                                    self.score += c2[i + 1][j].value + c2[i][j].value
                                    c2[i + 1][j].value += c2[i][j].value
                                    c2[i][j] = Pion(0, j, i)
                                    c2[i + 1][j].moved = True

        if not same_grid(c1, c2):
            self.grid = []
            for i in range(len(c2)):
                temp = []
                for j in range(len(c2[0])):
                    temp.append(Pion(c2[i][j].value, j, i))
                self.grid.append(temp)

            self.grid = new_piece(self.grid)
