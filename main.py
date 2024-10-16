import string

def generer_grille():
    # Créer les en-têtes de colonnes (A à J)
    colonnes = list(string.ascii_uppercase[:10])  # Liste des lettres de A à J
    
    # Afficher la première ligne avec les lettres (en-têtes horizontales)
    print("    " + "  ".join(f"{col:>3}" for col in colonnes))  # Laisse 3 espaces entre les lettres

    # Générer et afficher la grille avec les identifiants de cellule
    for ligne in range(1, 11):  # Pour chaque ligne de 1 à 10
        # Créer et afficher la ligne avec les identifiants de cellule sans zéros inutiles
        print(f"{ligne:2}  " + "  ".join(f"{col}{ligne}" for col in colonnes))

# Appeler la fonction pour afficher la grille
generer_grille()


class Grille:
    def __init__(self, taille=10):
        self.taille = taille
        self.grille = [['.' for _ in range(taille)] for _ in range(taille)]  # '.' indique une case vide

    def afficher(self):
        for ligne in self.grille:
            print("  ".join(ligne))
        print()

    def peut_placer(self, bateau, x, y, orientation):
        # Vérifier les limites de la grille
        if orientation == 'horizontal':
            if y + len(bateau) > self.taille:
                return False
            for j in range(y, y + len(bateau)):
                if self.grille[x][j] != '.':
                    return False
        else:  # vertical
            if x + len(bateau) > self.taille:
                return False
            for i in range(x, x + len(bateau)):
                if self.grille[i][y] != '.':
                    return False
        return True

    def placer_bateau(self, bateau, x, y, orientation):
        if self.peut_placer(bateau, x, y, orientation):
            for i in range(len(bateau)):
                if orientation == 'horizontal':
                    self.grille[x][y + i] = bateau[0]  # Utilise le premier caractère du nom du bateau
                else:
                    self.grille[x + i][y] = bateau[0]
            return True
        else:
            print("Placement invalide.")
            return False


# Exemple d'utilisation
grille = Grille()
grille.afficher()

bateaux = {
    "Porte-avions": "P",
    "Croiseur": "C",
    "Sous-marin": "S",
    "Destroyer": "D",
    "Torpilleur": "T"
}

# Placer les bateaux
grille.placer_bateau(bateaux["Porte-avions"], 0, 0, 'horizontal')
grille.placer_bateau(bateaux["Croiseur"], 1, 0, 'vertical')
grille.afficher()

