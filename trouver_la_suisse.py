import sys
def valeure_du_milieu (a, b, c):
    #Vérifier si a est le plus petit 
    if a < b and a < c :
        # Vérifier si b est le plus grand 
        if b > c :
            return c
        else: 
            return b
    # Vérifier si b est le plus petit 
    elif b < a and b < c : 
        # Vérifier si a est le plus grand 
        if a > c : 
            return 
        else :
            return a
    elif a == b and b == c:
        return "Erreur"    
    else:
        return a
    
if __name__ == "__main__" :
    if len (sys.argv) != 4 :
        print( "Veuillez fournir trois entiers en arguments")
    
    else:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            c = int(sys.argv[3])
            print(valeure_du_milieu(a, b, c))
        except ValueError:
            print("Les arguments doivent etre des entiers ")