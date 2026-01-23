from classes.classePotion import Potion
from classes.classePerso import Perso


class PotionEffet(Potion) :
    def __init__(self, nom, effect ,descEffet, duree= 0):
        self.nom=nom
        self.effect =effect
        self.effectDescription = descEffet
        self.duree=duree
    def __str__(self):
        descriptionEffet ="\nEffet de la potion : "+str(self.effectDescription) 
        return f"\n\nNom de la potion : **{self.nom}**{descriptionEffet}\n Durée de l'effet : {self.duree}"
    def __repr__(self):
        return str(self)
    def effet(self,buveur : Perso,turnNumber) :
        self.effect(buveur,turnNumber)