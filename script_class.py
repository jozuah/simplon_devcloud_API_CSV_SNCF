import json
import pprint
import requests
import csv

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
    
    def addNewStopArea(self,newStation):
        self.newStation = newStation
        self.json_sncf['stop_areas'].append(self.newStation)

    def requestAPI(self,my_password):
        self.my_password = my_password
        r = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas', auth=(my_password, ''))
        print(r.status_code)




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
'''
'''
#Ajouter un nouveau dict a la clé ['stop_areas'] du JSON existant
SNCF.addNewStopArea(writeNewDict())
'''
'''
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
authentification = input("authentification request :")
SNCF.requestAPI(authentification)

data = r.json()
#conversion de mon dict en string
data_object=json.loads(json.dumps(data))
#je mets dans une variable la liste data_object["stop_areas"]
listOfAreas = data_object["stop_areas"]