from random import randint 
import json

class Arme:
    def __init__(self,nom,mini,maxi,type,nbroll=1,uneMain = False) :
        self.nom=nom
        self.mini=mini
        self.uneMain = uneMain
        self.maxi=maxi
        self.type=type
        self.nbroll = nbroll
    def roll(self,nb):
        a=randint(self.mini,self.maxi)
        for i in range(1,self.nbroll) :
            a+=randint(self.mini,self.maxi)
        return a + int(nb/2)
    def __str__(self):
        return f"# {self.nom} \n **dégâts** : {self.mini*self.nbroll} à {self.maxi*self.nbroll}\n (détail dégâts : nombre de jet : {self.nbroll}, résultat jet : {self.mini} à {self.maxi})\n\n*bonus de dégât = force/2*"
    def toJSON(self) :
        return self.nom