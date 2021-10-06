import sqlite3

class ManageIntervention:
    def __init__(self):
        self.connexionBDD = sqlite3.connect("../Bases_de_donnees/EasySaves.db")
        self.curseurBDD = self.connexionBDD.cursor()

    def ajout_intervention(self, intervenant, date, adresse, modalite):
        instructionBDD = f"INSERT INTO intervention (id_intervenant, date_horaire, addresse, modalite) "\
                        f"VALUES ({intervenant}, {date}, {adresse}, {modalite})"
        self.curseurBDD.execute(instructionBDD)
        self.connexionBDD.commit()

    def liste_intervention(self, intervenant):
        pass