from implementations.implementation1 import create_grid, print_grid, update_grid
import os

def clear_screen():
    # Efface l'écran du terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid_with_generation(grid, generation):
    print_grid(grid)
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

    grid = create_grid(n)  # Crée la grille
    print_grid_with_generation(grid, 0)  # Affiche la grille initiale avec génération 0

    generation = 0  # Initialise le compteur de générations
    while True:
        user_input = input("Appuyez sur Entrée pour passer à la génération suivante ou 'bye' pour quitter...")

        if user_input == 'bye':
            break  # Sort de la boucle pour quitter
        
        generation += 1  # Incrémente le compteur de générations
        clear_screen() 
        
        # Met à jour et affiche la nouvelle génération
        grid = update_grid(grid)
        print_grid_with_generation(grid, generation)


# Ca ne fonctionne pas sans
if __name__ == "__main__":
    main()
