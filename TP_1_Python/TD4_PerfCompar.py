#!/usr/bin/python
# -*-coding:Latin-1 -*

from TD4_Ex_5_Recherche_Tab_Trie import Rechercher;
from TD4_Ex_1_Liste_Recherche import Est_Present;
import random;


def CreerTabRandom(t):
	#Données : prend un entier t
	#Résultat : crée un tableau de taille t d'éléments entiers aléatoires

	return([random.randint(0,9) for i in range(t)]);

def TriTab(T):
	#Données : prend le tableau Tab
	#Résultat : renvoie le tableau Tab trié par ordre croissant
	q=0;
	i=0;
	j=1;
	o=i;
	p=j;
	n=len(T);

	while((i<(n-1)) and (j<n)): #boucle qui redescend pour trouver la position de T[j]
		o=i;
		p=j;
		while(T[o]>T[p] and o>=0):
			q=T[o];
			T[o]=T[p];
			T[p]=q;
			o=o-1;
			p=p-1;
		#s'arrete quand T[o]<=T[p]
		i=i+1;
		j=j+1;
	return T;



def main():
	print("Donner la taille du tableau souhaité : ");
	o=input();
	Tab=CreerTabRandom(o);
	print (Tab);
	print(TriTab(Tab));


main();