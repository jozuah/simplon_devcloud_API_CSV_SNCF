import unittest
import script_class

class Test_file(unittest.TestCase):

    def test_data_vide(self):
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e'
        SNCF = script_class.APItools(authentification=password)
        self.assertEqual(SNCF.data, None)

    def test_data_with_json_file(self):
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e' 
        SNCF = script_class.APItools(authentification=password)   
        SNCF.requestAPI()
        self.assertTrue(type(SNCF.data)==dict)

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
            


if __name__ == '__main__':
    #Verbosity indique le nombre d'info que va retourner l'execution
    #de mes tests
    unittest.main(verbosity=2)


