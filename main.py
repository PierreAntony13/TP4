from noeuds import Noeud

deux = Noeud(2)
y = Noeud("y")
plus = Noeud("+", [deux, y])
exp = Noeud("exp")
exp.ajouter_enfant(plus)
exp.afficher() # Doit afficher : exp + 2 y
print()

val_dict = {
'y': 2
}
print(plus.evaluer(val_dict))
print(exp.evaluer(val_dict))