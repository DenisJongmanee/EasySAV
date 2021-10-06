import sqlite3

class ManageIntervention:
    def __init__(self):
        self.connexionBDD = sqlite3.connect("../Bases_de_donnees/EasySaves.db")
        self.curseurBDD = self.connexionBDD.cursor()

    def ajout_intervention(self):
        pass

    def liste_intervention(self):
        pass