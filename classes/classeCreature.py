from classes.classePerso import Perso
class Creature(Perso):
    def __init__(self,payload):
        super().__init__(payload)
        print(self.nom,"vous fait face !")

    def copie(self,nom="") :
        if nom =="":
            nom= self.nom
        return Creature({
            "nom" : nom,
            "force" : self.force,
            "habilité" : self.habilité,
            "constitution" : self.constitution,
            "charisme" : self.charisme,
            "foi" : self.foi,
            "classe" : str(self.classe),
            "inventaire" : self.inventaire,
            "dieux" : self.dieux,
            "niveau" :  self.niv,
            "coordX" : -1,
            "coordY" : -1,
        })
    