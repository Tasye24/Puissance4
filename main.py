import os

col = 7
line = 6

def grille_init():
	grille = [0] * line
	for i in range(line):
		grille[i] = [0] * col
	return grille

def affiche_grille(tab):
	"""
	for i in range(6):
		for j in range(7):
			if tab[i][j] == 1:
				#tab[i][j] = "O"
				print("0")
			elif tab[i][j] == 2:
				#tab[i][j] = "X"
				print("X")
			else:
				#tab[i][j] = ""
				print("E")
	"""
	#return tab

	for i in range(len(tab)):
		line = "|"
		for j in range(len(tab[i])):
			if tab[i][j] == 1:
				line += "X"
			elif tab[i][j] == 2:
				line += "O"
			else:
				line += " "
			line += "|"
		#line += "\n"
		#line += "-" * len(tab[i])*2
		print(line)

# True if empty else False
def colonne_libre(tab, colonne)->bool:
	if tab[0][colonne-1] != 0:
		print(f"la colonne {colonne} est pleine")
		tour_joueur(tab, joueur)
		return False
	return True



def place_jeton(tab, colonne, joueur):
	stop = False
	for i in range(len(tab)-1, -1, -1):
		# si la ligne la plus basse de la colonne est dispo:
		#if tab[i][i]
		if tab[i][colonne-1] == 0 and stop != True:
			tab[i][colonne-1] = joueur
			stop = True


# HRZ VER DIA en fonction de JOUEUR

def horizontale(tab, joueur):
	for i in range(line):
		for j in range(4):
			if tab[i][j] == tab[i][j + 1] == tab[i][j + 2] == tab[i][j + 3] & tab[i][j] != 0:
				return True
				print("gagné")


def verticale(tab, joueur):
	for i in range(3):
		for j in range(7):
			if tab[i][j] == tab[i + 1][j] == tab[i + 2][j] == tab[i + 3][j] & tab[i][j] != 0:
				print("gagné vert")
				return True
				


def diagonale(tab, joueur):
	for i in range(3):
		for j in range(2):
			if tab[i][j] == tab[i + 1][j + 1] == tab[i + 2][j + 2] == tab[i + 3][j + 3]  & tab[i][j] != 0:
				print("gagné dig")
				return True


def diagonale2(tab, joueur):
	for i in range(3, 6):
		for j in range(0, 2):
			if tab[i][j] == tab[i - 1][j + 1] == tab[i - 2][j + 2] == tab[i - 3][j + 3]  & tab[i][j] != 0:
				return True
				print("gagné")


def gagne(tab, joueur):
	if horizontale(tab, joueur) == True or verticale(tab, joueur) == True or diagonale(tab, joueur) == True or diagonale2(tab, joueur) == True:
		return True
	return False

def choix_colonne(tab, joueur):
	if joueur == 1:
		player = "X"
	else:
		player = "O"
	print(f"Joueur \"{player}\" ({joueur}) c'est à vous !")
	
	colonne = int(input("Choisissez une colonne: "))
 
	clear()

	if colonne_libre(tab, colonne) == False:
		tour_joueur(tab, joueur)
	return colonne

def tour_joueur(tab, joueur):
    affiche_grille(tab)
    colonne = choix_colonne(tab, joueur)
    place_jeton(tab, colonne, joueur)
    if gagne(tab, joueur):
        print(f"Le joueur {joueur} a gagné")
        return False ## continuer: false -> stops
    return True


def egalite(tab):
	for i in range(6):
		for j in range(7):
			if tab[i][j] == (1 or 2):
				return False
	return True


def jouer(tab):
	joueur = int(input("Choisissez un joueur"))
	while gagne(tab, joueur) == False and egalite(tab) == False:
		tour_joueur(tab, joueur)
		if joueur == 1:
			joueur = 2
		else:
			joueur = 1
	if egalite(tab):
		print("Egalité")


def clear()->None:
	os.system('cls' if os.name == 'nt' else 'clear')
	

'programme principal'

global grille

grille = grille_init()
clear()

n = 0
continuer = True
while (continuer):
	if n % 2 == 0:
		joueur = 1
	else:
		joueur = 2
	continuer = tour_joueur(grille, joueur)
	n = n + 1