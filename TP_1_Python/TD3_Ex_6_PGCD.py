#!/usr/bin/python
# -*-coding:Latin-1 -*

def PGCD (a,b):
	#Données : a et b sont des entiers strictement positifs
	#Resultat: renvoie P le PGCD de a et b 
	P=1; 
	i=1; #i est  notre curseur 

	while (i<=a and i<=b): 
		if (a%i==0 and b%i==0): 
			P=i;
		i=i+1;
	#i>a ou i>b 	
	return P;

def main():
	a=0;
	b=0; 

	print("Saisir a : ");
	a=input();
	print("Saisir b : ");
	b=input();

	p=PGCD(a,b);
	print("Le PGCD de ",a," et ",b," est ",p," !");

main();