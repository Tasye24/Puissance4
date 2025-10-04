import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Constantes
# Activer pour vérifier l'intégrité des fonctions
DEBUG_MODE = 1

col = 7
line = 6

# Initialisation de la grille
def grille_init()->list:
    grille = [0] * line
    for i in range(line):
        grille[i] = [0] * col
    return grille

# On affiche la grille de manière lisible dans le terminal
def affiche_grille(tab: list)->None:
    print(f"PUISSANCE {bcolors.FAIL}4{bcolors.ENDC}™ \n")
    
    for i in range(len(tab)):
        line = f"{bcolors.OKBLUE}|{bcolors.ENDC}"
        for j in range(len(tab[i])):
            if tab[i][j] == 1:
                line += f"{bcolors.FAIL}●{bcolors.ENDC}"
            elif tab[i][j] == 2:
                line += f"{bcolors.WARNING}●{bcolors.ENDC}"
            else:
                line += " "
            line += f"{bcolors.OKBLUE}|{bcolors.ENDC}"
        print(line)

# On vérifie que la dernière ligne de la colonne choisit par le joueur est libre
def colonne_libre(tab: list, colonne:int, joueur:int)->bool:
    if tab[0][colonne-1] != 0:
        print(f"la colonne {colonne} est pleine")
        tour_joueur(tab, joueur)
        return False
    return True

# On place le jeton du joueur sur la grille
def place_jeton(tab: list, colonne: int, joueur:int)->None:
    stop = False
    for i in range(len(tab)-1, -1, -1):
        # si la ligne la plus basse de la colonne est dispo:
        if tab[i][colonne-1] == 0 and stop != True:
            tab[i][colonne-1] = joueur
            stop = True

# HRZ VER DIA en fonction de JOUEUR

# On vérifie si le joueur possède une ligne de 4
def horizontale(tab: list, joueur: int)->bool:
    for i in range(line):
        for j in range(4):
            if tab[i][j] == tab[i][j + 1] == tab[i][j + 2] == tab[i][j + 3] & tab[i][j] == joueur:
                return True
    return False

# On vérifie si le joueur possède une colonne de 4
def verticale(tab: list, joueur: int)->bool:
    for i in range(3):
        for j in range(7):
            if tab[i][j] == tab[i + 1][j] == tab[i + 2][j] == tab[i + 3][j] & tab[i][j] == joueur:
                return True
    return False
                
# On vérifie si le joueur possède une diagonale descendante de 4 \
def diagonale(tab: list, joueur:int)->bool:
    for i in range(3):
        for j in range(2):
            if tab[i][j] == tab[i + 1][j + 1] == tab[i + 2][j + 2] == tab[i + 3][j + 3] & tab[i][j] == joueur:
                return True
    return False

# On vérifie si le joueur possède une ascendante de 4 /
def diagonale2(tab: list, joueur:int)->bool:
    for i in range(3, 6):
        for j in range(0, 2):
            if tab[i][j] == tab[i - 1][j + 1] == tab[i - 2][j + 2] == tab[i - 3][j + 3]  & tab[i][j] == joueur:
                return True
    return False

# On vérifie si le joueur un gagné
def gagne(tab:list, joueur:int)->bool:
    return (horizontale(tab, joueur) or verticale(tab, joueur) or diagonale(tab, joueur) or diagonale2(tab, joueur))

# On demande au joueur de choisir sa colonne
def choix_colonne(tab:list, joueur:int)->bool:
    if joueur == 1:
        player = f"{bcolors.FAIL}●{bcolors.ENDC}"
    else:
        player = f"{bcolors.WARNING}●{bcolors.ENDC}"
    print(f"\nJoueur {player} ({joueur}) c'est à vous !")
    
    colonne = int(input("Choisissez une colonne (1-7): "))
 
    clear()

    if colonne_libre(tab, colonne, joueur) == False:
        tour_joueur(tab, joueur)
    return colonne

# On effectue un tour pour le joueur
def tour_joueur(tab:list, joueur:int)->None:
    #affiche_grille(tab)
    colonne = choix_colonne(tab, joueur)
    place_jeton(tab, colonne, joueur)

# On vérifie l'égalité
def egalite(tab:list)->bool:
    # initialisation du compteur
    c = 0
    for i in range(7):
        if tab[0][i] != 0:
            c += 1
    if c == 7:
        return True
    return False

