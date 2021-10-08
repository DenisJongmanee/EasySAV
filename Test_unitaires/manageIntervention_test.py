import unittest
from Classes.manageIntervention import ManageIntervention

class ManageInterventionTestCase(unittest.TestCase):


    def test_ajout_intervention(self):
        #Arrange
        manageIntervention = ManageIntervention()

        manageIntervention.ajout_intervention(100, '2021-10-06 20:00:00', 'testAdresse','test')
        lastId = manageIntervention.curseurBDD.lastrowid

        #Act
        cmdSelect = f"SELECT * FROM intervention WHERE id_intervention = {lastId} "
        manageIntervention.curseurBDD.execute(cmdSelect)

        # Assert
        for row in manageIntervention.curseurBDD:
            self.assertEqual(row[1], 100)
            self.assertEqual(row[2], '2021-10-06 20:00:00')
            self.assertEqual(row[3], 'testAdresse')
            self.assertEqual(row[4], 'test')

        cmdDelete = f"DELETE FROM intervention WHERE id_intervention = {lastId}"
        manageIntervention.curseurBDD.execute(cmdDelete)
        manageIntervention.connexionBDD.commit()

    def test_liste_intervention(self):
        #Arrange
        manageIntervention = ManageIntervention()

        manageIntervention.ajout_intervention(22, '2021-10-06 20:00:00', 'testAdresse','test')
        ajout1 = manageIntervention.curseurBDD.lastrowid
        manageIntervention.ajout_intervention(22, '2021-10-07 20:20:20', 'testAdresse2', 'test')
        ajout2 = manageIntervention.curseurBDD.lastrowid

        #Act
        listIntervention = manageIntervention.liste_intervention(22)
        intervention1 = {"intervention" : 1, "date_horaire" : '2021-10-06 20:00:00', "adresse" : 'testAdresse', "modalite" : "test" }
        intervention2 = {"intervention" : 2, "date_horaire" : '2021-10-07 20:20:20', "adresse" : 'testAdresse2', 'modalite' : 'test'}
        listInterventionTest = {1 : intervention1, 2 : intervention2 }

        #Assert
        self.assertEqual(listIntervention, listInterventionTest)


        cmdDelete = f"DELETE FROM intervention WHERE id_intervention = {ajout1}"
        manageIntervention.curseurBDD.execute(cmdDelete)

        cmdDelete = f"DELETE FROM intervention WHERE id_intervention = {ajout2}"
        manageIntervention.curseurBDD.execute(cmdDelete)
        manageIntervention.connexionBDD.commit()

if __name__ == '__main__':
    unittest.main()
