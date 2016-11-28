#!/usr/bin/python
# -*- coding: utf8 -*-
class Grille :



	def __init__(self, tailleGrille):
		#Initialise une grille, avec comme paramètre la taille de celle-ci.



	def getBateau (self, xBat, yBat):
		#Données: Grille et coordonnées étudiées
		#Pré-conditions: xBat:int, yBat:int
		#Resultat: Renvoie le numéro du bateau correspondant aux coordonnées xBat, yBat, ou renvoie 0 s'il n'y pas de bateau
		#Post-conditions: numBat:int


	def placerPositionBateau(self, numBat, xBat, yBat):
		#Données: Grille, numéro du bateau à placer, et coordonnées indiquant où on veut le placer
		#Pré-conditions: numBat:int, xBat:int, yBat:int
		#Resultat: Ajoute le bateau de numéro numBat à la position (xBat,yBat) sur la grille du joueur et renvoie la grille
		#Post-conditions:  Grille


	def supprimerPosition(self, xBat, yBat):
		#Données: Grille et cordonnées (xBat,yBat)
		#Pré-conditions: xBat:int, yBat:int , on suppose vérfifiée le fait que la postion contient un bateau
		#Resultat: Supprime la position indiquée par les coordonnées (xBat,yBat) et renvoie la grille modifiée
		#Post-conditions: Grille


	def envue(self, xTir, yTir):
		#Données: Grille et coordonnées(xTir,yTir)
		#Pré-conditions: xTir:int, yTir:int
		#Resultat:Renvoie True si il y a un bateau sur la coordonnée xTir ou sur la coordonnée yTir, renvoie False sinon
		#Post-conditions: bool


	def estDansGrille(self, x, y):
		#Données: Grille et coordonnées (x,y)
		#Pré-conditions: x:int, y:int
		#Resultat: Renvoie True si la position indiquée par (x,y) se trouve dans la grille, renvoie False sinon
		#Post-conditions: bool

	def estBateau (self, x, y):
		#Données: Grille et coordonnées (x,y)
		#Pré-conditions: x:int, y:int
		#Resultat: Renvoie True s'il y a un bateau aux coordonnées (x,y) indiquées, renvoie False sinon
		#Post-conditions: bool

	def verificationCoordonnees(self, x, y):
		#Données: Grille et coordonnées (x,y)
		#Pré-conditions: x:int, y:int
		#Resultat: Renvoie True si la position indiquée indiquée par (x,y) est dans la grille et non-occupée par un bateau, renvoie False sinon
		#Post-conditions: bool

	def estValide(self, numBat, x, y):
		#Données: Grille, numéro du bateau, et coordonnées (x,y)
		#Pré-conditions: nuùBat:int, x:int, y:int
		#Resultat: Renvoie True si verificationCoordonnees est true et si la position indiquée par (x,y) est juxtaposée à un bateau de même numéro et que toutes les autres position de ce bateau sont sur la même ligne ou la même colonne, renvoie False sinon
		#Post-conditions: bool

	def estVide(self):
		#Données: Grille
		#Pré-conditions: ---
		#Resultat: Renvoie True si la grille ne comporte plus aucun bateau, renvoie False sinon
		#Post-conditions: bool

	def tirer(self, xTir, yTir):
		#Données: Grille et coordonnées (xTir,yTir)
		#Pré-conditions: xTir:int, yTir:int
		#Resultat: Renvoie le résultat du tir (en vue, touché ou coulé)
		#Post-conditions: resultatTir:string



