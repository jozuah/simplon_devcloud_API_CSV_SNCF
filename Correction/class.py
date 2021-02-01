import json
import requests
import csv
import pandas as pd
import pprint
import os
import unittest

class ReadSncfApi():

    def __init__(self):
        self.url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
        self.headers = {"Authorization": "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}
        self.list_hrefs = []
        self.filename_json = 'stop_areas_maria' # we don't put .json, see line 22 with open
        self.filename_csv = 'maria_csv'

    def read_json(self):  # reads and saves json

        response = requests.get(self.url, headers=self.headers) #headers1 is a name of the parameter, second = my real header which I pass

        with open(self.filename_json + '.json', mode="w") as file:
            json.dump(response.json(), file)

    def read_links(self):

        with open(self.filename_json + '.json') as json_stop_areas_file:
            data = json.load(json_stop_areas_file)

        links = data['links'] # 11 dict with 1 href in each

        for loop_link in links:

            if type(loop_link) == dict:
                if "href" in loop_link.keys():
                    local_href = loop_link["href"]
                    self.list_hrefs.append(local_href)
                else:
                    print("Missing key id")
            else:
                print(f"Unexpected format {type(loop_link)}") 

    def save_csv(self): 
        with open(self.filename_csv + '.csv', mode="w", newline='') as f:
            csv_writer = csv.writer(f, delimiter=';')
            if type(self.list_hrefs) == list:
                for row in self.list_hrefs:
                    csv_writer.writerow(row)
            else: 
                print("Unexpected input")
            print("csv ok") # test