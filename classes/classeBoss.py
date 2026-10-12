from classes.classePerso import Perso
class Boss(Perso):
    def __init__(self,payload):
        super().__init__(payload)
        print(self.nom,"apparaît...")
        
    def attaque(self,qql,arme,coef=1.3,critique = False):
        super().attaque(qql,arme,coef,critique)