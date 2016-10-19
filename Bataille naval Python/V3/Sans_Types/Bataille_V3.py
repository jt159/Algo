#Bataille naval 
#V1 : Stocke une position prédeterminé et immuable (un bateau de taille 1 sur la grille 20*20)
#Demande au joueur les coordonées x et y et renvoie touché, coulé ou en vue 
#V2 : S'arrète que lorsque touché
#V3 : Entrer 5 bateaux de taille 1 et le programme s'arrete quand tous les bateaux sont coulés

#Structure de données :
#Un tableau qui stock les tailles de chaque bateau actualisé
Tailles =[];

for v in range(5):
	Tailles.append(0);
print(Tailles);
#Un tableau à deux dimensions qui stocke la grille comprenant des 0 et des 1 pour les positions 
#des bateaux
Grille=[];

for v in range(21):
	Grille.append([0]*20);
	
#Fonctions utilisés : 

def envue(Grille, xvue, yvue): 
	envue=bool(False);
	p=int(0);
	while envue==False and p<21:
		if Grille[p][yvue]>0 or Grille[xvue][p]>0:
			envue=True;
		p=p+1;
			
	return envue
	
#Debut Main 
# Saisie de la position des 5 bateaux : 
for i in range(0,5):

	print ("Entrez coordonée x du bateau ",(i+1),": ");
	x = int(input());
	print ("Entrez coordonée y du bateau ",(i+1),": ");
	y = int(input());
	print ("Votre bateau est placé aux x=",x," et y=",y," !");
	Grille[x][y]=i+1;
	Tailles[i]=1;

#Affichage de la grille : 
for j in range(0,20):
	print(Grille[j]);

#Affiche tableau des tailles : 
print(Tailles);

#initialisation de la condition d'arret => touché -- bool à false

touche=bool(False);
print (touche);

# Boucle qui vérifie que le bateau est bien touché : 
while (sum(Tailles)):

	# Saisie des coordonnées de tir : 
	print ("Entrez coordonée x du tir : ");
	xtir = int(input());
	print ("Entrez coordonée y du tir : ");
	ytir = int(input());

	# Test des coordonnées de tir 
	if (Grille[xtir][ytir]>0): 
		bat=Grille[xtir][ytir];
		print ("Bateau ",bat," touché ! ");
		Tailles[(bat-1)]=Tailles[(bat-1)]-1;
		Grille[xtir][ytir]=Grille[xtir][ytir]-1;
		for j in range(0,20):
			print(Grille[j]);
	elif (envue(Grille,xtir,ytir)):
		print("En vue ! ");
	else:
		print("A l'eau !");

	print(Tailles);
