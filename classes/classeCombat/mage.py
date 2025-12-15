from classes.classeSort import Sort 
class Mage():
    def __init__(self):
        self.magie=3
        self.faiblesse="tranchant"
        self.resistance="foudre"
        self.nom="Mage"
        self.capacite="Ses sorts offensifs infligent 15%"+" de dégats supplémentaires"
    def power(self,methode,var):
        if methode=="attaque":
            if type(var[1])==Sort:
                var[2]*=1.15
                return var[2]
        return 