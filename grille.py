# Taille de la grille
TAILLE_GRILLE = 10

def generer_colonnes():
    """Génère les lettres de A à J pour les colonnes"""
    return [chr(i) for i in range(65, 65 + TAILLE_GRILLE)]  # ['A', 'B', 'C', ..., 'J']

def afficher_en_tete(colonnes):
    """Affiche les lettres d'en-tête (A, B, C, ...) avec un espacement fixe"""
    print("    " + "    ".join(colonnes))

def afficher_lignes(colonnes):
    """Affiche les lignes avec les cellules identifiables (A1, B2, ...)"""
    for ligne in range(1, TAILLE_GRILLE + 1):
        print(f"{ligne:2}  " + "   ".join(f"{col}{ligne}" for col in colonnes))

def afficher_grille():
    """Affiche toute la grille avec en-tête et lignes"""
    colonnes = generer_colonnes()  # Génère les colonnes de A à J
    afficher_en_tete(colonnes)     # Affiche les lettres des colonnes
    afficher_lignes(colonnes)      # Affiche les lignes numérotées

# Appel de la fonction pour afficher la grille
afficher_grille()
