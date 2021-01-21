import json
import pprint

with open('stop_areas.json') as my_json_file:
    data_sncf=my_json_file.read()
    json_sncf=json.loads(data_sncf)

pprint.pprint(json_sncf)


#custom_gare = 'Gare du Tieks'
#data_sncf[0]['My_game'] = custom_gare

#Ajouter une nouvelle 'key':'value' de mon json file
custom = {'My_gare':'Gare_du_tieks'}
json_sncf.update(custom)


#Ajouter une nouvelle gare a la key existante 'stop_areas'
json_sncf['stop_areas'].append({'My_gare':'Gare_du_tieks'})


with open('stop_areas.json', 'w') as my_json_file:
    json.dump(json_sncf,my_json_file)

with open('stop_areas.json') as my_json_file:
    data_sncf=my_json_file.read()
    json_sncf=json.loads(data_sncf)

pprint.pprint(json_sncf)