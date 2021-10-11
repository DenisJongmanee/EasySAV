import json
import unittest
from EasySAV.main_API import main_API

from flask import jsonify

class MainAPITestCase(unittest.TestCase):

    def setUp(self):
        #Arrange
        main_API.config["TESTING"] = True
        main_API.config["DEBUG"] = True
        self.app = main_API.test_client()

    def test_route_travail(self):
        # Act
        response = self.app.get("/EasySAV/Travail/666")
        interventions = json.loads(response.data)
        # Assert
        self.assertEqual(response.status_code, 200)


    def test_route_ajout_intervention(self):
        # Act
        data = '{ "intervenant" : 1001 , "date" : "2021-10-06 21:00:00", "adresse" : "EPSI", "modalite" : "reparation"}'
        response = self.app.post("/EasySAV/AjoutIntervention", data = data)
        # Assert
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
