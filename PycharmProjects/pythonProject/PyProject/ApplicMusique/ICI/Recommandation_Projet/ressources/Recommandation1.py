class Recommandation:
    def __init__(self,
                 _nom_recommandation,
                 _le_contexte,
                 _etiquettes: list,
                 _note_recommandation):
        self._nom_recommandation = _nom_recommandation   # Nom
        self._le_contexte = _le_contexte
        self._etiquettes = _etiquettes
        self._note_recommandation = _note_recommandation   # Note


    def get_nom_recommandation(self):    # accesseur
        return self._nom_recommandation

    def get_note_recommandation(self):    # accesseur
        return self._note_recommandation
    
    def change_note(self, nouvelle_note=''):
        self._note_recommandation = nouvelle_note

    def ajoute_etiquette(self, etiquette):
        self._etiquettes.append(etiquette)
