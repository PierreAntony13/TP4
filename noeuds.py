import numpy as np

class Noeud:
    """Classe représentant un noeud d'un arbre.
    Attributs:----------- valeur : str | float | int
    La valeur du noeud, qui peut être une constante, une variable ou une
    opération.- enfants : list[Noeud]
    La liste des enfants du noeud.
    """

    def __init__(self, valeur, enfants=None):
        if enfants is None:
            enfants = []
        self.enfants = enfants
        self.valeur = valeur

    def ajouter_enfant(self, enfant):
        """Ajoute un enfant au noeud.
        Parametres---------
        enfant : Noeud
        Le noeud enfant à ajouter.
        """
        self.enfants.append(enfant)

    def afficher(self):
        """Affichage polonais du noeud et de ses enfants.
        """
        print(self.valeur, end=" ")
        for i, enfant in enumerate(self.enfants):
            enfant.afficher()

    def evaluer(self, value_dict):
        """Évalue le noeud en fonction de sa valeur et de ses enfants.
        Parameters:----------
        value_dict : dict[str, int | float]
        Dictionnaire contenant les valeurs des variables.
        Returns:-------
        int | float
        La valeur évaluée du noeud.
        """
        # Cas 1: c'est une constante
        if isinstance(self.valeur, (int, float)):
            return self.valeur
        # Cas 2: c'est une variable
        if self.valeur in value_dict:
            return value_dict[self.valeur]
        # Cas 3: c'est une opération
        if len(self.enfants) > 0:
            if self.valeur == '+':
                return self.enfants[0].evaluer(value_dict) + self.enfants[1].evaluer(value_dict)
            elif self.valeur == '-':
                return self.enfants[0].evaluer(value_dict)- self.enfants[1].evaluer(value_dict)
            elif self.valeur == '*':
                return self.enfants[0].evaluer(value_dict) * self.enfants[1].evaluer(value_dict)
            elif self.valeur == '/':
                return self.enfants[0].evaluer(value_dict) / self.enfants[1].evaluer(value_dict)
            elif self.valeur == 'exp':
                return np.exp(self.enfants[0].evaluer(value_dict))
            elif self.valeur == 'log':
                return np.log(self.enfants[0].evaluer(value_dict))
            elif self.valeur == 'sin':
                return np.sin(self.enfants[0].evaluer(value_dict))
            elif self.valeur == 'cos':
                return np.cos(self.enfants[0].evaluer(value_dict))
    
        raise ValueError(f"Opération ou variable inconnue: {self.valeur}")