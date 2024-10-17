# Grille (10x10)
TAILLE_GRILLE = 10

# Liste des lettres de A à J
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(alphabet[:10])  # Affiche les 10 premières lettres, de A à J

# Créer une grille vide 10x10
def creer_grille():
    return [["°" for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]

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

# Suivi des attaques déjà effectuées
attaques = set()

# Fonction pour vérifier si le bateau peut être placé
def placement_valide(grille, taille_bateau, ligne, col, orientation):
    if orientation == 'h':
        if col + taille_bateau > TAILLE_GRILLE:
            return False
        for i in range(taille_bateau):
            if grille[ligne][col + i] != 'O':
                return False
    elif orientation == 'v':
        if ligne + taille_bateau > TAILLE_GRILLE:
            return False
        for i in range(taille_bateau):
            if grille[ligne + i][col] != 'O':
                return False
    return True

# Fonction pour placer le bateau si le placement est valide
def placer_bateau(grille, nom_bateau, taille_bateau, ligne, col, orientation):
    if placement_valide(grille, taille_bateau, ligne, col, orientation):
        if orientation == 'h':
            for i in range(taille_bateau):
                grille[ligne][col + i] = nom_bateau[0]
        elif orientation == 'v':
            for i in range(taille_bateau):
                grille[ligne + i][col] = nom_bateau[0]
        return True
    else:
        return False

# Fonction pour placer tous les bateaux sur la grille
def placer_tous_les_bateaux(grille):
    for nom_bateau, taille_bateau in BATEAUX.items():
        place = False
        while not place:
            orientation = input(f"Orientation du {nom_bateau} (h pour horizontal, v pour vertical) : ")
            ligne = int(input(f"Ligne pour le {nom_bateau} (1-{TAILLE_GRILLE}) : ")) - 1
            col = int(input(f"Colonne pour le {nom_bateau} (1-{TAILLE_GRILLE}) : ")) - 1
            if placer_bateau(grille, nom_bateau, taille_bateau, ligne, col, orientation):
                print(f"{nom_bateau} placé avec succès !\n")
                afficher_grille(grille)
                place = True
            else:
                print(f"Erreur : Le placement du {nom_bateau} est invalide, essayez encore.")

# Fonction pour vérifier si un bateau est coulé
def verifier_si_coule(grille, nom_bateau):
    for ligne in grille:
        if nom_bateau[0] in ligne:
            return False  # Si une partie du bateau reste, il n'est pas coulé
    return True

# Fonction pour gérer l'attaque d'une case
def attaquer_case(grille, ligne, col):
    # Vérifier si la case a déjà été attaquée (Story 7)
    if (ligne, col) in attaques:
        return "Case déjà attaquée, choisissez une autre case."
    
    attaques.add((ligne, col))  # Marquer la case comme attaquée

    # Si un bateau est touché
    if grille[ligne][col] != 'O':  
        nom_bateau = grille[ligne][col]
        grille[ligne][col] = 'X'  # Marquer la case comme touchée
        if verifier_si_coule(grille, nom_bateau):
            return "Coulé"  # Bateau coulé
        else:
            return "Touché"  # Bateau touché mais pas encore coulé
    else:
        grille[ligne][col] = 'M'  # M pour Manqué
        return "Manqué"

# Affichage initial de la grille
grille_adversaire = creer_grille()
placer_tous_les_bateaux(grille_adversaire)

# Boucle pour attaquer des cases (jusqu'à ce que tous les bateaux soient coulés)
def jouer():
    while True:
        afficher_grille(grille_adversaire)
        ligne = int(input(f"Sélectionnez la ligne à attaquer (1-{TAILLE_GRILLE}) : ")) - 1
        col = int(input(f"Sélectionnez la colonne à attaquer (1-{TAILLE_GRILLE}) : ")) - 1
        resultat = attaquer_case(grille_adversaire, ligne, col)
        print(resultat)

# Lancer le jeu avec la possibilité d'attaquer
jouer()
