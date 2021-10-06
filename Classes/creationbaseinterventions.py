import sqlite3

connexionBDD = sqlite3.connect("../Bases_de_donnees/EasySaves.db")
curseurBDD = connexionBDD.cursor()

instructionBDD = f"CREATE TABLE IF NOT EXISTS intervention("\
                f"id_intervention INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,"\
                f"id_intervenant INTEGER,"\
                f"date_horaire DATE,"\
                f"adresse TEXT,"\
                f"modalite TEXT)"

curseurBDD.execute(instructionBDD)
connexionBDD.commit()
connexionBDD.close()