import string

def afficher_grille():
    # Création de la première ligne avec les lettres A à J pour l'en-tête
    lettres = list(string.ascii_uppercase[:10])  # Liste des lettres de A à J

    # Affichage de l'en-tête (les lettres pour les colonnes)
    print("    " + "  ".join([f"{lettre:3}" for lettre in lettres]))  # Espaces pour alignement

    # Affichage des lignes de la grille avec les numéros à gauche et les cellules vides identifiables
    for i in range(1, 11):
        ligne = []  # Liste pour stocker chaque cellule
        for j in range(10):
            case = f"{lettres[j]}{i}"  # Combinaison lettre + numéro de ligne (ex: A1, B2, etc.)
            ligne.append(f"{case:<4}")  # Format pour s'assurer que chaque case occupe 4 espaces
        print(f"{i:2}  " + " ".join(ligne))  # Affichage de la ligne avec les cellules identifiables

# Appel de la fonction pour afficher la grille vide
afficher_grille()


def afficher_grille(grille):
    for ligne in grille:
        print(" ".join(ligne))

def placer_bateau(grille, taille, position):
    x, y = position
    if (x < 0 or x >= len(grille)) or (y < 0 or y >= len(grille[0])):
        print("Position invalide !")
        return False
    
    # Vérifie si le bateau peut être placé horizontalement
    if y + taille <= len(grille[0]):
        for j in range(y, y + taille):
            if grille[x][j] != ".":  # Si la case est déjà occupée
                print("Emplacement déjà pris !")
                return False
        # Placer le bateau
        for j in range(y, y + taille):
            grille[x][j] = "B"  # B pour bateau
        return True
    else:
        print("Emplacement hors limites !")
        return False

# Exemple d'utilisation
grille = [["." for _ in range(10)] for _ in range(10)]  # Crée une grille 10x10 vide
print("Grille initiale :")
afficher_grille(grille)

# Essayer de placer un bateau
if placer_bateau(grille, 3, (2, 1)):
    print("Bateau placé avec succès !")
else:
    print("Échec du placement.")

print("Grille après placement :")
afficher_grille(grille)
