#Grille (10x10)
TAILLE_GRILLE = 10 

def creer_grille():
    return [["~" for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]

# Afficher la grille en entière
def afficher_grille(grille):
    colonnes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:TAILLE_GRILLE]
    print("   " + "  ".join(colonnes))
    for i, ligne in enumerate(grille):
        print(f"{i+1:2} " + "  ".join(ligne))

grille = creer_grille()
afficher_grille(grille)







