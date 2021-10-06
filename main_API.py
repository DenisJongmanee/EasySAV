from flask import Flask, jsonify, request, abort
from Classes.manageIntervention import ManageIntervention

main_API = Flask(__name__)

@main_API.route('/EasySAV/Travail/<int:intervenant>')
def travail(intervenant):
    try:
        BaseDD = ManageIntervention()

        dictionnaire_interventions = BaseDD.liste_intervention(intervenant)

        return jsonify(dictionnaire_interventions)
    except:
        abort(500)

@main_API.route('/EasySAV/AjoutIntervention', methods={'POST'})
def ajout_intervention():
    message = request.get_json(force=True)
    BaseDD = ManageIntervention()
    if "intervenant" in message and "date" in message and "adresse" in message and "modalite" in message:
        try :
            BaseDD.ajout_intervention(message["intervenant"], message["date"], message["adresse"], message["modalite"])
            return "Ok"
        except:
            abort(500)
    else:
        abort(406)


if __name__ == '__main__':
    main_API.run()