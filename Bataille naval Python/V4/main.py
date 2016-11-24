#!/usr/bin/python
# -*- coding: utf8 -*-
from joueur import *;
from grille import *;
from flotte import *;


print("========== Bienvenue dans la Bataille Navale ==========");

#Saisie de la taille de la grille souhaitée par le joueur 
print("Saisissez la taille de votre grille :")
tailleGrille=input()

print(" ");

#Saisie du nom des deux joueurs par l'utilisateur 
print("Entrez le nom du Joueur 1 : ")
NomJoueur1=input(); #On récupère le nom du premier joueur 
Joueur1=Joueur(NomJoueur1, tailleGrille); #On crée le premier joueur 


print("Entrez le nom du Joueur 2 : ")
NomJoueur2=input(); #On récupère le nom du second joueur 
Joueur2=Joueur(NomJoueur2, tailleGrille); #On crée le second joueur 

print("La partie va opposer "+Joueur1+" à "+Joueur2+" !");

#Placement des bateaux 
print("--------------Placement des bateaux-----------------");
print("Combien voulez de bateaux : ");
nbBat=input();


#On ajoute les bateaux de taille definie par l'utilisateur 
for j in range(0,nbBat):
	print("Saisir la taille du bateau "+(j+1)+" :");
	taille=input();
	Joueur1.Flotte.ajouterBateaux(taille);
	Joueur2.Flotte.ajouterBateaux(taille);

#Les bateaux sont initialisés mais pas placés
#On place les bateaux 

print("--------------------------------------------------------------------------------------------")
print(" ")
print(Joueur1.name()+" place ses bateaux :  ")
print(" ")

 #Le joueur 1 place ses différents 

for i in range(0,nbat):
	t=0
	x=-1
	y=-1
	#On place la première coordonnée du bateau i
	while (Joueur1.Grille.verificationCoordonnees(x,y)==False):
		print("Entrez la "+(t+1)+" position du bateau"+(i+1)+" :")
		print("x = ");
		x=input();

		print("y = ");
		y=input();

		Joueur1.Grille.placerPositionBateau(i,x,y);

	for t in range(1,Joueur1.Flotte.getTaille(i)):
		x=-1;
		y=-1;
		while (Joueur1.Grille.estValide((i+1),x,y)==False):
			print("Entrez la "+(t+1)+" position du bateau"+(i+1)+" :")
			print("x = ");
			x=input();

			print("y = ");
			y=input();

		Joueur1.Grille.placerPositionBateau(i,x,y)

print("--------------------------------------------------------------------------------------------")
print(" ")
print(Joueur2.name()+ " place ses bateaux :  ")
print(" ")


for i in range(0,nbat):
	t=0
	x=-1
	y=-1
	#On place la première coordonnée du bateau i
	while (Joueur2.Grille.verificationCoordonnees(x,y)==False):
		print("Entrez la "+(t+1)+" position du bateau"+(i+1)+" :")
		print("x = ");
		x=input();

		print("y = ");
		y=input();

		Joueur2.Grille.placerPositionBateau(i,x,y)

	for t in range(1,Joueur2.Flotte.getTaille(i)):
		x=-1;
		y=-1;
		while (Joueur2.Grille.estValide((i+1),x,y)==False):
			print("Entrez la "+(t+1)+" position du bateau"+(i+1)+" :")
			print("x = ");
			x=input();

			print("y = ");
			y=input();

		Joueur2.Grille.placerPositionBateau(i,x,y);


	





print("==================== Début du jeu ========================");
#Début du jeu
tourDeJeu=1;

while ((Joueur1.Grille.estVide()==False) or (Joueur2.Grille.estVide()==False)): 
	if (tourDeJeu==1):
		print(Joueur1.name()+ " à toi de tirer !");
		#Joueur 1 tire
		a=-1;
		b=-1;
		while (Joueur2.Grille.estDansGrille(a,b)==False):
			print("Entrez les cordonnées de la cible : ");
			a=input();
			b=input();
		result=Joueur2.Grille.tirer(a,b);
		print(result);


		tourDeJeu=2; #Changement de tour

	else: 
		print(Joueur1.name()+ " à toi de tirer !");
		#Joueur 2 tire

		a=-1;
		b=-1;
		while (Joueur1.Grille.estDansGrille(a,b)==False):
			print("Entrez les cordonnées de la cible : ");
			a=input();
			b=input();
		result=Joueur1.Grille.tirer(a,b);
		print(result);

		tourDeJeu=1; #Changement de tour


print("==================== Fin du jeu ========================");

if(Joueur1.Grille.estVide()):
	print(Joueur2.name()+" a gagné");
else:
	print(Joueur1.name()+ "a gagné");




#Fin de Partie 
