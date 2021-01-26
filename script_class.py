import json
import pprint
import requests
import csv
import datetime
import os
import unittest

class APItools :
    def __init__(self,authentification,my_api_file=''):
        self.my_api_file = my_api_file
        self.authentification = authentification
        self.data = None
        self.data_sncf = None

    def readAPI (self):
        '''
        a="bleu"
        b = '"{}"'.format(a)
        b = '"' + a + '"'

        my_dict = { a : b }
        print(my_dict)
        '''
        #Lire mon Json file
        with open(self.my_api_file) as my_json_file:
            self.data_sncf = json.load(my_json_file)
            print(type(self.data_sncf))
  
    def printWithPrettyPrint (self):
        pprint.pprint(self.data_sncf)

    def addNewKeyValuePair (self,newKey):
        self.newKey = newKey
        self.data_sncf.update(self.newKey)
        with open(self.my_api_file, 'w') as my_json_file:
            json.dump(self.data_sncf,my_json_file)

    def addNewStopArea(self,newStation):
        self.newStation = newStation
        self.data_sncf['stop_areas'].append(self.newStation)
        #ecrire dans mon json
        with open(self.my_api_file, 'w') as my_json_file:
            json.dump(self.data_sncf,my_json_file)

    def requestAPI(self):
        #https://www.dataquest.io/blog/python-api-tutorial/
        #Je récupère ma requête dans "r"
        r = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas', auth=(self.authentification, ''))
        #print(r.status_code) #renseigne sur le statut de ma requête : 200 -> good
        #Je transforme mes données en json
        self.data = r.json()
               
    def writeCSV(self):
        #conversion de mon dict en string
        
        #je mets dans une variable la liste data_object["stop_areas"]
        listOfAreas = self.data["stop_areas"]
        
        listOfNames=[]
        for local_name in listOfAreas:       
            try:
                 local_name["name"]
            except :
                listOfNames.append("")
            else:
                listOfNames.append(local_name["name"])

        #print(listOfNames)   

        listOfLats=[]
        for local_lat in listOfAreas:       
            try:
                 local_lat["coord"]["lat"]
            except :
                listOfLats.append("")
            else:
                listOfLats.append(local_lat["coord"]["lat"])

        #print(listOfLats)           
        
        listOfLongs=[]
        for local_long in listOfAreas:       
            try:
                 local_long["coord"]["lon"]
            except :
                listOfLongs.append("")
            else:
                listOfLongs.append(local_long["coord"]["lon"])

        #print(listOfLongs)    
        
        listOfCodes=[]
        for local_code in listOfAreas:       
            try:
                 local_code["codes"]
            except :
                listOfCodes.append("")
            else:
                listOfCodes.append(local_code["codes"])

        #print(listOfCodes)    
        
        listOfCodesTypes=[]
        listOfCodesValues=[]
        for local_code in listOfAreas:       
            try:
                 local_code["codes"]
            except :
                listOfCodesTypes.append("")
                listOfCodesValues.append("")
            else:
                listOfCodesTypes.append(local_code["codes"][0]["type"])
                listOfCodesValues.append(local_code["codes"][0]["value"])
                
        
        #Définition des colonnes pour mon csv
        csv_colonnes = ['Nombre','Ville','Lattitude','Longitude','Type','Value']
        with open('sncf.csv', 'w', newline='') as my_csv_file:
            stylo = csv.DictWriter(my_csv_file,fieldnames = csv_colonnes)
            #Permet d'ecrire la premiere ligne avec les colonnes définis
            stylo.writeheader()
            for i in range (len(listOfAreas)):
            #je créé mon dictionnaire pour utiliser le DictWriter, je fais correspondre mes key avec ceux des colonnes définies
                final_dict={'Nombre':i,'Ville':listOfNames[i], 'Lattitude':listOfLats[i],'Longitude':listOfLongs[i],'Type':listOfCodesTypes[i],'Value':listOfCodesValues[i]}
                stylo.writerow(final_dict)
                print(final_dict)
        

        ''' La correction BY Amin/Maria la bikeuse
        for key in data_object.keys():
            print(key)
            print(f"{key} is {data_object[key]}")
        for key,value in data_object.items():
            print(f"{key} is {value}")
        print(data_object["stop_areas"])
        
        print(type(listOfAreas))
        Area=listOfAreas[0]
        print(type(Area),Area)
        print(Area.keys())

        listOfids=[]
        for loop_Area in listOfAreas:
            if type(loop_Area) == dict:
                if "id" in loop_Area.keys:
                    local_id = loop_Area["id"]
                    listOfids.append(local_id)
                else :
                    print("missing key:id")
            else:
                print("Unexpected format (dict expected)",type(loop_Area))
        '''          

    def requestAPIParisLyon(self):
        #URL = f"https://api.sncf.com/v1/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025
        depart = "stop_area:OCE:SA:87686006"
        arrivee = "stop_area:OCE:SA:87722025"
        URL = f"https://api.sncf.com/v1/journeys?from={depart}&to={arrivee}"
        #Récupération des données de la requête
        r = requests.get(URL, auth=(self.authentification, ''))      
        self.data2 = r.json()

    def areasSTOPSParisLyon(self):

        self.list_arret=[]
        self.acces_arret = SNCF.data2["journeys"][0]["sections"][1]["stop_date_times"]
        print("\nListe des arrets et de leur temps d'arret :\n")
        for arret in self.acces_arret:
            print(arret["stop_point"]["name"])
            self.list_arret.append(arret["stop_point"]["name"])

    
            #https://openclassrooms.com/forum/sujet/soustraire-deux-dates-pour-recuperer-temps-restant
            #Je récupère le temps d'arrivée
            self.base_arrival = arret["base_arrival_date_time"]
            #conversion du temps d'arrivée au format date
            self.base_arrival_date_format=datetime.datetime.strptime(self.base_arrival, "%Y%m%dT%H%M%S")

            self.base_departure = arret["base_departure_date_time"]
            self.base_departure_date_format=datetime.datetime.strptime(self.base_departure, "%Y%m%dT%H%M%S")
        
            self.temps_arret = self.base_departure_date_format - self.base_arrival_date_format
            print("temps d'arret: ",self.temps_arret)

    def requestStationWithDatetime (self):

        min_date_time = inputDateInSNCFFormat()
        min_date_time_date_format = datetime.datetime.strptime(min_date_time, "%Y%m%dT%H%M%S")
        
        self.all_departure_from =[]
        self.all_departure_from.append(min_date_time)

        depart = "stop_area:OCE:SA:87686006" #Paris (Gare de Lyon)
        arrivee = "stop_area:OCE:SA:87722025" #Lyon (Perrache)

        count_next_departure=int(input(f"\nCombien de départs à partir de {min_date_time_date_format} ? :"))
        #Je fais une boucle qui va iterer sur des request, ces request vont evoluer avec 
        #un datetime qui change. Je récuper l'heure du prochain départ, auxquel je rajoute +1second
        #que je réinjecte dans l'URL
        print(f"\nNext {count_next_departure} departure from Paris to Gare de Lyon:")
        for i in range (0,count_next_departure):
            URL = f"https://api.sncf.com/v1/journeys?from={depart}&to={arrivee}&datetime={self.all_departure_from[i]}"
            r = requests.get(URL, auth=(self.authentification, ''))
            # autre écriture plus compacte avec le .json() en fin de requete
            #self.data3 = requests.get(URL, auth=(self.authentification, '')).json()
            
            #Récupération des données de la requête
            self.data3 = r.json()

            #Récupération de l'heure d'arrivée
            next_departure_arrival = self.data3["journeys"][0]["arrival_date_time"]
            next_departure_arrival_date_format = datetime.datetime.strptime(next_departure_arrival, "%Y%m%dT%H%M%S")

            #Récupération du temps de trajet
            duration_trip = int(self.data3["journeys"][0]["duration"])
            duration_trip_time_format = datetime.timedelta(seconds=duration_trip) #converssion seconde to hh:mm:ss
            
            #Récupération de l'heure de départ
            next_departure = self.data3["journeys"][0]["departure_date_time"]
            next_departure_date_format=datetime.datetime.strptime(next_departure, "%Y%m%dT%H%M%S")
            
            print(f"départ:{next_departure_date_format}  arrivée:{next_departure_arrival_date_format}  durée:{duration_trip_time_format}")
            
            
            #Modif de l'heure de départ, je lui rajoute 1 seconde pour pouvoir relancer une requête dessus
            next_departure=next_departure [:-1] + "1"

            self.all_departure_from.append(next_departure)
            #print(all_departure_from)

