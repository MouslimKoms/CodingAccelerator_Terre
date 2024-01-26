import sys

def power(base, exposant):
    if exposant < 0:
        return "L'exposant ne peut pas etre négatif "
    resultat = 1
    for _ in range(exposant):
        resultat *= base 
    return resultat


if __name__ == "__ main__":
    
    if len(sys.argv) != 3:
        print("Erreur : Veuillez fournir la base et l'exposant en argument ")
        
else:
     try:
         
         base = int(sys.argv[1])
         exposant = int(sys.argv[2])
         print (power(base, exposant))
             
     except (IndexError, ValueError ):
        print("Erreur : Les arument doivent etre des Nombres .")