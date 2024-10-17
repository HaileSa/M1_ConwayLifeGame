import pytest
from implementations.implementation1 import create_grid

def test_create_grid():
    n = 5
    grid = create_grid(n)
    assert len(grid) == n  # Vérifie que la grille a n lignes
    for row in grid:
        assert len(row) == n  # Vérifie que chaque ligne a n colonnes
        assert all(cell in [0, 1] for cell in row)  # Vérifie que chaque cellule est 0 ou 1
