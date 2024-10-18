# Analyse de la Complexité de l'Implémentation 1

## Complexité de la Fonction `create_grid`

La fonction `create_grid` parcourt chaque cellule de la grille de taille `n x n` et génère aléatoirement une valeur (0 ou 1) pour chaque cellule.

- Boucle externe : O(n)
- Boucle interne : O(n)
- Choix aléatoire pour chaque cellule : O(1)

**Complexité totale** : O(n²)

---

## Complexité de la Fonction `print_grid`

La fonction `print_grid` parcourt la grille pour afficher chaque cellule, avec deux boucles imbriquées.

- Boucle externe : O(n)
- Boucle interne : O(n)
- Affichage de chaque cellule : O(1)

**Complexité totale** : O(n²)

---

## Complexité de la Fonction `update_grid`

La fonction `update_grid` parcourt chaque cellule de la grille et vérifie ses 8 voisins pour déterminer le prochain état de la cellule.

- Boucle externe : O(n)
- Boucle interne : O(n)
- Vérification des 8 voisins (constante) : O(1)

**Complexité totale** : O(n²)

---

## Conclusion

L'implémentation globale a une complexité temporelle de O(n²), où `n` est la taille de la grille (le nombre de cellules par côté). Chaque génération du Jeu de la Vie nécessite de parcourir l'ensemble de la grille pour appliquer les règles et mettre à jour chaque cellule.
