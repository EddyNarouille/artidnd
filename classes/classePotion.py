from classes.classeSort import Sort
from classes.classePerso import Perso


class Potion(Sort) :
    def __init__(self, nom, mini, maxi, type, stat="esprit", heal=0, nbroll=1, effect = None,descEffet="", duree= 0):
        super().__init__(nom, mini, maxi, type, stat, heal, nbroll)
        self.effect =effect
        self.effectDescription = descEffet
        self.duree=duree
    def __str__(self):
        descriptionEffet = ""
        if self.effect!= None :
            descriptionEffet ="\nEffet de la potion : "+str(self.effectDescription) 
            return f"\n\nNom de la potion : **{self.nom}**{descriptionEffet}\n Durée de l'effet : {self.duree}"
        if self.heal :
            return f"\n\nNom de la potion : **{self.nom}**\n\t↳soin : {self.mini} à {self.maxi}\n\t↳type de heal : {self.type} {self.desc[0]}\n\t↳stat améliorante : {self.stat} {self.desc[1]}"
        return f"\n\nNom de la potion : **{self.nom}**\n\t↳dégats : {self.mini} à {self.maxi}\n\t↳type de dégat : {self.type} {self.desc[0]}\n\t↳stat améliorante : {self.stat} {self.desc[1]}"
    def __repr__(self):
        return str(self)
    def effet(self,buveur : Perso,turnNumber) :
        if self.effect == None :
            nombre = self.roll(buveur.getStatValue(buveur.getStatName(self.stat)))
            if self.heal :
                buveur.heal(nombre)
            else :
                buveur.subitdegat(nombre,self.type)
        else :
            self.effect(self,buveur,turnNumber)