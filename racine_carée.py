import sys 

def raçine_carée (n):
    if n < 0 :
        return "L'entier fourni n'est pas posifif ."
    #Initialisation des variables pour la méthode d'extraction de la raçine carrée
    x = n #valeur initial de x
    y=(x + n // x) // 2 #calcul de la première approximation de la raçine carrée
    
    #boucle d'extraction de la raçine carrée 
    
    while y < x :
        x = y
        y = (x + n // x) // 2 
    return x #retourne la valeur de la racine carrée 

if __name__ ==  "__main__":
    if len (sys.argv) != 2: 
        print("Veuillez fournir un entier positif en argument .")
    else:
        try:
            nombre = int (sys.argv[1])
            print(raçine_carée(nombre))
        except ValueError:
            print("L'argument fourni n'est pas un entier .")    