from random import randint
from classes.classeArme import Arme
class Sort(Arme):
    def __init__(self,nom,mini,maxi,type,stat="intel",heal=0,nbroll=1,cout=0,porte=0,rayon =0) :
        super().__init__(nom,mini,maxi,stat,type,nbroll)
        self.desc=""
        self.cout=cout
        self.heal=bool(heal)
        self.porte=porte
        self.rayon = rayon
        if self.type=="feu":
            self.desc+="🔥"
        elif self.type=="poison":
            self.desc+="💀"
        elif self.type=="foudre":
            self.desc+="⚡"
        elif self.type=="eau":
            self.desc+="💧"
        elif self.type=="glace":
            self.desc+="❄️"
        elif self.type=="terre":
            self.desc+="🪨"
        elif self.type=="impact":
            self.desc+="🔨"
        elif self.type=="perçant" or self.type=="percant":
            self.desc+="🪛"
        elif self.type=="tranchant":
            self.desc+="🗡️"
        if self.stat=="intel":
            self.desc+="🧠"
        if self.stat=="esprit":
            self.desc+="💡"
        if self.stat=="force":
            self.desc+="💪"
        if self.stat=="dex":
            self.desc+="🎯"
        self.desc+="  "
    def __str__(self):
        porte = str(self.porte) + "m"
        if self.porte == 0 :
            porte = "Au contact"
        zone = ""
        if self.rayon != 0 :
            zone = f"\nCe sort est un sort de zone\n\t↳rayon : {self.rayon}m"
        if self.heal :
            return f"\n\nNom du sort : **{self.nom}**\n\t↳soin : {self.mini} à {self.maxi}\n\t↳type de heal : {self.type} {self.desc[0]}\n\t↳stat améliorante : {self.stat} {self.desc[1]}\n\t\t↳portée : {porte}{zone}"
        return f"\n\nNom du sort : **{self.nom}**\n\t↳dégats : {self.mini} à {self.maxi}\n\t↳type de dégat : {self.type} {self.desc[0]}\n\t↳stat améliorante : {self.stat} {self.desc[1]}\n\t\t↳portée : {porte}{zone}"
    def __repr__(self):
        return str(self)