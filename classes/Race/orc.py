class Orc():
    def __init__(self):
        self.magie=1
        self.faiblesse="impact"
        self.resistance="feu"
        self.nom="Orc"
        self.capacite="Augmente de 4 le résultat d'un roll force (jusqu'à 19), mais réduit ceux d'esprit, d'eloquence et d'intelligence de 2  (minimum 1)"
    def power(self,methode,var):
        if methode=="roll":
            if var[0] in "force":
                var[1]+=4
                return min(var[1],19)
            if var[0] in "esprit" or var[0] in "intelligence" or var[0] in "eloquence":
                var[1]-=2
                return max(var[1],1)
            