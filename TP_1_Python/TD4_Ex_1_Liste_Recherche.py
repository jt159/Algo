#!/usr/bin/python
# -*-coding:Latin-1 -*

def Est_Present(T,x):
	#Données: T tableau à n elements entiers et x entier 
	#Resultat: renvoie True si x est dans T, False sinon

	i=0;
	r=False;

	while (r==False and i<=(len(T)-1)):
		r=(T[i]==x);
		i=i+1;
	return r;
"""
def main():
	Tab=[2,5,9,4,3,7];
	print(Tab);
	print("Quelle valeur souhaitez vous chercher : ");
	o=input();

	print(Est_Present(Tab,o));

main();"""