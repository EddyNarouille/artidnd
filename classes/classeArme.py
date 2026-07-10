from random import randint 

class Arme:
    def __init__(self,nom,mini,maxi,type,nbroll=1) :
        self.nom=nom
        self.mini=mini
        self.maxi=maxi
        self.type=type
        self.nbroll = nbroll
    def roll(self,nb):
        a=randint(self.mini,self.maxi)
        for i in range(1,self.nbroll) :
            a+=randint(self.mini,self.maxi)
        return a+ int(nb/2)