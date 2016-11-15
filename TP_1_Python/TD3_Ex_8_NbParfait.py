#!/usr/bin/python
# -*-coding:Latin-1 -*

def Nb_Parfait(m):
	#Données: n entier strictement positif
	#Resultat: Renvoie vrai si le nombre n est parfait sinon renvoie faux

	s=0; #Somme des diviseurs
	i=1;

	for i in range(1,m):
		if (m%i==0):
			s=s+i;

	return (s==m); 

def Somme_Parfait(n): 
	#Données: n entier strictement supérieur à 0
	#Resultat: la somme des nombres parfait inférieur ou égaux à n 

	r=0 #Resultat renvoyé (somme des nombres parfait)
	j=1;

	for j in range(1,n+1):
		if (Nb_Parfait(j)):
			r=r+j;
		
	return r;

def main(): 
	N=0;

	print("Entrez le nombre n dont vous souhaitez connaitre la somme de tous les nombres parfait inférieur ou égaux à celui-ci :  ");
	N=input(); 

	print ("Voici la somme des nombres parfaits : ",Somme_Parfait(N)," !");


main();