from random import randint
from classes.classeArme import Arme 

class ArmeLegendaire(Arme):
    def __init__(self,nom,stat1,stat2,mini,maxi,req1,req2,type,nbroll=1):
        super().__init__(nom,mini,maxi,stat1,type,nbroll)
        self.bonus=stat2
        self.req1=req1
        self.req2=req2
        self.type=type
    def roll(self,nb1,nb2):
        a = 0
        if nb1>=self.req1 and nb2>=self.req2:
            for i in range(self.nbroll):
                a+= randint(self.mini,self.maxi)
            a+=+nb1/2 + randint(self.req2,nb2)
            return a 
        elif nb1>=self.req1:
            for i in range(self.nbroll):
                a+= randint(self.mini,self.maxi)
            a +=nb1/2
            return a
        else :
            print(f"{self.nom} est difficile à manier pour vous, vous êtes incapable de l'utiliser (fin de votre tour)")
            return 0
        
            