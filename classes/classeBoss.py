from random import randint 
from classes.classeArme import Arme
from classes.classeArmeLegendaire import ArmeLegendaire
from classes.classePerso import Perso
class Boss(Perso):
    def __init__(self,nom,force,dex,intel,end,perception,eloquence,esprit,magie,race,classe):
        super().__init__(nom,force,dex,intel,end,perception,eloquence,esprit,magie,race,classe)

        self.pv = 30 + 12*end
        self.maxpv= 30 + 12*end
        print(self.nom,"apparaît...")
        
    def attaque(self,qql,arme,coef=1.3):
        super().attaque(qql,arme,coef)