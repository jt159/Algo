# coding: utf8
"""
Classe Bateau

@author Godefroi ROUSSEL
@author Clément ROIG
---------------------------------
"""
from Position import *

class Bateau:

    def __init__(self, taille, dir, pos):
	#		int x int x position --> Bateau
        self.positions=[];
        self.positions.append(pos);

        if dir==0:
            if (pos.y()-(taille-1)<0):
                raise ValueError("Le Bateau sort de la grille ! ");
            else:
                for i in range (1,taille):
                    posi=Position(pos.x(),pos.y()-i);
                    self.positions.append(posi);
        elif dir == 1:
            if (pos.x()-(taille-1)<0):
                raise ValueError("Le Bateau sort de la grille ! ");
            else:
                for i in range (1, taille):
                    posi=Position(pos.x()-i,pos.y());
                    self.positions.append(posi);
        elif dir == 2:
            if (pos.y()-(taille-1)>20):
                raise ValueError("Le Bateau sort de la grille ! ");
            else:
                for i in range (1, taille):
                    posi=Position(pos.x(),pos.y()+i);
                    self.positions.append(posi);
        elif dir == 3:
            if (pos.x()-(taille-1)>20):
                raise ValueError("Le Bateau sort de la grille ! ");
            else:
                for i in range (1, taille):
                    posi=Position(pos.x()+i,pos.y());
                    self.positions.append(posi);
        else:
             raise ValueError("Direction invalide ! ");

	"""
	Place le bateau en partant de la position passée en paramètre et en se dirigeant vers
	la direction souhaitée (0 pour le bas, 1 pour la gauche, 2 pour le haut, 3 pour la droite)
	en fonction de la taille du bateau (compris entre 1 et 4).

	On se place dans le "repère" suivant :

		y
	    ^
		|
		|
		|
		|
	  0-|------------> x
		0

	On vérifie si les positions calculées du bateau sont comprises entre 0 et 20.
	Sinon, on renvoie une erreur et on annule la création du bateau.
	"""

    def taille(self):
        # 		Bateau --> int
        return len(self.positions);


	# Renvoie la taille du bateau (comprise entre 1 et 4).

    def position(self,numpos):
	#		Bateau --> [Position]
        return self.positions[numpos];

    def positions(self):
	#		Bateau --> [Position]
        return self.positions;

	# Renvoie le tableau des Positions du bateau.

    def nbPosTouche(self):
	#		Bateau --> int
        nbpostouche = 0;
        for i in range (0, self.taille()):
            if self.position(i).touche() == True :
                nbpostouche = nbpostouche+1;
        return nbpostouche;

	# Renvoie le nombre de position touché sur le bateau.

    def touchePosition(self,pos):
	#		Bateau x Position --> Bateau
        existe = False;
        i = 0;
        while (existe == False and i<self.taille()):
            if pos == self.position(i) :
                existe = True;
                self.position(i).devientTouche();
            i=i+1;
        return self;

	# pos doit être une Position du bateau. Renvoie le Bateau avec cette position touchée.

    def estCoule(self):
	# 		Bateau --> boolean
        return self.nbPosTouche()==self.taille();

	# Renvoie True si nbPosTouche() == taille() sinon False.


	"""
	# ------------------------------------ #
	# ------------ PROPRIETES ------------ #
	# ------------------------------------ #

	Soit bat = Bateau(taille, dir, pos) :

	1/ 	1 <= taille(bat) <= 4
	2/ 	nbPosTouche(bat) == 0 et nbPosTouche(bat) <= taille(bat)
	3/	estCoule(bat) == false
	4/ 	nbPostTouche(touchePosition(bat)) == nbPosTouche(bat) + 1
	5/	(nbPosTouche(bat) == taille(bat))
		implique
		estCoule(bat) == True

	"""
