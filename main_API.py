from flask import Flask, jsonify, request, abort
from Classes.manageIntervention import ManageIntervention

main_API = Flask(__name__)

@main_API('/EasySAV/Travail', methods={'POST'})
def travail():
    message = request.get_json(force=True)
    BaseDD = ManageIntervention()
    if "intervenant" in message:
        dictionnaire_interventions = BaseDD.liste_intervention(message["intervenant"])
        return jsonify(dictionnaire_interventions)
    else :
        abort(406)

@main_API('/EasySAV/AjoutIntervention', methods={'POST'})
def ajout_intervention():
    message = request.get_json(force=True)
    BaseDD = ManageIntervention()
    if "intervenant" in message and "date" in message and "adresse" in message and "modalite" in message:
        try :
            BaseDD.ajout_intervention(message["intervenant"], message["date"], message["adresse"], message["modalite"])
        except:
            abort(500)
    else:
        abort(406)


if __name__ == '__main__':
    main_API.run()