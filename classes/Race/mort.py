class Mort():
    def __init__(self):
        self.magie=2
        self.faiblesse="sacre"
        self.resistance="poison"
        self.nom="Mort"
        self.capacite="Possède du vol de vie sur chaque coup (3 pv a chaque coup)"
    def power(self,methode,var):
        if methode=="attaque":
            var[3].soin(3)
        return