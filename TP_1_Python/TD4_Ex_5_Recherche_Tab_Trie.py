#!/usr/bin/python
# -*-coding:Latin-1 -*

def Rechercher(T,x):
	#Données : prend un tableau T trié et un entier x
	#Résultat : retourne True si x figure dans T, False sinon

	n=0; #curseur de la première case du sous tableau de T étudié
	m=len(T)-1; #curseur de la dernière case du sous tableau de T étudié
	i=int(len(T)/2); #milieu du sous tableau de T étudié
	b=False;

	while(T[i]!=x and (i!=n and i!=m)):
		if(x<T[i]):
			m=i;
			i=int(m/2);
		else:
			n=i+1;
			i=int(n+((m-n)/2));
	#si x est dans le tableau, ou si tous les éléments du tableau ont été verifiés
		print("n=",n);
		print("m=",m);
		print("i=",i);

	return (T[i]==x);

"""
def main():
	Tab=[2,3,5,9,11,15];
	print(Tab);
	print("Quelle valeur souhaitez vous chercher : ");
	o=input();

	print(Rechercher(Tab,o));

main();"""