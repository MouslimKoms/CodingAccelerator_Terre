import sys

if len(sys.argv) !=3:
    print("veuillez entrer deux nombre !")
else:
    try:
        
        nombre1 = int(sys.argv[1])
        nombre2 = int(sys.argv[2])
        
        if nombre2 == 0 :
            print("Veuillez ne pas diviser par 0 !")
        else:
            resultat = nombre1 // nombre2
            reste = nombre1 % nombre2
            
            if resultat <= 0 :
                print(" Erreur le résultat est inférieur à 0 !")
            
            else:
                print(f"Resultat:{resultat}")
                print(f"Reste : {reste}")
    except ValueError:
     print("veuillez entrer des nombres !")
