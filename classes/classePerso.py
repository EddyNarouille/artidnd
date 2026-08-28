from random import randint 
from classes.classeArme import Arme
from classes.classeCombat.monstre import Monstre
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
from effetDieux import *
from functions import forger

class Perso:
    def __init__(self,payload):
        nom = payload["nom"]
        force = payload["force"]
        habilité = payload["habilité"]
        constitution = payload["constitution"]
        charisme = payload["charisme"]
        foi = payload["foi"]
        inventaire = payload["inventaire"]
        dieux = payload.get("dieux",{
    "Zeus" : 50,
    "Poséidon" : 50,
    "Artémis" : 50,
    "Arès" : 50,
    "Athéna" : 50,
    "Aphrodite" : 50,
    "Dionysos" : 50,
    "Déméter" : 50,
    "Hermès" : 50,
    "Apollon" : 50,
    "Héphaïstos" : 50
})
        classe = payload["classe"]
        niveau = payload["niv"]
        coordX = payload.get("coordX",-1)
        coordY = payload.get("coordY",-1)
        self.coordX=coordX
        self.coordY=coordY
        self.nom=nom
        self.force=force
        self.habilité=habilité
        self.foi = foi
        self.constitution=constitution
        self.niv,self.xp,self.monnaie=niveau,payload.get("xp",0),payload.get("monnaie",0)
        match classe : 
            case "Hoplite" :
                classe = Hoplite(self)
            case "Champion" :
                classe = Champion(self)
            case "Spartiate" :
                classe = Spartiate(self)
            case "Spadassin" :
                classe = Spadassin(self)
            case "Rhapsode" :
                classe = Rhapsode(self)
            case "Prophète" :
                classe = Prophete(self)
        if type(classe) == str :
            if "Sang" in classe :
                Olympe = ["Zeus","Arès","Poséidon","Artémis","Athéna","Aphrodite","Déméter","Dionysos","Hermès","Apollon","Héphaïstos"]
                dieuxL = classe.split(" / ")
                if dieuxL[1] in Olympe and dieuxL[2] in Olympe :
                    classe = SangMele(dieuxL[1],dieuxL[2],self)
                else :
                    classe = SangMele(user=self)
            elif "Lutteur" in classe :
                nb=-1
                lst= classe.split("|")
                if len(lst)>1 :
                    nb=int(lst[1])
                classe = Lutteur(self,nb)
            elif "Monstre" in classe :
                nb=1
                lst= classe.split("|")
                if len(lst)>1 :
                    nb=int(lst[1])
                classe = Monstre(self,nb)
        self.classe = classe
        bonusClasse=0
        if type(classe) == Hoplite :
            bonusClasse = 6
        elif type(classe) in (Lutteur,Champion,Spartiate) :
            bonusClasse = 4
        elif type(classe) in (SangMele, Spadassin) :
            bonusClasse = 2
        elif type(classe) in (Rhapsode, Prophete) :
            bonusClasse = 0
        self.maxpv=1 + 2*constitution + bonusClasse + (2+(bonusClasse//2))*niveau
        self.pv= payload.get("pv",self.maxpv)
        self.charisme=charisme
        self.classe.user = self
        if type(self.classe) == Monstre :
            self.classe.increaseHP(self.pv)
        self.point=payload.get("point",0)
        self.compteur=payload.get("compteur",0)
        self.poison=payload.get("poison",False)
        self.emoji=payload.get("emoji","O")
        self.inventaire = inventaire
        self.dieux = dieux
        self.faveurs = []
        self.coleres = []
        self.benedictions = []
        self.maledictions = []
        self.bonus = []
        self.malus = []
        self.usedDay = payload.get("usedDay",[])
        self.effect = payload.get("effect",{
            "bouclier" : [],
            "frayeur" : [],
            "dramatique" : [],
            "soin" : [],
            "courage" :  [],
            "divin" : []
        })
        self.usedCombat = payload.get("useCombat",[])
        for dieu in self.dieux.keys() :
            if self.dieux[dieu] > 75 :
                if type(self.classe) != SangMele or (type(self.classe) == SangMele and self.classe.dieuBonus!=dieu and self.classe.dieuMalus!=dieu):
                    self.bonus.append(f"Faveur de {dieu} : {Faveurs[dieu]}\n")
                    self.faveurs.append(dieu)
            if self.dieux[dieu] < 25:
                if type(self.classe) != SangMele or (type(self.classe) == SangMele and self.classe.dieuBonus!=dieu and self.classe.dieuMalus!=dieu):
                    self.malus.append(f"Colère de {dieu} : {Coleres[dieu]}\n")
                    self.coleres.append(dieu)
        if type(self.classe) == SangMele :
            if self.dieux[self.classe.dieuBonus]>40-(5*self.niv):
                self.bonus.append(f"Bénédiction de {self.classe.dieuBonus} : {Benedictions[self.classe.dieuBonus]}")
                self.benedictions.append(self.classe.dieuBonus)
            if self.dieux[self.classe.dieuMalus]<80-(5*self.niv):
                self.malus.append(f"Malédiction de {self.classe.dieuMalus} : {Maledictions[self.classe.dieuMalus]}")
                self.maledictions.append(self.classe.dieuMalus)
        self.armure = 10
        nb=0
        for equipement in inventaire :
            
            if type(equipement) == Armure :
                if "Héphaïstos" in self.maledictions :
                    break
                if "Héphaïstos" in self.coleres :
                    if nb==1 :
                        break
                    nb+=1
                self.armure+=equipement.armure
                if "Athéna" in self.faveurs and equipement.nom == "Bouclier" :
                    self.armure+=1
                
        if "Athéna" in self.faveurs :
            self.armure+=1
        if "Athéna" in self.coleres :
            self.armure-=2
        if "Aphrodite" in self.maledictions :
            self.maxpv=int(self.maxpv*0.75)
            if self.pv>self.maxpv:
                self.pv= self.maxpv
    def modifStat(self,stat,nb) :
        setattr(self,self.getStatName(stat),self.getStatValue(stat)+nb)
    def usePower(self,dieu) :
        if dieu in self.benedictions :
             
            if dieu in ("Artémis","Zeus","Dionysos","Héphaïstos") and dieu not in self.usedDay : #UsedDay
                self.usedDay.append(dieu)
                if dieu == "Héphaïstos" :
                    forger(self)
                if dieu == "Dionysos" :
                    bonus = ["faveur","soin","rhapsode","stat"][randint(0,3)]
                    match bonus :
                        case "faveur" :
                            self.updateFaveurs("all",10,True)
                        case "soin" :
                            self.soin(self.maxpv//5)
                        case "stat" : 
                            self.foi+=1
                            self.force +=1
                            self.constitution += 1
                            self.maxpv+=2
                            self.pv+=2
                            self.charisme +=1
                            self.habilité += 1
                        case "rhapsode" :
                            chant = ["courage","bouclier","soin","divin"][randint(0,3)]
                            if chant in ("courage","bouclier") :
                                self.effect[chant].append("Dionysos")
                            match chant :
                                case "soin" :
                                    self.soin(self.maxpv//5)
                                case "divin" :
                                    self.soin(self.maxpv//5)
                                    self.effect["courage"].append("Dionysos")
                                    self.effect["bouclier"].append("Dionysos")
                            bonus+=chant
                    self.usedDay.append(bonus)
            elif dieu in ("Athéna","Héphaïstos") and dieu not in self.usedCombat : #UsedCombat
                self.usedCombat.append(dieu)
            if (type(self.classe) == SangMele and "Zeus" in self.maledictions) :
                self.subitdegat(2,"Foudre")
                return f"{self.nom} appelle {dieu} pour l'aider. Mais la colère de Zeus s'abbat sur vous."
            return f"{self.nom} appelle {dieu} pour l'aider."
        elif dieu in self.faveurs :
            if dieu in ("Zeus") and dieu not in self.usedDay : #UsedDay
                self.usedDay.append(dieu)
            elif dieu in ("Héphaïstos") and dieu not in self.usedCombat and dieu not in self.usedDay : #UsedCombat
                self.usedCombat.append(dieu)
                self.usedDay.append(dieu)
            if (type(self.classe) == SangMele and "Zeus" in self.maledictions) :
                self.subitdegat(2,"Foudre")
                return f"{self.nom} appelle {dieu} pour l'aider. Mais la colère de Zeus s'abbat sur vous."
            return f"{self.nom} appelle {dieu} pour l'aider."
        else :
            return "Vous ne pouvez pas utiliser de pouvoir en lien avec ce dieu. Regardez vos bonus avec la commande pour."
    def getStatName(self,stat) :
        if stat in "habilité":
            return "habilité"
        if stat in "charisme":
            return "charisme"
        if stat in "force":
           return "force"
        if stat in "constitution":
            return "constitution"
        if stat in "foi":
            return "foi"
        return None
    def getStatValue(self,stat):
        return getattr(self,self.getStatName(stat))
    def newDay(self) :
        if "faveur" in self.usedDay :
            self.updateFaveurs("all",-10,True)
        if "stat" in self.usedDay :
            self.force -=1
            self.foi -=1
            self.habilité -= 1
            self.constitution -=1
            self.charisme -=1
            if self.pv >2 :
                self.pv-=2
            self.maxpv-=2
        self.usedDay = []
        self.usedCombat = []
        for chant in self.effect.keys() :
            self.effect[chant] = []
        self.soin(3)
        if type(self.classe) == Hoplite and self.niv >= 4 :
            self.soin(3)
        if type(self.classe) == Lutteur :
            self.classe.updateMartiaux(10)
        return 
    def roll(self , stat="charisme"):
        a=randint(1,20)
        limit = ""
        if "Dionysos"  in self.faveurs and stat=="charisme" :
            while a+int(self.getStatValue(stat)/2)<10 :
                a=randint(1,20) 
            limit="Ne peut pas être inférieur à 10 : Faveur de Dionysos"
        if "Dionysos" in self.maledictions :
            while a+int(self.getStatValue(stat)/2)>15 :
                a=randint(1,20)
            limit="Limitation à 15 : Malédiction de Dionysos"
        b = a
        if a ==20 :
            limit = "Limitation à 20 car succès critique"
            return 20,[b,int(self.getStatValue(stat)/2)],limit
        if a!=1:
            if min(19,a+int(self.getStatValue(stat)/2))>19 :
                limit = "Limitation à 19."
            if stat=="charisme" :
                if "Aphrodite" in self.faveurs :
                    a+=2
                    limit += "bonus de +2 faveur d'Aphrodite"
                    return min(19,a+int(self.getStatValue(stat)/2)),[b,int(self.getStatValue(stat)/2),2],limit
                elif "Aphrodite" in self.coleres :
                    a-=2
                    limit += "malus de -2 colère d'Aphrodite"
                    return min(19,a+int(self.getStatValue(stat)/2)),[b,int(self.getStatValue(stat)/2),-2],limit
            return min(19,a+int(self.getStatValue(stat)/2)),[b,int(self.getStatValue(stat)/2)],limit
        else : 
            limit = "Limitation à 1 car échec critique"
            return 1,[b,int(self.getStatValue(stat)/2)],limit
    def subitdegat(self,nb,typeDegat,who=None):
        if who!=None and "Héphaïstos" in self.faveurs and "Héphaïstos" in self.usedCombat : 
            who.subitdegat(3,"feu")
        if who!=None and "Athéna" in self.benedictions and "Athéna" not in self.usedCombat :
            self.usedCombat = "Athéna"
            return 0
        if who!=None and type(self.classe) == Spadassin and self.niv>=3 and "Dérobade" not in self.usedCombat :
            self.usedCombat("Dérobade")
            nb=nb//4
        if who!=None and type(self.classe) == Hoplite :
            for equipement in self.inventaire :
                if type(equipement) == Armure and equipement.nom == "Bouclier" :
                    nb=int(nb*0.8)
        for equipement in self.inventaire :
            if type(equipement) == Armure :
                if "Athéna" in self.faveurs and equipement.nom == "Bouclier" :
                    nb-=2
        if "Athéna" in self.faveurs :
            nb-=2
        if len(self.effect["bouclier"]) != 0 and "Dionysos" not in self.coleres:
            nb=int(nb*0.85)
        if len(self.effect["frayeur"]) != 0  and "Dionysos" not in self.coleres:
            nb=int(nb*1.1)
        if nb<0 :
            nb=1
        if typeDegat=="poison":
            self.poison=True
            self.compteur=0
        self.pv-=nb
        if self.pv <= 0 :
            self.pv=0
            if "Arès" in self.benedictions and "Arès" not in self.usedDay :
                self.usedDay.append("Arès")
                self.pv = self.maxpv
            elif type(self.classe) == Spartiate and self.niv>=5 and "Dernier courage" not in self.usedDay:
                self.usedDay.append("Dernier courage")
                self.pv = 1
            else : 
                print(self.nom,"est mort")
        return nb
    def monStuff(self) :
        a =""
        for item in self.inventaire :
            a += f"{item}\n"
        return a
    def getDieux(self) :
        if self.bonus+self.malus == [] :
            return "Les dieux ne prêtent pas encore attention à vous... Gagnez leurs faveurs ou leurs colères en fonction de vos actions."
        a =f"# Bonus et malus divins de {self.nom}\n"
        for faveur in self.bonus :
            a+= faveur+"\n"
        for colere in self.malus :
            a+= colere+"\n"
        return a
    def updateFaveurs(self,dieu,nb,fix = False) :
        if nb>0 and fix:
            nb+= randint(0,self.foi)
        if type(self.classe) == Prophete and self.niv >= 2 :
            if nb>0 :
                nb = int(nb*1.5)
            else :
                nb = int(nb/1.5)
        if dieu == "all" :
            self.faveurs = []
            self.coleres = []
            self.benedictions = []
            self.maledictions = []
            self.bonus = []
            self.malus = []
            for dieuK in self.dieux.keys() :
                self.dieux[dieuK]+=nb
                if self.dieux[dieuK] > 75 :
                    if type(self.classe) != SangMele or (type(self.classe) == SangMele and self.classe.dieuBonus!=dieuK and self.classe.dieuMalus!=dieuK):
                        self.bonus.append(f"Faveur de {dieuK} : {Faveurs[dieuK]}\n")
                        self.faveurs.append(dieuK)
                if self.dieux[dieuK] < 25 :
                    if type(self.classe) != SangMele or (type(self.classe) == SangMele and self.classe.dieuBonus!=dieuK and self.classe.dieuMalus!=dieuK):
                        self.malus.append(f"Colère de {dieuK} : {Coleres[dieuK]}\n")
                        self.coleres.append(dieuK)
            if type(self.classe) == SangMele :
                if self.dieux[self.classe.dieuBonus]>40-(5*self.niv) :
                    self.bonus.append(f"Bénédiction de {self.classe.dieuBonus} : {Benedictions[self.classe.dieuBonus]}")
                    self.benedictions.append(self.classe.dieuBonus)
                if self.dieux[self.classe.dieuMalus]<80-(5*self.niv) :
                    self.malus.append(f"Malédiction de {self.classe.dieuMalus} : {Maledictions[self.classe.dieuMalus]}")
                    self.maledictions.append(self.classe.dieuMalus)
            return self.dieux
        self.dieux[dieu]+=nb
        if self.dieux[dieu] > 75 and dieu not in self.faveurs:
            if type(self.classe) != SangMele or (type(self.classe) == SangMele and self.classe.dieuBonus!=dieu and self.classe.dieuMalus!=dieu):
                self.bonus.append(f"Faveur de {dieu} : {Faveurs[dieu]}\n")
                self.faveurs.append(dieu)
        if self.dieux[dieu] <= 75 and dieu in self.faveurs:
            if type(self.classe) != SangMele or (type(self.classe) == SangMele and self.classe.dieuBonus!=dieu and self.classe.dieuMalus!=dieu):
                self.bonus.remove(f"Faveur de {dieu} : {Faveurs[dieu]}\n")
                self.faveurs.remove(dieu)
        if self.dieux[dieu] < 25 and dieu not in self.coleres:
            if type(self.classe) != SangMele or (type(self.classe) == SangMele and self.classe.dieuBonus!=dieu and self.classe.dieuMalus!=dieu):
                self.malus.append(f"Colère de {dieu} : {Coleres[dieu]}\n")
                self.coleres.append(dieu)
        if self.dieux[dieu] >= 25 and dieu in self.coleres:
            if type(self.classe) != SangMele or (type(self.classe) == SangMele and self.classe.dieuBonus!=dieu and self.classe.dieuMalus!=dieu):
                self.malus.remove(f"Colère de {dieu} : {Coleres[dieu]}\n")
                self.coleres.remove(dieu)
        if type(self.classe) == SangMele :
            if self.dieux[self.classe.dieuBonus]>40-(5*self.niv) and self.classe.dieuBonus not in self.benedictions:
                self.bonus.append(f"Bénédiction de {self.classe.dieuBonus} : {Benedictions[self.classe.dieuBonus]}")
                self.benedictions.append(self.classe.dieuBonus)
            if self.dieux[self.classe.dieuMalus]<80-(5*self.niv) and self.classe.dieuMalus not in self.maledictions:
                self.malus.append(f"Malédiction de {self.classe.dieuMalus} : {Maledictions[self.classe.dieuMalus]}")
                self.maledictions.append(self.classe.dieuMalus)
            if self.dieux[self.classe.dieuBonus]<=40-(5*self.niv) and self.classe.dieuBonus in self.benedictions:
                self.bonus.remove(f"Bénédiction de {self.classe.dieuBonus} : {Benedictions[self.classe.dieuBonus]}")
                self.benedictions.remove(self.classe.dieuBonus)
            if self.dieux[self.classe.dieuMalus]<80-(5*self.niv) and self.classe.dieuMalus in self.maledictions:
                self.malus.remove(f"Malédiction de {self.classe.dieuMalus} : {Maledictions[self.classe.dieuMalus]}")
                self.maledictions.remove(self.classe.dieuMalus)
        
        return {dieu : self.dieux[dieu]}
    def soin(self,nb):
        diff = self.maxpv - self.pv
        self.pv+=nb
        self.poison=False
        self.compteur=0
        if self.pv>self.maxpv:
            self.pv=self.maxpv
        return min(nb,diff)
    def heal(self,qql,nb):
        return qql.soin(nb)
    def attaque(self,qql,arme,coef=1,critique = False):
        a=0
        oneShot = qql.pv == qql.maxpv
        if type(self.classe) == Spartiate and self.niv >= 3 :
            a+=(self.maxpv-self.pv)//5
        if type(self.classe) == Champion :
            if self.pv==self.maxpv :
                a+=4
            if oneShot :
                a+=2
        if "Poséidon" in self.faveurs :
            a+=2
            if arme.nom in ["lance","hallebarde","trident"] :
                a+=2
        if "Aphrodite" in self.faveurs :
            roll = randint(1,3)
            if roll != 1 :
                qql.armure -= 1
            if roll == 3 :
                qql.armure -= 1
        if "Artémis" in self.faveurs and arme.nom =="arc":
            a+=5
        if "Arès" in self.faveurs :
            a+=2
            self.soin(2)
        if "Zeus" in self.benedictions and critique :
            a+=2
        if type(arme)==Arme :
            a += int(arme.roll(self.force)*coef)
        if type(arme)==ArmeLegendaire:
            a += int(arme.roll(self.force,self.getStatValue(arme.bonus))*coef)
        if type(self.classe) == Lutteur and arme.nom == "poing" :
            a+=self.force//2
        if critique :
            a*=2
            if type(self.classe) == Spartiate and self.niv>=4 :
                a=int(a*1.3)
        oneShot = oneShot and qql.pv<=a
        if type(self.classe) == Champion and self.niv >= 2:
            self.soin(3)
            if oneShot :
                self.soin(3)
        return qql.subitdegat(int(a),arme.type,self)
    def copie(self,nom="") :
        if nom =="":
            nom= self.nom
        return Perso({"nom" : nom,
            "force" : self.force,
            "habilité" : self.habilité,
            "constitution" : self.constitution,
            "charisme" : self.charisme,
            "foi" : self.foi,
            "classe" : self.classe,
            "inventaire" : self.inventaire,
            "niveau" :  self.niv,
            })
    def toJSON(self) :
        jsonmap = dict(self.__dict__)
        jsonmap["classe"] = str(self.classe)
        del jsonmap["armure"]
        del jsonmap["faveurs"]
        del jsonmap["coleres"]
        del jsonmap["bonus"]
        del jsonmap["malus"]
        del jsonmap["benedictions"]
        del jsonmap["maledictions"]
        jsonmap["inventaire"] = self.inventaire.copy()
        for item in range(len(self.inventaire)) :
            if type(jsonmap["inventaire"][item]) != str :   
                jsonmap["inventaire"][item] = self.inventaire[item].toJSON()
        with open("PlayerData/"+self.nom+".json","w") as outfile :
            json.dump(jsonmap,outfile,indent=2)
        return json.dumps(jsonmap,indent=2)
    
    def __str__(self):
        a=f"# Stats de {self.nom} : \n **force** : {self.force } \n **habilité** : {self.habilité}"
        a+=f"\n **constitution** : {self.constitution}\n **charisme** : {self.charisme} \n **foi** : {self.foi}"
        a+=f"\n\n# info : \n **pv** : {self.pv} (**pv max** : {self.maxpv}) \n **niveau** : {self.niv}"
        a+=f"\n **exp** : {self.xp}, il reste {30+5*self.niv*self.niv-self.niv} exp avant de level up \n "
        a+=f"**point de compétence à utiliser** : {self.point}\n **monnaie** : {self.monnaie}"

        if type(self.classe) == Lutteur :
            a+=f"\n **classe** : Lutteur" #pour pas a voir Lutteur | 0, je le laisse pour le sang mele car ca sert pour la sauvegarde et pour la classe du perso, mais la je met une ligne en plus justement
        else :
            a+=f"\n **classe** : {self.classe}"
        a+=f"**\n classe d'armure** : {self.armure}\n"
        if type(self.classe) == Lutteur and self.niv > 1 :
            a+= f"\n**points martiaux restants** : {self.classe.martiaux} sur {self.classe.maxMartiaux}"
        if self.dieux != {} : 
            a+=f"\n### Relations divines :"
            for dieu in self.dieux.keys() :
                a+=f"\n\t**{dieu}** : {self.dieux[dieu]}"
        return a
    def __repr__(self):
        return str(self)
    def lv(self,nb):
        return