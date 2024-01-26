import sys

def Nombre_premier (n):
    if n < 2 : # Vérifie si le nombre est inférieur à 2 
        return False # retourne false pour 0 et 1 qui ne sont pas premiers
    for i in range (2 , n) : # Parcourt les nombres de 2 à n-1
        if (n % i ) == 0 : # Vérifie si le nombre est divisible par un nombre autre que 1 et lui-meme
            return False # Retourne false si le nombre est divisible 
    return True # Retourne true si le nombre est premier


if  __name__ == "__main__" :
    if len(sys.argv) != 2 : # Vérifie s' il y a un seul argument 
        print("Veuillez fournir un seul entier en argument .") # Affiche un message d'erreur
        
    else: 
        try:
            nombre = int(sys.argv[1]) # Convertit l'argument entier
            if Nombre_premier(nombre): # Vérifie si le nombre est premier en uilisant la fonction Nombre_premier 
                print(f"{nombre} est un nombre premier") # Affiche un message si le nombre est premier 
            else:
                print(f"{nombre} n'est pas un nombre premier ") # Affiche un message si le nombre n'est pas premier 
        except ValueError :
            print("L'argument fourni n'est pas un entier ") # Affiche un message d'erreur si l'argument n'est pas un entier
            