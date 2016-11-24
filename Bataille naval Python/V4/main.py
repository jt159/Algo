from joueur import *;
from grille import *;
from bateau import *;


print("========== Bienvenue dans la Bataille Navale ==========");

#Saisie de la taille de la grille souhaitée par le joueur 
print("Saisissez la taille de votre grille :")
tailleGrille=input()

print(" ");

#Saisie du nom des deux joueurs par l'utilisateur 
print("Entrez le nom du Joueur 1 : ")
NomJoueur1=input(); #On récupère le nom du joueur 
Joueur1=Joueur(NomJoueur1); #On crée le joueur 
Grille1=creeGrille(tailleGrille); #On crée la grille 

print("Entrez le nom du Joueur 2 : ")
NomJoueur2=input(); #On récupère le nom du joueur 
Joueur2=Joueur(NomJoueur2); #On crée le joueur 
Grille2=creeGrille(tailleGrille); #On crée la grille 

print("La partie va opposer "+Joueur1+" à "+Joueur2+" !");

#Placement des bateaux 
print("--------------Placement des bateaux-----------------");
print("Combien voulez de bateaux : ");
nbBat=input();



#On initialise la flotte des joueurs
Flotte1=Flotte();
Flotte2=Flotte();

#On ajoute les bateaux de taille definie par l'utilisateur 
for j in range(0,nbBat):
	print("Saisir la taille du bateau "+(j+1)+" :");
	taille=input();
	Flotte1.ajouterBateaux(taille);
	Flotte2.ajouterBateaux(taille);

#Les bateaux sont initialisés mais pas placés
#On place les bateaux 

print("--------------------------------------------------------------------------------------------")
print(" ")
print("Le Joueur 1 place ses bateaux :  ")
print(" ")

 #Le joueur 1 place ses différents 

for i in range(0,nbat):
	t=0
	x=-1
	y=-1
	#On place la première coordonnée du bateau i
	while (Grille1.verificationCoordonnees(x,y)==False):
			print("Entrez la "+(t+1)+" position du bateau"+(i+1)+" :")
			print("x = ");
			x=input();

			print("y = ");
			y=input();

		Grille1.placerPositionBateau(i,x,y)

	for t in range(1,Joueur1.getTaille(i)):
		x=-1;
		y=-1;
		while (Grille1.estValide((i+1),x,y)==False):
			print("Entrez la "+(t+1)+" position du bateau"+(i+1)+" :")
			print("x = ");
			x=input();

			print("y = ");
			y=input();

		Grille1.placerPositionBateau(i,x,y)

print("--------------------------------------------------------------------------------------------")
print(" ")
print("Le Joueur 2 place ses bateaux :  ")
print(" ")


for i in range(0,nbat):
	t=0
	x=-1
	y=-1
	#On place la première coordonnée du bateau i
	while (Grille1.verificationCoordonnees(x,y)==False):
			print("Entrez la "+(t+1)+" position du bateau"+(i+1)+" :")
			print("x = ");
			x=input();

			print("y = ");
			y=input();

		Grille1.placerPositionBateau(i,x,y)

	for t in range(1,Joueur1.getTaille(i)):
		x=-1;
		y=-1;
		while (Grille1.estValide((i+1),x,y)==False):
			print("Entrez la "+(t+1)+" position du bateau"+(i+1)+" :")
			print("x = ");
			x=input();

			print("y = ");
			y=input();

		Grille1.placerPositionBateau(i,x,y);


	





print("==================== Début du jeu ========================");
#Début du jeu
tourDeJeu=1;

while (!(Grille1.estVide()) or !(Grille2.estVide())): 
	if (tourDeJeu==1):
		#Joueur 1 tire
		a=-1;
		b=-1;
		while (Grille2.estDansGrille(a,b)==False):
			print("Entrez les cordonnées de la cible : ");
			a=input();
			b=input();
		result=Grille2.tirer(a,b);
		print(result);


		tourDeJeu=2; #Changment de tour

	else: 
		#Joueur 2 tire

		a=-1;
		b=-1;
		while (Grille1.estDansGrille(a,b)==False):
			print("Entrez les cordonnées de la cible : ");
			a=input();
			b=input();
		result=Grille1.tirer(a,b);
		print(result);

		tourDeJeu=1; #Changment de tour


print("==================== Fin du jeu ========================");

if(Grille1.estVide()):
	print("Le joueur 2 a gagné");
else:
	print("Le joueur 1 a gagné");




#Fin de Partie 
