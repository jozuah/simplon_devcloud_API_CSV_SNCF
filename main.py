import script_class

def main():

    choix = 0
    
    #clé fournie par la SNCF pour acceder à l'API
    #password = input("authentification request :")
    password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e'

    SNCF = script_class.APItools(password,'stop_areas.json')
    while choix != "q" :
        
        print("\n(1) Lire une fichier Json localement")
        print("(2) Utiliser PPrint pour lire le Json")
        print("(3) Ajouter un nouveau dictionnaire au Json")
        print("(4) Ajouter un nouveau dictionnaire au Json dans un dictionnaire existant ['stop_areas']")
        print("(5) Faire une requete sur l'API de la SNCF + ecriture d'un CSV")
        print("(6) Affichet les arrets et temps d'arrêts pour le trajet Paris-Lyon")
        print("(7) Afficher les prochains départs pour le trajet Paris-Lyon à partir d'une date précise")
        print("(q) Pour quitter l'aplication")

        choix = input("Que voulez vous faire ? ")

        if choix == "1" :
            #Lire l'API
            SNCF.readAPI()
            print(SNCF.data_sncf)
        elif choix == "2":
            #Lire l'API
            SNCF.readAPI() 
            #Afficher le jason file avec pretty_print
            SNCF.printWithPrettyPrint()           
        elif choix == "3":
            #Lire l'API
            SNCF.readAPI() 
            #Ajouter un nouveau dict au JSON existant
            SNCF.addNewKeyValuePair(script_class.writeNewDict())           
        elif choix == "4":
            #Lire l'API
            SNCF.readAPI() 
            #Ajouter un nouveau dict a la clé ['stop_areas'] du JSON existant
            SNCF.addNewStopArea(script_class.writeNewDict())           
        elif choix == "5":
            #Faire une requête sur l'API de la SNCF
            SNCF.requestAPI()
            #Ecrire des données dans un CSV, avec parfois des cases vides, checker la fonction
            SNCF.writeCSV()
        elif choix == "6":
            #Faire une requête sur le trajet PARIS - LYON
            SNCF.requestAPIParisLyon()

            #Récuperer des données sur le trajet PARIS - LYON
            SNCF.areasSTOPSParisLyon()
        elif choix == "7":
            #Faire une requete pour avoir des résultats avec une heure précise
            #ici on va utiliser une boucle pour avoir tous les prochains départs
            SNCF.requestStationWithDatetime()
        
    print("Au revoir !")
    



if __name__ == '__main__':

    main()
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
    