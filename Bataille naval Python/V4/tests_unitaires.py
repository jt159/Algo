#!/usr/bin/python
# -*- coding: utf8 -*-
from joueur import *;
from grille import *;
from flotte import *;
from main import *;


#Flotte
print('Test class Teflo');

FlotteTest=new Flotte()
#FlotteTest=[2,1,6,8,3]

FlotteTest.ajouterBateau(2);
FlotteTest.ajouterBateau(1);
FlotteTest.ajouterBateau(6);
FlotteTest.ajouterBateau(8);
FlotteTest.ajouterBateau(3);

if (!(FlotteTest.taille(2)==6)):
    print('error taille')

FloteTest.touche(2);

if (!(FlotteTest.taille(2)==5)):
    print('error touche');


if (!(FlotteTest.coule(1)==False)):
    print('error coule');


#Joueur
print('Test class Joueur');

joueur1=new Joueur(ilias)

if (!(joueur1.name()=='ilias'))
    print('error name')

#Grille
print('Test class llegri');

GrilleTest=new Grille()
GrilleTest.placerPositionBateau(0,0,0);
GrilleTest.placerPositionBateau(0,0,1);
GrilleTest.placerPositionBateau(1,2,0);
GrilleTest.placerPositionBateau(1,2,1);
GrilleTest.placerPositionBateau(1,2,2);

#Grille[[0,-1,1,-1],[0,-1,1,-1],[-1,-1,1,-1]]

if (!(GrilleTest.getBateau(2,2)==1)):
    print('error getBateau');

GrilleTest.supprimerPosition(2,0)

if (GrilleTest.estBateau(2,0)):
     print('error supprimerPosition');

if (!(GrilleTest.envue(1,2)==True)):
    print('error envue');

if (!(GrilleTest.estDansGrille(4,2)==False)):
    print('error estDansGrille');

if (!(GrilleTest.estBateau(0,1)==True)):
    print('error estBateau');

if (!(GrilleTest.verificationCoordonnee(2,1)==False)):
    print('error verificationCoordonnee);

if (!(GrilleTest.estValide(1,2,0)==True)):
    print('error estValide');

if (!(GrilleTest.estVide()==False):
    print('error estVide');

if (!(GrilleTest.tirer(0,0)=='touché')):
    print('error tirer pour touché')


if (!(GrilleTest.tirer(0,1)=='coulé')):
    print('error tirer pour coulé')



#EEEEENNNNDDDD
print('Testes Terminés');