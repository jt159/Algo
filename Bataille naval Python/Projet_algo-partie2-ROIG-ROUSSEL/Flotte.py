# coding: utf8
"""
Classe Flotte

@author Godefroi ROUSSEL
@author Clément ROIG
---------------------------------
"""

from Bateau import *

class Flotte:

    def __init__(self):
    #         --> Flotte
        self.listebateaux=[]

    # Renvoie une flotte sans bateau.

    def nbBat(self):
    #         Flotte --> int
        return len(self.listebateaux);

    # Renvoie le nombre de bateau dans la flotte.

    def bateau(self,numBat):
    #         Flotte --> Bateau     /!\ Nous avons ajouter cette fonction qui renvoie un bateau précisement
        return self.listebateaux[numBat-1]

    def bateaux(self):
    #         Flotte --> [Bateau]
        return self.listebateaux

    # Renvoie le tableau des bateaux présents dans la flotte.

    def ajouterBateau(self, bateau):
    #         Flotte x Bateau --> Flotte
        for j in range(0,bateau.taille()):
            for i in range(0,self.nbBat()):
                for k in range(0,self.bateau(i).taille()):
                    if (self.bateau(i).position(k).x()==bateau.position(j).x() and self.bateau(i).position(k).y()==bateau.position(j).y()):
                        return ValueError("Le bateau chevauche un bateau existant");

        return self.listebateaux.append(bateau);



    # Ajoute un bateau à la flotte si aucune position n'est déjà occupée par un autre bateau
    # présent dans la flotte, sinon renvoie la flotte sans ajouter le bateau.

    def nbBatCoule(self):
    #         Flotte --> int
        n=0;
        for i in range(0, self.nbBat()):
            if self.bateau(i).estCoule():
                n=n+1;
        return n;


    # Renvoie le nombre de bateau(x) coulé(s).

    def flotteDetruite(self):
    #         Flotte --> bool
        return self.nbBatCoule()==self.nbBat();

    # Renvoie True si tous les bateaux de la flotte sont coulés, sinon False.

    def verifTir(self,pos):
    #         Flotte x Position --> [int](2)
        res=[3,-1];
        for i in range(0,self.nbBat()):
                for k in range(0,self.bateau(i).taille()):
                    if (self.bateau(i).position(k).x()==pos.x() and self.bateau(i).position(k).y()==pos.y()):
                        if not self.bateau(i).position(k).touche():
                            res=[1,i];
                            self.bateau(i).position(k).devientTouche()
                    elif(self.bateau(i).position(k).x()==pos.x() or self.bateau(i).position(k).y()==pos.y()):
                        if res==[3,-1]:
                            res=[2,-1];



        return res;
    """
    La position doit être valide et :

    - si le tir "touche" une position d'un bateau non-touchée au préalable
                => renvoie [1] et [indice du bateau touché]
    - si une position non-touchée d'un bateau se trouve sur la même ligne ou colonne que le tir
     ("en vue")
                => renvoie [2] et [-1]
    - sinon le tir est "à l'eau"
                => renvoie [3] et [-1]
    """


    """
    # ------------------------------------ #
    # ------------ PROPRIETES ------------ #
    # ------------------------------------ #

    Soit flotte = Flotte() :
    1/      nbBat(flotte) == 0 (quand construit) et nbBat(flotte) >= 0 (toujours valable)
    2/      nbBatCoule(flotte) >= 0 et nbBatCoule(flotte) <= nbBat(flotte)

    Soit flotte = Flotte() et bat = Bateau(taille, pos, dir) et ajouterBateau(flotte,bat) :
    3/     flotteDetruite(flotte) == False
    4/     Si estCoule(bat) alors nbBatCoule(flotte) == 1
    5/     Si nbBatCoule(flotte) == nbBat(flotte) alors flotteDetruite(flotte) == True
    """
