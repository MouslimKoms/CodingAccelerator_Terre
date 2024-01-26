import sys

if len (sys.argv) == 1 :
    print("Erreur : Aucune chaine de caractère fournie en argument")

elif len(sys.argv) > 2:
    print("Erreur : vous avez fourni plus d'une chaine de caractère")    
else : 
    chaine = sys.argv[1]
    
    if chaine.isdigit():
        print ("Erreur : Un entier a été fourni en argument ")
    else:
        print(len(chaine))
        


  