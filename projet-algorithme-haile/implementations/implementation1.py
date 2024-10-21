import random

def create_grid(n):
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            cell = random.choice([0, 1])
            row.append(cell)
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(['♥' if cell == 1 else ' ' for cell in row]))
        
def count_neighbors(grid, x, y, n):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for direction_x, direction_y in directions:
        neighbor_x, neighbor_y = x + direction_x, y + direction_y
        if 0 <= neighbor_x < n and 0 <= neighbor_y < n:
            count += grid[neighbor_x][neighbor_y]
    return count

def update_grid(grid):
    n = len(grid)
    new_grid = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            alive_neighbors = count_neighbors(grid, i, j, n)
            if grid[i][j] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[i][j] = 0  # Cellule morte
                else:
                    new_grid[i][j] = 1  # Reste vivante
            else:
                if alive_neighbors == 3:
                    new_grid[i][j] = 1  # Cellule naît
                else:
                    new_grid[i][j] = 0  # Reste morte
    return new_grid