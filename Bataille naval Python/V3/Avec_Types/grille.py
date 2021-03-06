class Grille :

	#Le type grille permet de regrouper toutes les positions du plateau de chaque joueur. Chaque coordonnées de l'attribut plateau 
	#contient soit 0 si la case est vide ou un numéros de bateau <0 si la case contient un bateau.

	def __init__(self):
		#Initialise une grille vide de taille 20*20 remplit de 0
		self.plateau=[]
		for v in range(21):
			Grille.append([0]*20);

	def estBateau (self, xBat, yBat): 
		#Renvoie True sir le numéros contenu par plateau pour x et y est supérieur à 0

	def getBateau (self, xBat, yBat): 
		#renvoie le numéros du bateau correspondant aux coordonées xbat et ybat ou 0 si il n'y a pas de bateau
		return self.plateau[xBat][yBat]

	def ajouterPosition(self, numBat, xBat, yBat):
		#Ajoute le bateau de numéro numBat à la position xbat ybat sur la grille du joueur 
		return self.plateau[xBat][yBat]=numBat; 

	def suprimerPosition(self, xBat, yBat):
		#Suprimer la position d'un bateau sur la grille en remplaçant le num du bateau par un 0
		return self.plateau[xBat][yBat]=0;

	def envue(self, xTir, yTir): 
		#Renvoie true si bateau sur les coordonnées x ou y passé en paramètre
		envue=bool(False);
		p=int(0);
		while envue==False and p<21:
			if self.plateau[p][yTir]>0 or self.plateau[xTir][p]>0:
				envue=True;
			p=p+1;
				
		return envue


