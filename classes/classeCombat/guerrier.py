class Guerrier():
    def __init__(self):
        self.magie=2
        self.faiblesse="impact"
        self.resistance="tranchant"
        self.nom="Guerrier"
        self.capacite="Réduit de 2 les dégats subits"
    def power(self,methode,var):
        if methode=="subitdegat":
            var[0]-=2
            return max(var[0],0)
        return