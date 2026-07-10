from random import randint 
from classes.classeArme import Arme
from classes.classeSort import Sort
from classes.classeArmeLegendaire import ArmeLegendaire
from classes.classeCombat.champion import *
from classes.classeCombat.lutteur import *
from classes.classeCombat.prophete import *
from classes.classeCombat.rhapsode import *
from classes.classeCombat.sangmelé import *
from classes.classeCombat.spadassin import *
from classes.classeCombat.spartiate import *
from classes.classeCombat.hoplite import *
from classes.classeArmure import *
import json

class Perso:
    def __init__(self,nom,force,habilité,constitution,charisme,foi,inventaire,dieux,classe,niveau=1):
        self.coordX=-1
        self.coordY=-1
        self.nom=nom
        self.force=force
        self.habilité=habilité
        self.foi = foi
        self.constitution=constitution
        self.classe = classe
        if type(classe) == Hoplite :
            bonusClasse = 6
        if type(classe) in (Lutteur,Champion,Spartiate) :
            bonusClasse = 4
        elif type(classe) in (SangMele, Spadassin) :
            bonusClasse = 2
        elif type(classe) in (Rhapsode, Prophete) :
            bonusClasse = 0
        self.maxpv=1 + 2*constitution + bonusClasse + 2*niveau
        self.pv = 1 + 2*constitution + bonusClasse + 2*niveau
        self.charisme=charisme
        self.niv,self.xp,self.monnaie=niveau,0,0
        self.point=0
        self.compteur=0
        self.poison=False
        self.emoji="O"
        self.inventaire = inventaire
        self.dieux = dieux
        self.armure = 10
        for equipement in inventaire :
            if type(equipement) == Armure :
                self.armure+=equipement.armure
    def modifStat(self,stat,nb) :
        setattr(self,self.getStatName(stat),getattr(self,self.getStatName(stat))+nb)
    def getStatName(self,stat) :
        if stat in "charisme":
            return "charisme"
        if stat in "force":
           return "force"
        if stat in "constitution":
            return "constitution"
        if stat in "foi":
            return "foi"
        if stat in "habilité":
            return "habilité"
    def getStatValue(self,stat):
        return getattr(self,self.getStatName(stat))
    def roll(self , stat="charisme"):
        a=randint(1,20)
        if a ==20 :
            return 20
        if a!=1:
            return min(19,a+int(self.getStatValue(stat)/3))
        else : 
            return 1
    def getstat(self):
        return f"{self.force}\n{self.habilité}\n{self.constitution}\n{self.charisme}\n{self.foi}"
    def getInfo(self):
        return f"{self.pv}\n{self.niv}\n{self.xp}\n{self.monnaie}\n{self.point}\n{self.coordX}\n{self.coordY}"
    def subitdegat(self,nb,type):
        if self.poison:
            nb+=2
            self.compteur+=1
            if self.compteur==2:
                self.compteur=0
                self.poison=False
        if type=="poison":
            self.poison=True
            self.compteur=0
        self.pv-=nb
        if self.pv <= 0 :
            print(self.nom,"est mort")
    def soin(self,nb):
        self.pv+=nb
        self.poison=False
        self.compteur=0
        if self.pv>self.maxpv:
            self.pv=self.maxpv
    def heal(self,qql,nb):
        qql.soin(nb)
    def attaque(self,qql,arme,coef=1):
        a=0
        if type(arme)==Arme or type(arme)==Sort:
            a = arme.roll(self.force)*coef
        if type(arme)==ArmeLegendaire:
            a = arme.roll(self.force,self.getStatValue(arme.bonus))*coef
        qql.subitdegat(int(a),arme.type)
        return int(a)
    def copie(self,nom="") :
        if nom =="":
            nom= self.nom
        return Perso(nom,self.force,self.habilité,self.constitution,self.charisme,self.foi)
    def toJsonMap(self) :
        return self.__dict__
    def __str__(self):
        a=f"# Stats de {self.nom} : \n **force** : {self.force } \n **habilité** : {self.habilité}"
        a+=f"\n **constitution** : {self.constitution} **charisme** : {self.charisme} \n **foi** : {self.foi}"
        a+=f"\n\n# info : \n **pv** : {self.pv} (**pv max** : {self.maxpv}) \n **niveau** : {self.niv}"
        a+=f"\n **exp** : {self.xp}, il reste {20+15*self.niv*self.niv} exp avant de level up \n "
        a+=f"**point de compétence à utiliser** : {self.point}\n **monnaie** : {self.monnaie} \n **classe** : {self.classe}"
        a+=f"\n**Relations divines :** \n{json.loads(self.dieux)[1:len(self.dieux)-1]}"
        return a
    def __repr__(self):
        return str(self)
    def lv(self,nb):
        return