import script_class


if __name__ == '__main__':
    #clé fournie par la SNCF pour acceder à l'API
    #password = input("authentification request :")
    password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e'

    SNCF = script_class.APItools(password,'stop_areas.json')

    '''
    #Lire l'API
    SNCF.readAPI()
    
    #Afficher le jason file avec pretty_print
    SNCF.printWithPrettyPrint()

    
    #Ajouter un nouveau dict au JSON existant
    SNCF.addNewKeyValuePair(script_class.writeNewDict())

    #Ajouter un nouveau dict a la clé ['stop_areas'] du JSON existant
    SNCF.addNewStopArea(script_class.writeNewDict())

    #Afficher le jason file avec pretty_print
    SNCF.printWithPrettyPrint()
    
    #SNCF.getLinks()
    
    #Faire une requête sur l'API de la SNCF
    SNCF.requestAPI()
    
    #Ecrire des données dans un CSV, avec parfois des cases vides, checker la fonction
    SNCF.writeCSV()
    
    #Faire une requête sur le trajet PARIS - LYON
    SNCF.requestAPIParisLyon()

    #Récuperer des données sur le trajet PARIS - LYON
    SNCF.areasSTOPSParisLyon()
    

    #Faire une requete pour avoir des résultats avec une heure précise
    #ici on va utiliser une boucle pour avoir tous les prochains départs
    SNCF.requestStationWithDatetime()
    '''