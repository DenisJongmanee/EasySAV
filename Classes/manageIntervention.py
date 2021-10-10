import sqlite3

class ManageIntervention:
    def __init__(self):
        # connexion à la base de donnée
        self.connexionBDD = sqlite3.connect("../Bases_de_donnees/EasySaves.db")
        self.curseurBDD = self.connexionBDD.cursor()

    def ajout_intervention(self, intervenant, date, adresse, modalite):
        #methode pour ajouter une intervention
        instructionBDD = f"INSERT INTO intervention (id_intervenant, date_horaire, adresse, modalite) "\
                        f"VALUES ({intervenant}, '{date}', '{adresse}', '{modalite}')"
        # creation d'une intervention
        self.curseurBDD.execute(instructionBDD)
        self.connexionBDD.commit()

    def liste_intervention(self, intervenant):
        #methode qui assignent les interventions à leur intervenant
        instructionBDD = f"SELECT * FROM intervention WHERE id_intervenant = {intervenant}"
        self.curseurBDD.execute(instructionBDD)
        dictionnaire_retour = {}
        # creation variable indexe = 1 correspond au numero de l'intervention
        indexe = 1
        for ligne in self.curseurBDD:
            dictionnaire_ligne = {}
            dictionnaire_ligne["intervention"] = indexe
            dictionnaire_ligne["date_horaire"] = ligne[2]
            dictionnaire_ligne["adresse"] = ligne[3]
            dictionnaire_ligne["modalite"] = ligne[4]
            dictionnaire_retour[indexe] = dictionnaire_ligne
            indexe += 1  # incrémente le numero d'intervention
        return dictionnaire_retour