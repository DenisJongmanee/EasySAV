import sqlite3

class ManageIntervention:
    def __init__(self):
        self.connexionBDD = sqlite3.connect("../Bases_de_donnees/EasySaves.db")
        self.curseurBDD = self.connexionBDD.cursor()

    def ajout_intervention(self, intervenant, date, adresse, modalite):
        instructionBDD = f"INSERT INTO intervention (id_intervenant, date_horaire, adresse, modalite) "\
                        f"VALUES ({intervenant}, '{date}', '{adresse}', '{modalite}')"
        self.curseurBDD.execute(instructionBDD)
        self.connexionBDD.commit()

    def liste_intervention(self, intervenant):
        instructionBDD = "SELECT * FROM intervention"
        self.curseurBDD.execute(instructionBDD)
        dictionnaire_retour = {}
        indexe = 1
        for ligne in self.curseurBDD:
            dictionnaire_ligne = {}
            dictionnaire_ligne["intervention"] = indexe
            dictionnaire_ligne["date_horaire"] = ligne.date_horaire
            dictionnaire_ligne["adresse"] = ligne.adresse
            dictionnaire_ligne["modalite"] = ligne.modalite
            indexe += 1
            dictionnaire_retour[indexe] = dictionnaire_ligne
        return dictionnaire_retour