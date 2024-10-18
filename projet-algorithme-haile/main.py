from implementations.implementation1 import create_grid, print_grid, update_grid

def main():
    # Demande à l'utilisateur de saisir la taille de la grille
    try:
        n = int(input("Veuillez entrer la taille de la grille : "))
        if n <= 0:
            print("Veuillez entrer un nombre positif.")
            return
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    # Demande à l'utilisateur de saisir le nombre de générations
    try:
        generations = int(input("Veuillez entrer le nombre de générations à afficher : "))
        if generations < 0:
            print("Veuillez entrer un nombre non négatif.")
            return
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    grid = create_grid(n)  # Crée la grille
    print_grid(grid)  # Affiche la grille

    for generation in range(generations):  # Exécute le nombre de générations spécifié par l'utilisateur
        grid = update_grid(grid)
        print(f"Génération {generation + 1} :")
        print_grid(grid)

if __name__ == "__main__":
    main()
