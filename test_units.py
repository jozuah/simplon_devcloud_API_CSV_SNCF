import unittest
import script_class
import os

class Test_file(unittest.TestCase):
    '''
    #Test que le fichier exist
    def test_check_file_exist_readAPI(self):
        directory_path = './stop_areas.json' # somepath
        self.assertTrue(os.path.exists(directory_path)) 
    
    #Test le fichier renvoi bien un dictionnaire   
    def test_readAPI(self):
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e' 
        SNCF = script_class.APItools(password,'stop_areas.json')
        SNCF.readAPI()
        self.assertTrue(type(SNCF.data_sncf)==dict)

    def test_writeNewDict_return_dict(self):
        self.assertEqual(type(script_class.writeNewDict()),dict)

    
    def test_AddNewKeyValuePair(self):
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e' 
        SNCF = script_class.APItools(password,'stop_areas.json')
        
        new_dict = script_class.writeNewDict()
        
        SNCF.readAPI()
        SNCF.addNewKeyValuePair(new_dict)
        #Cette ligne renvoie true SI le petit dict est bien dans le
        #grand dict
        my_test=set(new_dict).issubset(set(SNCF.data_sncf))
        #Je test que my_test renvoie True
        self.assertTrue(my_test)
    

    #Cette fonction ne fonctionne pas encore 
    def test_AddNewStopArea(self):
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e' 
        SNCF = script_class.APItools(password,'stop_areas.json')
        
        new_dict = script_class.writeNewDict()
        
        SNCF.readAPI()
        SNCF.addNewStopArea(new_dict)
        #Cette ligne renvoie true SI le petit dict est bien dans le
        #grand dict
        my_test=set(new_dict).issubset(set(SNCF.data_sncf['stop_areas']))
        #Je test que my_test renvoie True
        self.assertTrue(my_test) 
    
    def test_data_vide(self):
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e'
        SNCF = script_class.APItools(authentification=password)
        self.assertEqual(SNCF.data, None)

    def test_data_with_json_file(self):
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e' 
        SNCF = script_class.APItools(authentification=password)   
        SNCF.requestAPI()
        self.assertTrue(type(SNCF.data)==dict)

    def test_list_for_csv_file_not_empty(self):
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e' 
        SNCF = script_class.APItools(authentification=password)   
        SNCF.requestAPI()
        SNCF.writeCSV()
        #Verification que le dict final dict a été créé et qu'il n'est
        #pas vide sinon return False
        self.assertTrue(SNCF.final_dict)
    
    #Test que le fichier exist
    def test_check_CSV_file_exist(self):
        directory_path = './sncf.csv' # somepath
        self.assertTrue(os.path.exists(directory_path))
    
    #Test que la requête a aboutit
    def test_request_is_complete (self):
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e' 
        SNCF = script_class.APItools(authentification=password)   
        SNCF.requestAPIParisLyon()
        #si le status code est 200 tout est good
        self.assertEqual(SNCF.r.status_code,200)   

    #Test que je récupère bien un dictionnaire en fin de fonction
    def test_requestAPIParisLyon_return_dict (self):
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e' 
        SNCF = script_class.APItools(authentification=password)   
        SNCF.requestAPIParisLyon()
        self.assertTrue(type(SNCF.data2)==dict)
    

    def test_all_stop_points_exists(self):  
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e' 
        SNCF = script_class.APItools(authentification=password)   
        SNCF.requestAPIParisLyon()
        SNCF.areasSTOPSParisLyon()
        self.assertTrue(SNCF.list_arret)         
    '''
if __name__ == '__main__':
    #Verbosity indique le nombre d'info que va retourner l'execution
    #de mes tests
    unittest.main(verbosity=2)


