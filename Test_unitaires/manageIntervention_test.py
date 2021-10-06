import unittest
from Classes.manageIntervention import ManageIntervention

class ManageInterventionTestCase(unittest.TestCase):


    def test_ajout_intervention(self):
        manageIntervention = ManageIntervention()

        manageIntervention.ajout_intervention(1, '2021-10-06 20:00:00', 'testAdresse','test')

        cmdSelect = f"SELECT * FROM intervention WHERE id_intervention = {manageIntervention.curseurBDD.lastrowid} "

        manageIntervention.curseurBDD.execute(cmdSelect)
        for row in manageIntervention.curseurBDD:
            self.assertEqual(row[1], 1)
            self.assertEqual(row[2], '2021-10-06 20:00:00')
            self.assertEqual(row[3], 'testAdresse')
            self.assertEqual(row[4], 'test')



if __name__ == '__main__':
    unittest.main()
