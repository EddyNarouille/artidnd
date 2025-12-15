from random import randint 
from classes.classeArme import Arme
from classes.classeSort import Sort
from classes.classeArmeLegendaire import ArmeLegendaire
class Perso:
    def __init__(self,nom,force,dex,intel,end,perception,eloquence,esprit,magie,race,classe):
        self.nom=nom
        self.force=force
        self.dex=dex
        self.intel = intel
        self.end=end
        self.pv = 5 + 2*end
        self.maxpv=5 + 2*end
        self.esprit=esprit
        self.magie=magie
        self.eloquence=eloquence
        self.perception=perception
        self.niv,self.xp,self.monnaie=0,0,0
        self.point=0
        self.bonus=0
        self.classe=classe
        self.race=race
        self.compteur=0
        self.mana=0
        self.maxmana=0
        self.poison=False
        compense1 = self.race.faiblesse==self.classe.resistance
        compense2 = self.race.resistance==self.classe.faiblesse
        self.faiblesse =  [self.race.faiblesse,self.classe.faiblesse]
        self.resistance = [self.race.resistance,self.classe.resistance]
        if compense1 and not compense2:
            self.faiblesse=[self.classe.faiblesse]
            self.resistance=[self.race.resistance]
        elif compense2 and not compense1:
            self.faiblesse = [self.race.faiblesse]
            self.resistance=[self.classe.resistance]
        elif  compense1 and compense2 :
            self.faiblesse=["Aucune"]
            self.resistance=["Aucune"]
    def modifStat(self,stat,nb) :
        if stat in ("eloquence"):
            self.eloquence+=nb
        if stat in "force":
            self.force+=nb
        if stat in "intelligence":
            self.intel+=nb
        if stat in "perception":
            self.perception+=nb
        if stat in "endurance":
            self.end+=nb
        if stat in "esprit":
            self.esprit+=nb
        if stat in "dextérité":
            self.dex+=nb
        if stat in "magie" :
            self.magie+=nb
    def getStatName(self,stat) :
        if stat in ("eloquence"):
            return "eloquence"
        if stat in "force":
           return "force"
        if stat in "intelligence":
           return "intelligence"
        if stat in "perception":
            return "perception"
        if stat in "endurance":
            return "endurance"
        if stat in "esprit":
            return "esprit"
        if stat in "dextérité":
            return "dextérité"
        if stat in "magie" :
            return "magie"
    def getStatValue(self,stat):
        if stat in ("eloquence"):
            return self.eloquence
        if stat in "force":
           return self.force
        if stat in "intelligence":
           return self.intel
        if stat in "perception":
            return self.perception
        if stat in "endurance":
            return self.end
        if stat in "esprit":
            return self.esprit
        if stat in "dextérité":
            return self.dex
        if stat in "magie" :
            return self.magie
    def roll(self , stat="eloquence"):
        a=randint(1,20)
        if a ==20 :
            return 20
        a=self.useClassePower("roll",[stat,a]) if (self.useClassePower("roll",[stat,a])!=None) else a
        a=self.useRacePower("roll",[stat,a]) if (self.useRacePower("roll",[stat,a])!=None) else a
        if a!=1:
            return min(19,a+int(self.getStatValue(stat)/3))
        else : 
            return 1
    def getstat(self):
        return f"{self.force}\n{self.dex}\n{self.intel}\n{self.end}\n{self.perception}\n{self.eloquence}\n{self.esprit}\n{self.magie}"
    def getInfo(self):
        return f"{self.pv}\n{self.niv}\n{self.xp}\n{self.monnaie}\n{self.point}\n{self.mana}\n{self.bonus}"
    def subitdegat(self,nb,type):
        nb = self.useClassePower("subitdegat",[nb,type]) if self.useClassePower("subitdegat",[nb,type])!= None else nb
        nb = self.useRacePower("subitdegat",[nb,type]) if self.useRacePower("subitdegat",[nb,type])!= None else nb
        for faiblesse in self.faiblesse:
            if type in faiblesse:
                nb=int(nb*1.5)      
        for resistance in self.resistance:
            if type in resistance:
                nb=int(nb/1.5) 
            

        bon = self.faiblesse.count("poison")
        if self.poison:
            nb+=2
            self.compteur+=1
            if self.compteur==2+bon:
                self.compteur=0
                self.poison=False
        if type=="poison" and "poison" not in self.resistance:
            self.poison=True
            self.compteur=0
        self.pv-=nb
        if self.pv <= 0 :
            print(self.nom,"est mort")
    def soin(self,nb):
        if nb>0:
            nb+=randint(0,self.esprit)
        self.useClassePower("soin",nb)
        self.useRacePower("soin",nb)
        self.pv+=nb
        self.poison=False
        self.compteur=0
        if self.pv>self.maxpv:
            self.pv=self.maxpv
    def heal(self,qql,nb):
        nb = self.useClassePower("heal",nb) if self.useClassePower("heal",nb)!=None else nb
        nb = self.useRacePower("heal",nb) if self.useRacePower("heal",nb)!=None else nb
        qql.soin(nb)
    def attaque(self,qql,arme,coef=1):
        coef = self.useClassePower("attaque",[qql,arme,coef,self]) if self.useClassePower("attaque",[qql,arme,coef,self])!=None else coef
        coef = self.useRacePower("attaque",[qql,arme,coef,self]) if self.useRacePower("attaque",[qql,arme,coef,self])!=None else coef
        a=0
        if type(arme)==Arme or type(arme)==Sort:
            a = arme.roll(self.getStatValue(arme.stat))*coef
        if type(arme)==ArmeLegendaire:
            a = arme.roll(self.getStatValue(arme.stat),self.getStatValue(arme.bonus))*coef
        qql.subitdegat(int(a),arme.type)
        return int(a)
    def copie(self,nom="") :
        if nom =="":
            nom= self.nom
        return Perso(nom,self.force,self.dex,self.intel,self.end,self.perception,self.eloquence,self.esprit,self.magie,self.race,self.classe)
    def faiblesses(self):
        a = self.faiblesse[0]
        for i in range(1,len(self.faiblesse)):
            a+=", "+self.faiblesse[i]
        return a
    def resistances(self):
        a = self.resistance[0]
        for i in range(1,len(self.resistance)):
            a+=", "+self.resistance[i]
        return a
    def __str__(self):
        b = self.faiblesse.count("poison")
        a=f"# Stats de {self.nom} : \n **force** : {self.force } \n **dex** : {self.dex} \n **intelligence** : {self.intel}\n **endurance** : {self.end} \n **perception** : {self.perception} \n **eloquence** : {self.eloquence} \n **esprit** : {self.esprit} \n **magie** : {self.magie} \n\n# info : \n **pv** : {self.pv} (**pv max** : {self.maxpv}) \n **mana** : {self.mana} (**mana max** : {self.maxmana})\n **niveau** : {self.niv}\n **exp** : {self.xp}, il reste {15+10*self.niv-self.xp} exp avant de level up \n **point de compétence à utiliser** : {self.point}\n **monnaie** : {self.monnaie}\n **race** : {self.race.nom}\n **classe** : {self.classe.nom}\n **faiblesses** : {self.faiblesses()}\n **résistances** : {self.resistances()}\n **Capacité de classe** : {self.classe.capacite}\n **Capacité de race** : {self.race.capacite}"
        if self.poison :
            a+=f"\n\n Vous êtes empoisonné, il reste {str(3+b-self.compteur)} coup(s) à prendre pour être automatiquement soigné"
        return a
    def __repr__(self):
        return str(self)
    def useClassePower(self,methode,var):
        return self.classe.power(methode,var)
    def useRacePower(self,methode,var):
        return self.race.power(methode,var)
    def lv(self,nb):
        return