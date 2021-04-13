from Recommandation1 import Recommandation


class Musique(Recommandation):
    def __init__(self,
                 _nom_artistes,
                  _le_contexte,
                 _etiquettes,
                 _note_recommandation,
                 _lien_pour_ecoute):

        super().__init__(_nom_artistes, _le_contexte, _etiquettes,  _note_recommandation)
        self._lien_pour_ecoute = _lien_pour_ecoute
        self._nom_artistes = _nom_artistes



    def get_lien_pour_ecoute(self):  # accesseur
        return self._lien_pour_ecoute

    def get_nom_artistes(self):   # accesseur
        return self._nom_artistes

    def set_lien_pour_ecoute(self, _lien_pour_ecoute):
        self._lien_pour_ecoute = _lien_pour_ecoute


print("instanciation d'un object de type Musique")
a = Musique("lady gaga", "Musique", ["top", "cool"], "4", "www.ladygaga.com")
print(a)
print("lien d'écoute: ", a.get_lien_pour_ecoute())
print("Nom de l'artiste: ", a.get_nom_artistes())

# appel des méthodes de la classe parente
print(a.get_nom_recommandation())
print(a.get_note_recommandation())
