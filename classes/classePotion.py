from classes.classeSort import Sort
from classes.classePerso import Perso
from random import randint
import json
class Potion :
    def __init__(self, nom, mini, maxi, heal=0, nbroll=1,descEffet="", duree= 0):
        self.nom= nom
        self.mini = mini
        self.maxi = maxi
        self.heal = bool(heal)
        self.nbroll=nbroll
        self.effectDescription = descEffet
        self.duree=duree
    def __str__(self):
        if self.heal :
            return f"Nom de la potion : **{self.nom}**\n\t↳soin : {self.mini*self.nbroll} à {self.maxi*self.nbroll}\n\n{self.effectDescription}"
        return f"Nom de la potion : **{self.nom}**\n\t↳dégats : {self.mini*self.nbroll} à {self.maxi*self.nbroll}\n\n{self.effectDescription}"
    def __repr__(self):
        return str(self)
    def roll(self):
        a=0
        for i in range(0,self.nbroll) :
            a+=randint(self.mini,self.maxi)
        return a
    def effet(self,buveur : Perso) :
        nombre = self.roll()
        if self.heal :
            buveur.heal(nombre)
        else :
            buveur.subitdegat(nombre,self.type)
    def toJSON(self) :
        return json.dumps({"nom" : self.nom})