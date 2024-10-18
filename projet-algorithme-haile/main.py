import os
import time
from implementations.implementation1 import create_grid, print_grid, update_grid

def clear_screen():
    # Efface l'écran du terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid_with_generation(grid, generation):
    print("LIFE GAME   ≽^•⩊•^≼")
    print("")
    print_grid(grid)
    print("")
    print(f"Génération : {generation}") 

def main():
    try:
        n = int(input("Veuillez entrer la taille de la grille : "))
        if n <= 0:
            print("Veuillez entrer un nombre positif.")
            return
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    # Demande du nombre de générations à afficher
    try:
        num_generations = int(input("Veuillez entrer le nombre de générations à générer : "))
        if num_generations <= 0:
            print("Veuillez entrer un nombre positif.")
            return
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    clear_screen()
    grid = create_grid(n)  # Crée la grille
    print_grid_with_generation(grid, 0)  # Affiche la grille initiale avec génération 0

    generation = 0  # Initialise le compteur de générations

    # Boucle while pour générer les générations
    while generation < num_generations:
        time.sleep(0.5)  # Attend 1 seconde entre chaque génération
        clear_screen()
        
        generation += 1  # Incrémente le compteur de générations
        grid = update_grid(grid)  # Met à jour la grille
        print_grid_with_generation(grid, generation)  # Affiche la nouvelle génération


# Si le nom du script c'est main, alors on lance main()
if __name__ == "__main__":
    main()