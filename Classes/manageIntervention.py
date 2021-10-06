import sqlite3

class ManageIntervention:
    def __init__(self):
        self.connexionBDD = sqlite3.connect("../Bases_de_donnees/EasySaves.db")
        #connexion à la base de donnée
        self.curseurBDD = self.connexionBDD.cursor()

    def ajout_intervention(self, intervenant, date, adresse, modalite):
        #methode pour ajouter une intervention
        instructionBDD = f"INSERT INTO intervention (id_intervenant, date_horaire, adresse, modalite) "\
                        f"VALUES ({intervenant}, '{date}', '{adresse}', '{modalite}')"
        self.curseurBDD.execute(instructionBDD)
        #creation d'une intervention
        self.connexionBDD.commit()

    def liste_intervention(self, intervenant):
        #methode
        instructionBDD = f"SELECT * FROM intervention WHERE id_intervenant = {intervenant}"
        self.curseurBDD.execute(instructionBDD)
        dictionnaire_retour = {}
        indexe = 1
        # creration variable indexe = 1 correspond au numero de l'intervention
        for ligne in self.curseurBDD:
            dictionnaire_ligne = {}
            dictionnaire_ligne["intervention"] = indexe
            dictionnaire_ligne["date_horaire"] = ligne[2]
            dictionnaire_ligne["adresse"] = ligne[3]
            dictionnaire_ligne["modalite"] = ligne[4]
            indexe += 1 #incrémente le numero d'intervention
            dictionnaire_retour[indexe] = dictionnaire_ligne
        return dictionnaire_retour