from classes.classePerso import Perso
class Creature(Perso):
    def __init__(self,nom,force,dex,intel,end,perception,eloquence,esprit,magie,race,classe):
        super().__init__(nom,force,dex,intel,end,perception,eloquence,esprit,magie,race,classe)
        print(self.nom,"vous fait face !")

    def copie(self,nom="") :
        if nom =="":
            nom= self.nom
        return Creature(nom,self.force,self.dex,self.intel,self.end,self.perception,self.eloquence,self.esprit,self.magie,self.race,self.classe)
    