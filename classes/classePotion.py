from classes.classeSort import Sort


class Potion(Sort) :
    def __init__(self, nom, mini, maxi, type, stat="esprit", heal=0, nbroll=1):
        super().__init__(nom, mini, maxi, type, stat, heal, nbroll)
    def __str__(self):
        if self.heal :
            return f"\n\nNom de la potion : **{self.nom}**\n\t↳soin : {self.mini} à {self.maxi}\n\t↳type de heal : {self.type} {self.desc[0]}\n\t↳stat améliorante : {self.stat} {self.desc[1]}"
        return f"\n\nNom de la potion : **{self.nom}**\n\t↳dégats : {self.mini} à {self.maxi}\n\t↳type de dégat : {self.type} {self.desc[0]}\n\t↳stat améliorante : {self.stat} {self.desc[1]}"
    def __repr__(self):
        return str(self)