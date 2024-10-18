import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) ##Pour permettre a pytest de fonctionner

from implementations.implementation1 import create_grid, update_grid

#Test sur la création de la grille et l'insertion des cellules vivantes ou mortes (0 ou1)
def test_create_grid():
    n = 5
    grid = create_grid(n)
    assert len(grid) == n
    for row in grid:
        assert len(row) == n
        assert all(cell in [0, 1] for cell in row)


def test_update_grid():
    grid = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]
    expected_grid = [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 1]
    ]
    assert update_grid(grid) == expected_grid

