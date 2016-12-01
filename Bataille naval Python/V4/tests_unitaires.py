#!/usr/bin/python
# -*- coding: utf8 -*-
from joueur import *;
from grille import *;
from flotte import *;
from main import *;

#===============================================================
#--------------------------FLOTTE-------------------------------


#---------------------------creation_flotte----------------------
def test_creation_flotte():
    try:
        FlotteTest=Flotte();
        return true;

    except:
        return false;


#FlotteTest=[2,1,6,8,3]

#-------------------------------ajouter_bateau---------------------
def test_ajouter_bateau():
    try:
        FlotteTest.ajouterBateau(2);
        return true;
    except:
        return false;




#-----------------------------taille---------------------
def test_taille():
    FlotteTest.ajouterBateau(1);
    FlotteTest.ajouterBateau(6);
    FlotteTest.ajouterBateau(8);
    FlotteTest.ajouterBateau(3);
    if (FlotteTest.taille(2)!=6):
        return false;
    else :
        return true;

#--------------------------touche------------------------------
def test_touche():
    FlotteTest.touche(2);

    if (FlotteTest.taille(2)!=5):
        return false;
    else :
        return true;


#-----------------------------coule_false----------------
def test_coule_false():
    if (FlotteTest.coule(1)!=False):
        return false;
    else :
        return true;


#--------------------------------coule_True---------------
def test_coule_true():
    FlotteTest.touche(2);
    FlotteTest.touche(2);
    FlotteTest.touche(2);
    FlotteTest.touche(2);
    FlotteTest.touche(2);

    if (FlotteTest.coule(1)!=True):
        return false;
    else :
        return true;







#==================================================================
#---------------------------JOUEUR------------------------------
#Joueur


def test_Joueur():
    try:
        joueur1=Joueur(ilias)
        return true;
    except:
        return false;


#---------------------------name--------------------

def test_name():
    if (joueur1.name()!='ilias'):
        return false;
    else :
        return true;








#==================================================================
#---------------------------GRILLE------------------------------
#Grille





#---------------------------Création Grille-------------------------

def test_grille():
    try:
        GrilleTest=Grille()
        return true;
    except:
        return false;



#-------------------------AjouterPositionBateau-------------------

def test_placerPositionBateau():
    try:
        GrilleTest.placerPositionBateau(0,0,0);
        return true;
    except:
        return false;


def test_placerPositionBateau_trop_eloigne():
    try:
        GrilleTest.placerPositionBateau(0,0,2);
        return false;
    except:
        return true;




#-------------------------GetBateau-------------------

GrilleTest.placerPositionBateau(0,0,1);
GrilleTest.placerPositionBateau(1,2,0);
GrilleTest.placerPositionBateau(1,2,1);
GrilleTest.placerPositionBateau(1,2,2);

#Grille[[0,-1,1,-1],[0,-1,1,-1],[-1,-1,1,-1]]

def test_getBateau():
    if (GrilleTest.getBateau(2,2)!=1):
        return false;
    else :
        return true;





#-------------------------supprimerPosition-------------------


def test_supprimerPosition():
    GrilleTest.supprimerPosition(2,0)

    if (GrilleTest.estBateau(2,0)==True):
         return false;
    else :
        return true;





#------------------------------envue-----------------------

def test_envue():
    if (GrilleTest.envue(1,2)!=True):
        return false;
    else :
        return true;




#-------------------------estDansGrille-------------------

def test_estDansGrille():
    if (GrilleTest.estDansGrille(4,2)!=False):
        return false;
    else :
        return true;





#-------------------------estBateau-------------------

def test_estBateau():
    if (GrilleTest.estBateau(0,1)!=True):
        return false;
    else :
        return true;





#-------------------------verificationCoordonées-------------------

def test_verificationCoordonnee():
    if (GrilleTest.verificationCoordonnee(2,1)!=False):
        return false;
    else :
        return true;





#------------------------------estValide -------------------

def test_estValide():
    if (GrilleTest.estValide(1,2,0)!=True):
        return false;
    else :
        return true;




#----------------------------estVide------------------------

def test_estVide():
    if (GrilleTest.estVide()!=False):
        return false;
    else :
        return true;



#----------------------------Tirer-----------------------

def test_tirer():
    if (GrilleTest.tirer(0,0)!='touché'):
        return false;
    else :
        return true;


def test_coule():
    if (GrilleTest.tirer(0,1)!='coulé'):
        return false;
    else :
        return true;



#EEEEENNNNDDDD
