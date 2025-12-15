class Paladin():
    def __init__(self):
        self.magie=2
        self.faiblesse="impact"
        self.resistance="sacre"
        self.nom="Paladin"
        self.capacite="Augmente les soins que vous donnez"
    def power(self,methode,var):
        if methode=="heal":
            var+=3
            return var