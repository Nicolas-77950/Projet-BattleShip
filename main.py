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




# Création et affichage de la grille de jeux
grille = creer_grille()
afficher_grille(grille)


# Dictionnaire avec les bateaux et leur taille
BATEAUX = {
    "Porte-avions": 5,
    "Croiseur": 4,
    "Contre-torpilleur": 3,
    "Sous-marin": 3,
    "Torpilleur": 2
}




# Fonction pour vérifier si le bateau peut être placé
def placement_valide(grille, taille_bateau, ligne, col, orientation):
    # Si orientation horizontale, vérifie que le bateau ne dépasse pas à droite
    if orientation == 'h':
        if col + taille_bateau > TAILLE_GRILLE:
            return False
        # Vérifie qu'il n'y a pas déjà un bateau sur le chemin
        for i in range(taille_bateau):
            if grille[ligne][col + i] != 'O':
                return False
    # Si orientation verticale, vérifie que le bateau ne dépasse pas en bas
    elif orientation == 'v':
        if ligne + taille_bateau > TAILLE_GRILLE:
            return False
        # Vérifie qu'il n'y a pas déjà un bateau sur le chemin
        for i in range(taille_bateau):
            if grille[ligne + i][col] != 'O':
                return False
    return True


# Fonction pour placer le bateau si le placement est valide
def placer_bateau(grille, nom_bateau, taille_bateau, ligne, col, orientation):
    if placement_valide(grille, taille_bateau, ligne, col, orientation):
        # Place le bateau horizontalement ou verticalement
        if orientation == 'h':
            for i in range(taille_bateau):
                grille[ligne][col + i] = nom_bateau[0]  # Utilise la première lettre du bateau
        elif orientation == 'v':
            for i in range(taille_bateau):
                grille[ligne + i][col] = nom_bateau[0]
        return True
    else:
        return False




# Fonction pour placer tous les bateaux sur la grille
def placer_tous_les_bateaux(grille):
    # Pour chaque bateau dans le dictionnaire BATEAUX
    for nom_bateau, taille_bateau in BATEAUX.items():
        place = False
        while not place:
            # Demande l'orientation du bateau (horizontale ou verticale)
            orientation = input(f"Orientation du {nom_bateau} (h pour horizontal, v pour vertical) : ")




            # Demande les coordonnées de départ (ligne et colonne)
            ligne = int(input(f"Ligne pour le {nom_bateau} (1-{TAILLE_GRILLE}) : ")) - 1
            col = int(input(f"Colonne pour le {nom_bateau} (1-{TAILLE_GRILLE}) : ")) - 1




            # Tente de placer le bateau
            if placer_bateau(grille, nom_bateau, taille_bateau, ligne, col, orientation):
                print(f"{nom_bateau} placé avec succès !\n")
                afficher_grille(grille)  # Affiche la grille après placement
                place = True  # Bateau placé correctement, on sort de la boucle
            else:
                print(f"Erreur : Le placement du {nom_bateau} est invalide, essayez encore.")



# Place tous les bateaux en demandant à l'utilisateur les coordonnées.
placer_tous_les_bateaux(grille)
