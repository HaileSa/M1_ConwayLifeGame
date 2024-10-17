import random

def create_grid(n):
    return [[random.choice([0, 1]) for i in range(n)] for j in range(n)]

def print_grid(grid):
    for row in grid:
        print(" ".join(['█' if cell == 1 else ' ' for cell in row]))
