class Elfe():
    def __init__(self):
        self.magie=4
        self.faiblesse="feu"
        self.resistance="poison"
        self.nom="Elfe"
        self.capacite="Augmente de 2 le résultat d'un roll éloquence (jusqu'à 19)"
    def power(self,methode,var):
        if methode=="roll":
            if var[0] in "eloquence":
                return min(var[1]+2,19)