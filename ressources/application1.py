# - Importations et fonctions ----------------

import os
import json
from musique_recommandation1 import Musique
from Recommandation1 import Recommandation

# -----------  Classes -----------------------------


class Application:

    """
    Trouve et retourne des fichiers correspondants à noms_prenoms_etudiants.json & recommandations.json
    """
    cwd = os.getcwd() # get the current working dir

    _dossier_courant = cwd
    files = os.listdir(cwd) # get all files in that dir
    print(files)

    _chemin_fichier_etudiants = os.path.join(_dossier_courant, "noms_prenoms_etudiants.json")
    _chemin_fichier_recommandations = os.path.join(_dossier_courant, "recommandations.json")

    # -----------  Constructeur -----------------------------

    def __init__(self, etiquettes):
        """
         Initialise une collection d'étudiants
        """
        self._dico_etudiants = self._recupere_liste_etudiants()



    def _recupere_liste_etudiants(self):
        """
        Retourne la liste d'étudiants appropriée
        """
        etudiants = None
        with open(self._chemin_fichier_etudiants, "r", encoding='utf-8') as fichier_etudiants:
            etudiants = json.load(fichier_etudiants)

        return etudiants


    def _recupere_recommandations_du_fichier(self):
        """
        Examine si le fichier de Recommandation se trouve dans l'active directory ou en crée un nouveau
        """

        if os.path.basename(self._chemin_fichier_recommandations) not in os.listdir(self._dossier_courant):
            with open(self._chemin_fichier_recommandations, "w", encoding='utf-8') as newfile:
                json.dump({'Muisque': []}, newfile)

        with open(self._chemin_fichier_recommandations, "r", encoding='utf-8') as fichier_recommandations:
            return json.load(fichier_recommandations) # conversion des données de format.json en py



    def ajoute_recommandation(self, confirmation=False):
        """
        Création d'un object de type musique et extraction de ses attributs dans des variables exploitables
        """

        recommandations = self._recupere_recommandations_du_fichier()
        musique = self._cree_musique()
        lien = musique._lien_pour_ecoute
        nom = musique._nom_artistes
        note = musique._note_recommandation
        etiquettes = musique._etiquettes
        recommandations['Musique'].append({'nom': nom,
                                                   'lien': lien,
                                                   'note': note,
                                                   'etiquettes': etiquettes})

        confirmation = True if input('Confirmez l"ajout [y/n]:') in ('y', 'yes') else confirmation

        if confirmation:
            with open(self._chemin_fichier_recommandations, "w", encoding='utf-8') as fichier_recommandations:
                json.dump(recommandations, fichier_recommandations)
        return confirmation


    @staticmethod
    def _cree_musique():
        """
        Fonction appelante au service des ajouts
        """
        nom_de_lartiste = input('Entrez le nom de l"artiste').replace(' ', '')
        nom_de_loeuvre = input('Entrez le nom de l"oeuvre').replace(' ', '')
        etiquettes = input('Entrez les étiquettes séparées par un espace.').split()
        note = input("Entrez la note correspondante :")
        lien_pour_ecoute = 'www.youtube.com/' + nom_de_lartiste + '_' + nom_de_loeuvre
        return Musique(nom_de_lartiste, nom_de_loeuvre, etiquettes, note, lien_pour_ecoute)



# ------------ Programme Principal -----------------


recommandNation = Application('')

print(recommandNation)

etudiant = recommandNation._recupere_liste_etudiants()

print("Les étudiaints sauvegardés : \n", etudiant)

recommandation = recommandNation._recupere_recommandations_du_fichier()

print("Les recommandations enregistrées : \n", recommandation )

print(recommandNation.ajoute_recommandation)
recommandNation.ajoute_recommandation()





