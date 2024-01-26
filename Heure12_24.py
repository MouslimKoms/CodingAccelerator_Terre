import sys 

def heure12_24 (temps):
    #Vérifier si l'heure est valide
    if len(temps) !=7 or temps[2] != ':' or temps[5:] not in ['AM', 'PM'] :
        return "Format d'heure invalide" # Retourne un message d'erreur si le format de l'heure est invalide 
    
    heures = int (temps[:2]) # Récupère les heures de l'heure donnée 
    minutes = int(temps[3:5]) # Récupére les mimutes de l'heure donnée 
    periode = temps[5:] # Récupère la période (AM ou PM) de l'heure donnée 
    
    # Vérifier si l'heure est valide 
    if heures < 1 or heures > 12 or minutes < 0 or minutes > 59:
        return "heure invalide" # Retourne un message d'erreur si l'heur est invalde
    
    # Convertir l'heure au format 24h
    if periode == 'AM':
        if heures == 12 :
            return "00:"+ temps[3:5] # Retourne minuit au format 24h
        else:
            return temps[:2] +":"+ temps[3:5] # Retourne l'heure du matin  au format 24h
    else: # période PM
        if heures == 12 :
            return "12:"+temps[3:5] # Retourne midi au format 24h
        else:
            return str(heures+12).zfill(2) +":"+ temps[3:5] # Retourne l'heure de l'aprés-midi au format 24h 


if __name__ == "__main__" : 
    if len(sys.argv) != 2 :
        print ("Veuillez fournir une heure au format 12h en argument .")
    else :
        temps = sys.argv[1]
        print (heure12_24(temps)) # Affiche l'heure convertie au format 24h 