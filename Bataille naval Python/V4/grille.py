class Grille :

	

	def __init__(self, tailleGrille):
		#Initialise une grille, avec comme paramètre la taille de celle-ci.
		


	def getBateau (self, xBat, yBat): 
		#renvoie le numéro du bateau correspondant aux coordonées xbat et ybat ou 0 si il n'y a pas de bateau
		

	def placerPositionBateau(self, numBat, xBat, yBat):
		#Ajoute le bateau de numéro numBat à la position xbat ybat sur la grille du joueur
		

	def supprimerPosition(self, xBat, yBat):
		#Supprime la position d'un bateau sur la grille 
		

	def envue(self, xTir, yTir): 
		#Renvoie true si il y a un bateau sur les coordonnées x ou y passées en paramètre

	def estDansGrille(self, x, y): 
		#Renvoie true si les coordonnées x et y se trouvent dans la grille

	def estBateau (self, x, y): 
		#Renvoie True si il y a un bateau aux coordonnées indiquées en paramètre 

	def verificationCoordonnees(self, x, y):
		#Renvoie true si la coordonnées est dans la grille et non occupée par un autre bateau
	
	def estValide(self, numBat, x, y):
		#Renvoie true si la verificationCoordonnees et true et si la position est juxtaposée à un bateau de même numéro 

	def estVide(self): 
		#Renvoie True si la grille ne comporte plus aucun bateau

	def tirer(self, xtire, ytire): 
		#Renvoie le resultat du tire (touché, coulé ou en vue)


		