# Fonction principal du permettant le jeu
def jouer(tab: list, tour:int)->bool:
    # Par défaut on continue la partie
    continuer = True
    
    # On affiche la grille pour l'utilisateur
    affiche_grille(tab)

    # C'est au tour du 1er joueur si le tour est pair sinon le 2e joueur
    if tour % 2 == 0:
        joueur = 1
    else:
        joueur = 2
    
    tour_joueur(tab, joueur)

    if gagne(tab, joueur):
        print(f"Le joueur {joueur} a gagné")
        
          # Le joueur a gagné on arret la partie
        continuer = False
    elif egalite(tab):
        print(f"Egalité")
        
          # On arrete la partie car il ne peut pas y avoir de gagner la grille est complète
        continuer = False
    
    return continuer


# Permet d'effacer le terminal
def clear()->None:
    # On ajoute n lignes pour ne plus voir les precedentes lignes (si le clear ne marche pas)
    print(
        "\n"*150
    )
    # on clear le terminal via une commande cls pour Windows® et clear pour Ubuntu, MacOs® etc...
    os.system('cls' if os.name == 'nt' else 'clear')
    

'programme principal'

grille = grille_init()

clear()

# Fonction de debuggage permettant de vérifier si le programme fonctionne
def debug()->None:
    # Définitions de variables pour des cas précis avec un résultat attendu
    grid_diagonale2 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]
    grid_diagonale = [[0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    grid_hrz = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0]]
    grid_vert = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0]]
    
    #affiche_grille(grid_diagonale)
    #affiche_grille(grid_diagonale2)

    #print(diagonale(grid_diagonale, 1))
    
    # on s'attend a ce que les fontions renvoient true sinon on affiche un message d'erreur
    if diagonale(grid_diagonale, 1) != True:
        print(f"{bcolors.FAIL}Erreur `diagonale()` ne marche pas{bcolors.ENDC}")
    if horizontale(grid_hrz, 1) != True:
        print(f"{bcolors.FAIL}Erreur `horizontale()` ne marche pas{bcolors.ENDC}")
    if verticale(grid_vert, 1) != True:
        print(f"{bcolors.FAIL}Erreur `verticale()` ne marche pas{bcolors.ENDC}")
    if diagonale2(grid_diagonale2, 1) != True:
        print(f"{bcolors.FAIL}Erreur `diagonale2()` ne marche pas{bcolors.ENDC}")
    

if DEBUG_MODE:
    debug()


# On initialise le compteur de tours
n = 0

# 
continuer = True

#
while (continuer):
    
    continuer = jouer(grille, n)

    # On incrémente le conmpteur de tours
    n += 1


"========="

