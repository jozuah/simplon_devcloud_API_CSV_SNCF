import json
import pprint
import requests
import csv
import datetime

class APItools :
    def __init__(self,my_api_file):
        self.my_api_file = my_api_file

    def readAPI (self):
        with open(self.my_api_file) as my_json_file:
            self.data_sncf=my_json_file.read()
            self.json_sncf=json.loads(self.data_sncf)
            
    def printWithPrettyPrint (self):
        pprint.pprint(self.json_sncf)

    def addNewKey (self,newKey):
        self.newKey = newKey
        self.json_sncf.update(self.newKey)
        with open(self.my_api_file, 'w') as my_json_file:
            json.dump(self.json_sncf,my_json_file)
    
    def addNewStopArea(self,newStation):
        self.newStation = newStation
        self.json_sncf['stop_areas'].append(self.newStation)
        #ecrire dans mon json
        with open(self.my_api_file, 'w') as my_json_file:
            json.dump(self.json_sncf,my_json_file)

    def requestAPI(self,my_password):
        self.my_password = my_password
        r = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas', auth=(my_password, ''))
        print(r.status_code)
        #Récupération des données de la requête
        self.data = r.json()
        
    def writeCSV(self):
        #conversion de mon dict en string
        data_object=json.loads(json.dumps(self.data))
        #je mets dans une variable la liste data_object["stop_areas"]
        listOfAreas = data_object["stop_areas"]
        
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
             #Crash car il y a un 'code' manquant a un moment dans le json
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

    def requestAPIParisLyon(self,my_password):
        self.my_password = my_password
        depart = "stop_area:OCE:SA:87686006"
        arrivee = "stop_area:OCE:SA:87722025"
        URL = f"https://api.sncf.com/v1/journeys?from={depart}&to={arrivee}"
        r = requests.get(URL, auth=(my_password, ''))
        print(r.status_code)
        #Récupération des données de la requête
        self.data2 = r.json()

def writeNewDict ():
    my_dict={}
    my_key=input("KEY:")
    my_value=input("VALUE:")
    my_dict[my_key]=my_value

    return my_dict


SNCF = APItools('stop_areas.json')

#Lire l'API
SNCF.readAPI()

'''
#Ajouter un nouveau dict au JSON existant
SNCF.addNewKey(writeNewDict())


#Ajouter un nouveau dict a la clé ['stop_areas'] du JSON existant
SNCF.addNewStopArea(writeNewDict())


#Afficher le jason file avec pretty_print
SNCF.printWithPrettyPrint()
'''
'''
#https://www.dataquest.io/blog/python-api-tutorial/
#GET request, faire une requete pour avoir des données
API qui n'existe pas
response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print(response.status_code)
API qui existe
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())
'''

#Faire une requete sur l'API de la sncf
#authentification = input("authentification request :")
authentification = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e'
SNCF.requestAPI(authentification)


#SNCF.writeCSV()

#pprint.pprint(SNCF.data)

'''
// https://api.sncf.com/v1/coverage/sncf/journeys

{
  "message": "you should at least provide either a 'from' or a 'to' argument"
}
'''
SNCF.requestAPIParisLyon(authentification)
#print(SNCF.data2)
#pprint.pprint(SNCF.data2)
#        depart = "stop_area:OCE:SA:87686006"
#       arrivee = "stop_area:OCE:SA:87722025"
#URL = f"https://api.sncf.com/v1/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"

list_arret=[]
acces_arret = SNCF.data2["journeys"][0]["sections"][1]["stop_date_times"]
for arret in acces_arret:
    print(arret["stop_point"]["name"])
    list_arret.append(arret["stop_point"]["name"])


    #https://openclassrooms.com/forum/sujet/soustraire-deux-dates-pour-recuperer-temps-restant
    base_arrival = arret["base_arrival_date_time"]
    base_arrival_date_format=datetime.datetime.strptime(base_arrival, "%Y%m%dT%H%M%S")
    #print(base_arrival_date_format)
    base_departure = arret["base_departure_date_time"]
    base_departure_date_format=datetime.datetime.strptime(base_departure, "%Y%m%dT%H%M%S")
    
    temps_arret = (base_departure_date_format - base_arrival_date_format)
    print("temps d'arret: ",temps_arret)


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
'''

#Faire une request sur une heure précise (ici la date d'aujoud'hui + 18h00) entre Paris Gare de Lyon et Lyon Perrache
#https://api.navitia.io/v1/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025&datetime=20140425T1337
#https://api.sncf.com/v1/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025&datetime=20210125T180000


min_date_time ="20210125T150000"
all_departure_from =[]
all_departure_from.append(min_date_time)

authentification = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e'
depart = "stop_area:OCE:SA:87686006"
arrivee = "stop_area:OCE:SA:87722025"

for i in range (0,10):
    URL = f"https://api.sncf.com/v1/journeys?from={depart}&to={arrivee}&datetime={all_departure_from[i]}"
    r = requests.get(URL, auth=(authentification, ''))

    #Récupération des données de la requête
    data3 = r.json()
    #print(data3)

    next_departure = data3["journeys"][0]["departure_date_time"]
    print(next_departure)
    next_departure=next_departure [:-1] + "1"
    next_departure_date_format=datetime.datetime.strptime(next_departure, "%Y%m%dT%H%M%S")
    all_departure_from.append(next_departure)
    print(all_departure_from)