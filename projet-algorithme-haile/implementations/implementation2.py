import random

class Cell:
    """Représente une cellule dans le Jeu de la Vie."""
    
    def __init__(self, is_alive=False):
        self.is_alive = is_alive

    def __repr__(self):
        return '1' if self.is_alive else '0'


class Grid:
    """Représente la grille du Jeu de la Vie."""
    
    def __init__(self, size):
        self.size = size
        self.grid = [[Cell(random.choice([True, False])) for _ in range(size)] for _ in range(size)]

    def update(self):
        """Met à jour la grille pour la génération suivante."""
        new_grid = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        
        for row in range(self.size):
            for col in range(self.size):
                alive_neighbors = self.count_alive_neighbors(row, col)
                cell = self.grid[row][col]
                
                # Règles du jeu
                if cell.is_alive:
                    if alive_neighbors in [2, 3]:
                        new_grid[row][col].is_alive = True
                else:
                    if alive_neighbors == 3:
                        new_grid[row][col].is_alive = True

        self.grid = new_grid

    def count_alive_neighbors(self, row, col):
        """Compte le nombre de cellules vivantes autour d'une cellule donnée."""
        alive_count = 0
        for r in range(max(0, row - 1), min(self.size, row + 2)):
            for c in range(max(0, col - 1), min(self.size, col + 2)):
                if (r != row or c != col) and self.grid[r][c].is_alive:
                    alive_count += 1
        return alive_count

    def display(self):
        """Affiche la grille dans le terminal."""
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))
        print()

