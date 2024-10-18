import pytest
from implementations.implementation2 import Cell, Grid

def test_cell_initialization():
    """Test l'initialisation des cellules."""
    dead_cell = Cell()
    alive_cell = Cell(is_alive=True)

    assert dead_cell.is_alive == False
    assert alive_cell.is_alive == True

def test_grid_initialization():
    """Test l'initialisation de la grille."""
    grid_size = 5
    grid = Grid(grid_size)

    assert len(grid.grid) == grid_size
    assert len(grid.grid[0]) == grid_size

def test_count_alive_neighbors():
    """Test le comptage des voisins vivants."""
    grid = Grid(3)
    grid.grid[0][0].is_alive = True
    grid.grid[0][1].is_alive = True
    grid.grid[1][0].is_alive = True

    assert grid.count_alive_neighbors(1, 1) == 3
    assert grid.count_alive_neighbors(0, 0) == 1
    assert grid.count_alive_neighbors(2, 2) == 0

def test_update():
    """Test la mise à jour de la grille."""
    grid = Grid(3)
    grid.grid[0][0].is_alive = True
    grid.grid[0][1].is_alive = True
    grid.grid[1][0].is_alive = True
    
    # Avant mise à jour
    grid.update()
    
    # Test de l'état après mise à jour
    assert grid.grid[0][0].is_alive == True  # Reste vivant
    assert grid.grid[0][1].is_alive == True  # Reste vivant
    assert grid.grid[1][0].is_alive == False # Devient mort

    # Ajout d'une cellule morte pour voir si elle devient vivante
    grid.grid[1][1].is_alive = False
    grid.update()
    
    # La cellule (1, 1) devrait devenir vivante
    assert grid.grid[1][1].is_alive == True

if __name__ == "__main__":
    pytest.main()
