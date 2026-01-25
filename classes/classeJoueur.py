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
                self.maxpv=(4+self.niv)*self.end+10+self.bonus
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
    
   
