import os

ficher_present = True
ficher_suivant = False
nom_fichier = os.path.basename(__file__)


def affiche_fichier ():
     print(nom_fichier)
     
while ficher_suivant == ficher_present :
     print(False)
else :
     affiche_fichier ()
     

	
