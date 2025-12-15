class Berserker:
    def __init__(self):
        self.magie=1
        self.faiblesse="tranchant"
        self.resistance="feu"
        self.nom="Berserker"
        self.capacite="Augmente de 2 le résultat d'un roll force (jusqu'à 19)"
    def power(self,methode,var):
    	if methode=="roll":
            if var[0] in "force":
                var[1]+=2
            return min(var[1],19)