import sqlite3

connexionBDD = sqlite3.connect("EasySaves.db") #Creer la connexion à la base de donnée "EasySaves.db"
curseurBDD = connexionBDD.cursor()

#Creation table intervention avec ses colonnes
instructionBDD = f"CREATE TABLE IF NOT EXISTS intervention("\
                f"id_intervention INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,"\
                f"id_intervenant INTEGER,"\
                f"date_horaire DATE,"\
                f"adresse TEXT,"\
                f"modalite TEXT)"

curseurBDD.execute(instructionBDD)
connexionBDD.commit()
connexionBDD.close() #Fermer connexion à la base de donnée