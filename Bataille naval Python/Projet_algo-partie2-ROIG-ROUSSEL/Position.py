# coding: utf8
"""
Classe Position

@author Godefroi ROUSSEL
@author Clément ROIG
---------------------------------
"""

class Position:

    def __init__(self,x,y):
	#		int x int --> Position
        self.posX=x;
        self.posY=y;
        self.trouee=False;

	# Créer une position avec deux int compris entre 0 et 20 et touche initilialisée à false.

    def x(self):
	#		Position --> int
        return self.posX;

	# Renvoie l'entier des abscisses.

    def y(self):
	#		Position --> int
        return self.posY;

	# Renvoie l'entier des ordonnées.

    def touche(self):
	#		Position --> boolean
        return self.trouee;

	# Renvoie True si la position est touchée (i.e, on a déjà tiré sur cette position), sinon False.

    def devientTouche(self):
	#		Position --> Position
        self.trouee = True;
        return self;

	# Renvoie la position avec touche passée à True.


"""
# ------------------------------------ #
# ------------ PROPRIETES ------------ #
# ------------------------------------ #

Soit pos = Position(x,y) :

1/	0 <= x(pos) <= 20
2/	0 <= y(pos) <= 20
3/	touche(pos) == false
4/ 	touche(devientTouche(pos)) == true

"""



