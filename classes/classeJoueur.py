from classes.classePerso import Perso
class Joueur(Perso):
    def __init__(self,nom,force,dex,intel,end,perception,eloquence,esprit,magie,monnaie,race,classe):
        super().__init__(nom,force,dex,intel,end,perception,eloquence,esprit,magie,race,classe)
        
        self.pv = 10 + 4*end
        self.maxpv=10 + 4*end
        self.monnaie=monnaie
        self.xp=0
        self.niv=1
        self.point=0
        self.sorts=[]
        self.sortTout=[]
        self.mana = int(self.magie + self.intel/2) * self.race.magie * self.classe.magie
        self.maxmana = int(self.magie + self.intel/2) * self.race.magie * self.classe.magie
        self.potion = {}
        print(self.nom,"initialisé")
    def argent(self,nb):
        if self.monnaie+nb<0:
            return "pas assez de monnaie"
        else :
            self.monnaie+=nb
            return self.nom +"a "+self.monnaie
    def apprend(self,sort):
        self.sorts.append(sort.nom)
        self.sortTout.append(sort)
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
            if self.xp==15+10*self.niv:
                self.niv+=1
                self.point+=1
                self.xp=0
    def delv(self,nb):
        for i in range(nb):
            self.xp-=1
            if self.xp==-1:
                self.niv-=1
                self.point-=1
                self.xp=15+10*self.niv-1
    def AjouteMana(self,nb):
        self.mana+=nb
        if self.mana>self.maxmana :
            self.mana=self.maxmana
        return
    def EnleveMana(self,nb):
        self.mana-=nb
        return
    def ajouterPotion(self,potion,nb):
        if potion not in self.potion.keys() :
            self.potion[potion] =nb
        else :
            self.potion[potion] +=nb
    def retirerPotion(self,potion) :
        self.potion[potion]-=1
    def augmentStat(self,stat):
        if self.point>0:
            if stat== "eloquence" :
                if self.eloquence>9:
                    return "Le niveau maximal dans cette stat a déja été atteint"  
                else :
                    self.eloquence+=1
                    a=self.eloquence
                    self.point+=-1
            if stat== "force":
                if self.force>9:
                    return "Le niveau maximal dans cette stat a déja été atteint"  
                else :
                    self.force+=1
                    a=self.force
                    self.point+=-1
            if stat== "intelligence":
                if self.intel>9:
                    return "Le niveau maximal dans cette stat a déja été atteint"   
                else :
                    self.intel+=1
                    a=self.intel
                    self.point+=-1
            if stat== "perception" or stat== "per":
                if self.perception>9:
                    return "Le niveau maximal dans cette stat a déja été atteint"   
                else :
                    self.perception+=1
                    a= self.perception
                    self.point+=-1
            if stat== "end" or stat== "endurance" :
                if self.end>9:
                    return "Le niveau maximal dans cette stat a déja été atteint"   
                else :
                    self.end+=1
                    self.maxpv+=4
                    a =self.end
                    self.point+=-1
            if stat== "esprit" or  stat== "esp":
                if self.eloquence>9:
                    return "Le niveau maximal dans cette stat a déja été atteint"   
                else :
                    self.esprit+=1
                    a =self.esprit
                    self.point+=-1
            if stat== "dex" or stat=="dextérité":
                if self.dex>9:
                    return "Le niveau maximal dans cette stat a déja été atteint"  
                else :
                    self.dex+=1
                    a =self.dex
                    self.point+=-1
            if stat=="magie":
                if self.magie>9:
                    return "Le niveau maximal dans cette stat a déja été atteint"   
                else :
                    self.magie+=1
                    a =self.magie
                    self.point+=-1
            return "Vous avez mis un point en "+stat+" (vaut désormais : "+str(a)+ "), il vous reste "+str(self.point)+" point(s) de compétence a utiliser"
        return "Vous n'avez plus de point de compétence"
    
   
