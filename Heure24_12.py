import sys

def convertie_heure_12 (time) :
    # Vérifier si l'heure est valide 
    if len(time) != 5 or time [2] != ':':
        return "Format d'heure invalide" # Retourne un message d'erreur si le format de l'heure est invalide
    heures = int(time[:2]) # Récupère les heures de l'heure donnée 
    minutes = int(time[3:]) #Récupère les minutes de l'heure donnée 
    
    
    # Vérifier si l'heure est valide 
    if heures == 0 :
        return "12" + time[3:] + "AM" # Retourne minuit au format 12h 
    elif heures < 12 :
        return time + "AM" # Retourne l'heure du matin au format 12h
    elif heures == 12 :
        return time + "PM" # Retourne midi au format 12h
    else :
        return str(heures - 12).zfill(2) + ":" + time[3:] + "PM" # Retourne l'heure de l'après-midi au format 12


if __name__ == "__main" : 
    if len(sys.argv) != 2:
        print("Veuillez fournir une heure au format 24h en argument ")
    
else:
    time = sys.argv[1]
    print(convertie_heure_12(time)) # Affiche l'heure convertie au format 12h 