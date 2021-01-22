import json
import pprint
import requests
import csv

#ouvrir et lire mon json
with open('stop_areas.json') as my_json_file:
    data_sncf=my_json_file.read()
    json_sncf=json.loads(data_sncf)

'''
pprint.pprint(json_sncf)
'''

#custom_gare = 'Gare du Tieks'
#data_sncf[0]['My_game'] = custom_gare

#Ajouter une nouvelle 'key':'value' de mon json file
custom = {'My_gare':'Gare_du_tieks'}
json_sncf.update(custom)


#Ajouter une nouvelle gare a la key existante 'stop_areas'
json_sncf['stop_areas'].append({'My_gare':'Gare_du_tieks'})

#ecrire dans mon json
with open('stop_areas.json', 'w') as my_json_file:
    json.dump(json_sncf,my_json_file)
'''
with open('stop_areas.json') as my_json_file:
    data_sncf=my_json_file.read()
    json_sncf=json.loads(data_sncf)

pprint.pprint(json_sncf)
'''
#https://www.dataquest.io/blog/python-api-tutorial/
#GET request, faire une requete pour avoir des données

'''
API qui n'existe pas
response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
print(response.status_code)
API qui existe
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())
'''
#https://2.python-requests.org/en/master/
#r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r = requests.get('https://api.sncf.com/v1/coverage/sncf/stop_areas', auth=('8d148dd0-f46d-4e1e-9afd-d9a82d40b90e', ''))
r.status_code
print(r.status_code)
#print(r.json())
#pprint.pprint(r.json())

data = r.json()
#conversion de mon dict en string
data_object=json.loads(json.dumps(data))


'''
a = json.loads('{"X":"value1","Y":"value2","Z":[{"A":"value3","B":"value4"}]}')
>>> a
{'Y': 'value2', 'X': 'value1', 'Z': [{'A': 'value3', 'B': 'value4'}]}
>>> a["Z"][0]["A"]
'value3'
'''
#a = json.loads('{"X":"value1","Y":"value2","Z":[{"A":"value3","B":"value4"}]}')

print(type(data_object))
#print(a["Z"][0]["A"])
#print(data_object["stop_areas"]["admnistrative_regions"][0]["name"])

#print(data_object["stop_areas"])
#je mets dans une variable la liste data_object["stop_areas"]
listOfAreas = data_object["stop_areas"]


#for i in range (len(listOfAreas)):
    #print(listOfAreas[i])

    #Le print issue de "administrative_regions" ne fonctionne pas tjrs car 
    # certaine données n'ont pas le administrative_regions"
    #print("\n",listOfAreas[i]["administrative_regions"][0]['name'])
    
    #Je print les ville situés dans 'label'
    #print("\nVille:",listOfAreas[i]["label"], "Code:",listOfAreas[i]["codes"],"Coordonnés:",listOfAreas[i]["coord"])


''' Fonctionne mais affiche les noms des villes avec un caractère par colonne
with open('sncf.csv', 'w', newline='') as my_csv_file:
    stylo = csv.writer(my_csv_file)
    for i in range (len(listOfAreas)):
        #stylo.writerow([listOfAreas[i]["label"],listOfAreas[i]["codes"] , listOfAreas[i]["coord"])
        stylo.writerow(listOfAreas[i]["label"])
'''

#Définition des colonnes pour mon csv
csv_colonnes = ['numCol','Codes','Nom','Coord']
with open('sncf.csv', 'w', newline='') as my_csv_file:
    stylo = csv.DictWriter(my_csv_file,fieldnames = csv_colonnes)
    #Permet d'ecrire la premiere ligne avec les colonnes définis
    stylo.writeheader()
    #Crash car il y a un 'code' manquant a un moment dans le json
    for i in range (5):
        #je créé mon dictionnaire pour utiliser le DictWriter, je fais correspondre mes key avec ceux des colonnes définies
        d={'numCol':i,'Codes':listOfAreas[i]["codes"], 'Nom':listOfAreas[i]["label"],'Coord':listOfAreas[i]["coord"]}
        stylo.writerow(d)
 
''' Ce code fonctionne
csv_columns = ['No','Name','Country']
dict_data = [
{'No': 1, 'Name': 'Alex', 'Country': 'India'},
{'No': 2, 'Name': 'Ben', 'Country': 'USA'},
{'No': 3, 'Name': 'Shri Ram', 'Country': 'India'}]

with open('sncf.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)
'''
''' Voir la page + code
https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file
The csv module contains DictWriter method that requires name of csv file to write and a list object containing field names. The writeheader() method writes first line in csv file as field names. The subsequent for loop writes each row in csv form to the csv file.

import csv
csv_columns = ['No','Name','Country']
dict_data = [
{'No': 1, 'Name': 'Alex', 'Country': 'India'},
{'No': 2, 'Name': 'Ben', 'Country': 'USA'},
{'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
{'No': 4, 'Name': 'Smith', 'Country': 'USA'},
{'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
]
csv_file = "Names.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
'''