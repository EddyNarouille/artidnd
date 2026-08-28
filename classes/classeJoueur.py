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
    def __init__(self,payload):
        point = payload["point"]
        xp = payload["xp"]
        potion = payload["potion"]
        monnaie = payload["monnaie"]
        joueurid = payload["joueurid"]
        super().__init__(payload)
        self.point=point
        self.xp = xp
        self.potion = potion
        self.joueurid = joueurid
        self.monnaie=monnaie
        print(self.nom,"initialisé")
    def argent(self,nb):
        if self.monnaie+nb<0:
            return "pas assez de monnaie"
        else :
            self.monnaie+=nb
            return self.nom +"a "+self.monnaie + " pièce(s)"
    def paye(self,nb,qql=None):
        if self.monnaie-nb<0:
            return "pas assez de monnaie"
        if qql==None:
            self.monnaie-=nb
            return f"{self.nom} paye {nb} à un PNJ. Il vous reste "+str(self.monnaie)+" pièce(s)"
        else :
            qql.argent(nb)
            self.monnaie-=nb
            return self.nom+" donne "+str(nb)+" pièce(s) à "+qql.nom
    def lv(self,nb):
        for i in range(nb):
            if (self.niv ==5) :
                break
            self.xp+=1
            if self.xp==30+5*self.niv*self.niv:
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
                self.maxpv=1 + 2*self.constitution + bonusClasse + (2+(bonusClasse//2))*self.niv
                if type(self.classe) == Lutteur :
                    self.classe.levelMartial()
    def delv(self,nb):
        for i in range(nb):
            if (self.niv ==1 and self.xp == 0) :
                break
            self.xp-=1
            if self.xp==-1:
                self.niv-=1
                self.point-=1
                self.xp=30+5*self.niv*self.niv-1
                if type(self.classe) == Hoplite :
                    bonusClasse = 6
                elif type(self.classe) in (Lutteur,Champion,Spartiate) :
                    bonusClasse = 4
                elif type(self.classe) in (SangMele, Spadassin) :
                    bonusClasse = 2
                elif type(self.classe) in (Rhapsode, Prophete) :
                    bonusClasse = 0
                self.maxpv=1 + 2*self.constitution + bonusClasse + (2+(bonusClasse//2))*self.niv
                if (self.pv>self.maxpv) :
                    self.pv=self.maxpv
                if type(self.classe) == Lutteur :
                    self.classe.levelMartial()
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
    
   
