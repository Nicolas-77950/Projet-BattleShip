# Grille (10x10)
TAILLE_GRILLE = 10


# Liste des lettres de A à J
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(alphabet[:10])  # Affiche les 10 premières lettres, de A à J


# Créer une grille vide 10x10
def creer_grille():
    return [["O" for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]


# Afficher la grille entière avec les lettres de A à J
def afficher_grille(grille):
    colonnes = alphabet[:TAILLE_GRILLE]  # Utilisation des lettres de A à J
    print("   " + "  ".join(colonnes))
    for i, ligne in enumerate(grille):
        print(f"{i+1:2} " + "  ".join(ligne))


# Création et affichage de la grille
grille = creer_grille()
afficher_grille(grille)
