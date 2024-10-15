import string

def generer_grille():
    # Créer les en-têtes de colonnes (A à J)
    colonnes = list(string.ascii_uppercase[:10])  # Liste des lettres de A à J
    
    # Afficher la première ligne avec les lettres (en-têtes horizontales)
    print("    " + "  ".join(f"{col:>3}" for col in colonnes))  # Formater les lettres avec 3 espaces

    # Générer et afficher la grille avec les identifiants de cellule
    for ligne in range(1, 11):  # Pour chaque ligne de 1 à 10
        # Créer et afficher la ligne avec les identifiants de cellule sans zéros inutiles
        print(f"{ligne:2}  " + "  ".join(f"{col}{ligne}" for col in colonnes))

# Appeler la fonction pour afficher la grille
generer_grille()
