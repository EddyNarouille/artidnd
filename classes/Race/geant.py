class Geant():
    def __init__(self):
        self.magie=1
        self.faiblesse="perçant"
        self.resistance="impact"
        self.nom="Géant"
        self.capacite="Réduis les dégats subits de 1 et augmente de 2 le résultat d'un roll force (jusqu'à 19)"
    def power(self,methode,var):
        if methode=="roll":
            if var[0] in "force":
                var[1]+=2
            return min(var[1],19)
        if methode=="subitdegat":
            var[0]-=1
            return max(var[0],0)
        return