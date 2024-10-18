# Projet : Jeu de la Vie de Conway

Bienvenue dans mon implémentation du célèbre "Jeu de la Vie" de Conway ! ✨🦠 Ce projet simule un automate cellulaire qui évolue au fil des générations en fonction de règles simples, mais pouvant donner lieu à des comportements complexes.

## Fonctionnalités

- **Taille personnalisée de la grille** : L'utilisateur peut choisir la taille de la grille à l'initialisation.
- **Affichage dynamique des générations** : La grille évolue au fur et à mesure des générations, avec une génération affichée toutes les 0,5 secondes.
- **Suivi des générations** : Le numéro de la génération courante est affiché sous la grille.
- **Effacement automatique** : L'écran est effacé à chaque génération pour ne montrer que l'état actuel.
- **Arrêt automatique** : Le programme s'arrête après un nombre de générations défini par l'utilisateur.

## Utilisation

1. Clonez ce dépôt sur votre machine locale.
2. Exécutez le programme via `python main.py`.
3. Entrez la taille de la grille et le nombre de générations à simuler.
4. Regardez l'évolution du jeu de la vie en temps réel dans le terminal.

### Exemple de flux utilisateur

```bash
$ python main.py
Veuillez entrer la taille de la grille : 10
Veuillez entrer le nombre de générations à générer : 5