"""algorithme

fonction grille_init()->list:
variables
    param
        /
    internes
        entier: i
    en sortie
        tableau entier: grille
debut

grille <- [0,0,0,0,0,0]
pour i variant de 0 à 6 exclus
    grille[i] <- [0,0,0,0,0,0,0]
retourne grille
fin

fonction afficher_grille(tab: list)->None:
variables
    param
        tableau entier: tab
    internes
        entier: i, j
        string: line
    en sortie
        /
debut

pour i variant de 0 à len(tab) exclus
    line <- "|"
    pour j variant de 0 à len(tab[i]) exclus par pas de 1
        si tab[i][j] = 1 alors
            line <- line + "X"
        sinon_si tab[i][j] = 2 alors
            line <- line + "O"
        sinon
            line <- line + " "
        fin_si

        line <- line + "|"
    print(line)
fin

fonction colonne_libre(tab, colonne, joueur)->bool:
variables
    param
        tableau entier: tab
        entier: colonne, joueur
    internes
        /
    en sortie
        /
debut

    si tab[0][colonne-1] != 0 alors
        print("la colonne {colonne} est pleine")
        tour_joueur(tab, joueur)
        
        retourner False
    fin_si

    retourner True

fin

fonction place_jeton(tab, colonne, joueur)->None:
variables
    param
        tableau entier: tab
        entier: colonne, joueur
    internes
        bool: stop
        entier: i
    en sortie
        tableau entier: grille
debut

stop <- False
pour i variant de len(tab)-1 à 0 par pas de -1
    si tab[i][colonne-1] = 0 et stop != True alors
        tab[i][colonne-1] <- joueur
        stop <- True
    fin_si

fin

fonction horizontale(tab, joueur)->bool:
variables
    param
        tableau entier: tab
        entier: joueur
    internes
        entier: i, j
    en sortie
        /
debut

pour i variant de 0 à 6 par pas de 1
    pour j variant de 0 à 4 par pas de 1
        si tab[i][j] = tab[i][j + 1] = tab[i][j + 2] = tab[i][j + 3] & tab[i][j] = joueur alors
            renvoyer True
        fin_si
renvoyer False

fin

fonction verticale(tab, joueur)->bool:
variables
    param
        tableau entier: tab
        entier: joueur
    internes
        entier: i, j
    en sortie
        /
debut

pour i variant de 0 à 3 par pas de 1
    pour j variant de 0 à 4 par pas de 1
        si tab[i][j] = tab[i][j + 1] = tab[i][j + 2] = tab[i][j + 3] & tab[i][j] = joueur alors
            renvoyer True
        fin_si
renvoyer False

fin

fonction diagonale(tab, joueur)->bool:
variables
    param
        tableau entier: tab
        entier: joueur
    internes
        entier: i, j
    en sortie
        /
debut

pour i variant de 0 à 3 exclus par pas de 1
    pour j variant de 0 à 2 exclus par pas de 1
        si tab[i][j] = tab[i + 1][j + 1] = tab[i + 2][j + 2] = tab[i + 3][j + 3] & tab[i][j] = joueur alors
            renvoyer True
        fin_si
renvoyer False

fin

fonction diagonale2(tab, joueur)->bool:
variables
    param
        tableau entier: tab
        entier: joueur
    internes
        entier: i, j
    en sortie
        /
debut

pour i variant de 3 à 6 exclus par pas de 1
    pour j variant de 0 à 2 exclus par pas de 1
        si tab[i][j] = tab[i - 1][j + 1] = tab[i - 2][j + 2] = tab[i - 3][j + 3] & tab[i][j] = joueur alors
            renvoyer True
        fin_si
renvoyer False
fin


fonction choix_colonne(tab, joueur)->bool:
variables
    param
        tableau entier: tab
        entier: joueur
    internes
        /
    en sortie
        /
debut

si joueur = 1 alors
    player <- "X"
sinon
    player <- "O"
fin_si
print("Joueur \"{player}\" ({joueur}) c'est à vous !")

afficher("Choisissez une colonne: ")
colonne <- lire("")

clear()

si colonne_libre(tab) alors
    tour_joueur(tab, joueur)
fin_si

retourner colonne

fin


fonction gagne(tab, joueur)->bool:
variables
    param
        tableau entier: tab
        entier: joueur
    internes
        /
    en sortie
        /
debut

si horizontale(tab, joueur) = True or verticale(tab, joueur) = True or diagonale(tab, joueur) = True or diagonale2(tab, joueur) = True alors
    retourner True
retourner False
fin_si

fin


fonction tour_joueur(tab, joueur)->None:
variables
    param
        tableau entier: tab
        entier: joueur
    internes
        /
    en sortie
        /
debut

colonne <- choix_colonne(tab, joueur)
place_jeton(tab, colonnne, joueur)

fin

fonction egalite(tab, joueur)->bool:
variables
    param
        tableau entier: tab
        entier: joueur
    internes
        entier: i
    en sortie
        /
debut

pour i variant de 0 à 6 exclus par pas de 1
    si tab[0][i] != 0 alors
        retourne True
    fin_si
retourne False

fin

fonction joueur(tab, tour)->bool:
variables
    param
        tableau entier: tab
        entier: tour
    internes
        entier: joueur
        bool: continuer
    en sortie
        /
debut

continuer <- True

afficher_grille(tab)

si tour % 2 = 0 alors
    joueur <- 1
sinon
    joueur <- 2
fin_si

tour_joueur(tab, joueur)

si gagne(tab, joueur) alors
    print("Le joueur {joueur} a gagné")
    continuer <- False
sinon_si egalite(tab) alors
    print("Egalité)
    continuer <- False
fin_si
retourner continuer

fin

fonction clear()->None
variables
    /
debut

print("\n"*150)

os.system("cls" si os.name = "nt" sinon "clear")

fin

fonction debug()->None
...

programme principal
variables
    en entrée
        /
    intnerne
        bool: DEBUG_MODE, continuer
        entier: n
    en sortie
        /
debut

n <- 0
continuer <- True

tant que continuer alors
    continuer <- jouer(grille, n)
    n = n + 1

fin

"""