def writeNewDict ():
    my_dict={}
    my_key=input("KEY:")
    my_value=input("VALUE:")
    my_dict[my_key]=my_value

    return my_dict

def inputDateInSNCFFormat () :
    print("\nDéfinir l'heure de départ:")
    year = input(str("année :"))
    month = input(str("mois :"))
    day = input(str("jour :"))
    hour = input(str("heure :"))
    minutes = input(str("minutes :"))
    sec = input(str("secondes :"))

    my_date_is=year+month+day+'T'+hour+minutes+sec
    return my_date_is


'''http://doc.navitia.io/#standard-objects 
Iso-date-time
Navitia

exposes every date times as local times of the coverage via an ISO 8601 “YYYYMMDDThhmmss” string
can be requested using local times of the coverage via ISO 8601 as “YYYYMMDDThhmmss” or “YYYY-MM-DDThh:mm:ss”
can be requested using UTC relative times via ISO 8601 as “YYYYMMDDThhmmss+HHMM” or “YYYY-MM-DDThh:mm:ss+HH:MM”
can be requested using UTC times via ISO 8601 as “YYYYMMDDThhmmssZ” or “YYYY-MM-DDThh:mm:ssZ”
Context object provides the Timezone, useful to interpret datetimes of the response.

For example:

https://api.navitia.io/v1/journeys?from=bob&to=bobette&datetime=20140425T1337
https://api.navitia.io/v1/journeys?from=bob&to=bobette&datetime=2014-04-25T13:37+02:00
https://api.navitia.io/v1/journeys?from=bob&to=bobette&datetime=2014-04-25T13:37:42Z
There are lots of ISO 8601 libraries in every kind of language that you should use before breaking down https://youtu.be/-5wpm-gesOY

Iso-date
The date are represented in ISO 8601 “YYYYMMDD” string.


#Faire une request sur une heure précise (ici la date d'aujoud'hui + 18h00) entre Paris Gare de Lyon et Lyon Perrache
#https://api.navitia.io/v1/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025&datetime=20140425T1337
#https://api.sncf.com/v1/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025&datetime=20210125T180000

'''

'''
#Pour trouver le code de la gare de Perpignan  0087784009  ==> stop_area:OCE:SA:87784009"
# https://data.sncf.com/explore/dataset/referentiel-gares-voyageurs/table/?disjunctive.gare_ug_libelle&sort=gare_alias_libelle_noncontraint

authentification = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e'
depart = "stop_area:OCE:SA:87686006" #Paris (Gare de Lyon)
arrivee = "stop_area:OCE:SA:87784009" #Perpignan

URL = f"https://api.sncf.com/v1/journeys?from={depart}&to={arrivee}"
r = requests.get(URL, auth=(authentification, ''))

#Récupération des données de la requête
data4 = r.json()
pprint.pprint(data4)
'''
