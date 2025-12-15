class Archer():
    def __init__(self):
        self.magie=1
        self.faiblesse="tranchant"
        self.resistance="foudre"
        self.nom="Archer"
        self.capacite=" Augmente de 2 le résultat d'un roll perception (jusqu'à 19)"
    def power(self,methode,var):
        if methode=="roll":
            if var[0] in "perception":
                var[1]+=2
            return min(var[1],19)