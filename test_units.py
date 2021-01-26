import unittest
from script_class import APItools

class Test_file(unittest.TestCase):

    def test_data_vide(self):
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e'
        SNCF = APItools(authentification=password)
        self.assertEqual(SNCF.data, None)

    def test_data_with_json_file(self):
        password = '8d148dd0-f46d-4e1e-9afd-d9a82d40b90e' 
        SNCF = APItools(authentification=password)   
        SNCF.requestAPI()
        self.assertTrue(type(SNCF.data)==dict)

if __name__ == '__main__':
    #Verbosity indique le nombre d'info que va retourner l'execution
    #de mes tests
    unittest.main(verbosity=2)


