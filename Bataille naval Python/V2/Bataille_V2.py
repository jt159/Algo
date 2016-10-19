#Bataille naval 
#V1 : Stocke une position prédeterminé et immuable (un bateau de taille 1 sur la grille 20*20)
#Demande au joueur les coordonées x et y et renvoie touché, coulé ou en vue 
#V2 : S'arrète que lorsque touché


# Saisie de la position du bateau : 
print ("Entrez coordonée x du bateau : ");
x = int(input());
print ("Entrez coordonée y du bateau : ");
y = int(input());

print ("Votre bateau est placé aux x=",x," et y=",y," !");

#initialisation de la condition d'arret => touché -- bool à false

touche=bool(False);
print (touche);

# Boucle qui vérifie que le bateau est bien touché : 
while (touche==False):

	# Saisie des coordonnées de tir : 
	print ("Entrez coordonée x du tir : ");
	xtir = int(input());
	print ("Entrez coordonée y du tir : ");
	ytir = int(input());

	# Test des coordonnées de tir 
	if (xtir==x and ytir==y): 
		print ("Touché ! ");
		touche=True; 
	elif (xtir==x or ytir==y):
		print("En vue ! ");
	else:
		print("A l'eau !");

#End