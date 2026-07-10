from classes.classePerso import Perso
from classes.classeCombat.champion import *
from classes.classeCombat.lutteur import *
from classes.classeCombat.prophete import *
from classes.classeCombat.rhapsode import *
from classes.classeCombat.sangmelé import *
from classes.classeCombat.spadassin import *
from classes.classeCombat.spartiate import *
from classes.classeCombat.hoplite import *


class Joueur(Perso):
    def __init__(self,nom,force,habilité,constitution,charisme,foi,inventaire,dieux,classe):
        super().__init__(nom,nom,force,habilité,constitution,charisme,foi,inventaire,dieux,classe)
        self.niv=1
        self.point=0
        self.sorts=[]
        self.sortTout=[]
        self.potion = {}
        print(self.nom,"initialisé")
    def argent(self,nb):
        if self.monnaie+nb<0:
            return "pas assez de monnaie"
        else :
            self.monnaie+=nb
            return self.nom +"a "+self.monnaie
    def paye(self,nb,qql=""):
        if qql=="":
            if self.monnaie-nb<0:
                return "pas assez de monnaie"
            else :
                self.monnaie-=nb
                return "il vous reste "+str(self.monnaie)+" pièce(s)"
        elif self.monnaie-nb<0:
            return "pas assez de monnaie"
        else :
            qql.argent(nb)
            self.monnaie-=nb
            return self.nom+" donne "+str(nb)+" pièce(s) à "+qql.nom
    def lv(self,nb):
        for i in range(nb):
            self.xp+=1
            if self.xp==20+15*self.niv*self.niv:
                self.niv+=1
                self.point+=1
                self.xp=0
                bonusClasse = 0
                if type(self.classe) == Hoplite :
                    bonusClasse = 6
                if type(self.classe) in (Lutteur,Champion,Spartiate) :
                    bonusClasse = 4
                elif type(self.classe) in (SangMele, Spadassin) :
                    bonusClasse = 2
                elif type(self.classe) in (Rhapsode, Prophete) :
                    bonusClasse = 0
                self.maxpv=1 + 2*self.constitution + bonusClasse + 2*self.niv
    def delv(self,nb):
        for i in range(nb):
            self.xp-=1
            if self.xp==-1:
                self.niv-=1
                self.point-=1
                self.xp=20+15*self.niv*self.niv-1
                if type(self.classe) == Hoplite :
                    bonusClasse = 6
                if type(self.classe) in (Lutteur,Champion,Spartiate) :
                    bonusClasse = 4
                elif type(self.classe) in (SangMele, Spadassin) :
                    bonusClasse = 2
                elif type(self.classe) in (Rhapsode, Prophete) :
                    bonusClasse = 0
                self.maxpv=1 + 2*self.constitution + bonusClasse + 2*self.niv
                if (self.pv>self.maxpv) :
                    self.pv=self.maxpv
    def ajouterPotion(self,potion,nb):
        if potion not in self.potion.keys() :
            self.potion[potion] =nb
        else :
            self.potion[potion] +=nb
    def retirerPotion(self,potion) :
        self.potion[potion]-=1
        if self.potion[potion] ==0 :
            del self.potion[potion]
    def augmentStat(self,stat):
        if self.point>0:
            if self.getStatValue(stat) >9 :
                return "Le niveau maximal dans cette stat a déja été atteint"
            self.modifStat(stat,1)
            a= self.getStatValue(stat)
            self.point+=-1
            return "Vous avez mis un point en "+stat+" (vaut désormais : "+str(a)+ "), il vous reste "+str(self.point)+" point(s) de compétence a utiliser"
        return "Vous n'avez plus de point de compétence"
    
   
