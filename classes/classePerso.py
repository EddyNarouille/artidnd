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

Faveurs = {
    "Zeus" : "Relancer un échec critique une fois par jour dans n'importe quelle catégorie",
    "Ares" : "Augmentation des dégâts infligés, chaque attaque vous soigne de quelques points de vies",
    "Poséidon" : "Augmente les dégâts et la portée des attaques au corps à corps, l'effet est doublé pour les armes d'hast",
    "Artémis" : "Bonus dégât a l'arc et à la discrétion",
    "Athéna" : "Les dégâts que vous prenez sont réduits et réduits les chances de se faire toucher par une attaque. Ce bonus est doublé en équippant un bouclier",
    "Aphrodite" : "Bonus à l'éloquence, les personnes que vous attaquez peuvent être affaiblis.",
    "Demeter" : "Les effets bénéfique des plantes curatives sont augmenté de 100%",
    "Dionysos" : "Vos jets d'interactions sociales ne peuvent pas être en dessous de 10.",
    "Hermès" : "Vous gagnez une action supplémentaire pendant le premier tour de votre combat. Le prix des objets est réduit de 10%",
    "Apollo" : "Vous êtes capable de créer une forme de lumière, qui ne peut être touché, mais qui peut prendre la forme de votre choix (environ taille humaine). Cette forme de lumière peut prendre diverses couleurs pour ressembler le plus à l'objet de loin, mais de proche, celle-ci est floue et légèrement transparente (type hologramme). Cette forme peut se déplacer et faire des gestes, mais elle ne réagit a rien sauf si vous la faites réagir vous mêmes. Elle ne peut pas parler.",
    "Héphaïstos" : "Vous mettez en feu votre propre corps pendant un combat entier. Ce feu ne vous brûle pas, mais brûle toute personne qui vous attaque. Utilisable une fois par jour"
}
Benedictions ={
    "Zeus" : "Vos attaques critiques font tomber un coup de tonnerre sur la personne que vous avez attaqué, lui infligeant quelques dégâts supplémentaires et l'étourdit. Vous pouvez invoquer la foudre une fois par jour pour provoquer cet effet sans dégâts supplémentaires.",
    "Ares" : "Le premier coup fatal subit d'une journée redonne tous vos points de vie",
    "Poséidon" : "Chacunes de vos attaques (touche ou non) crée une vague qui dans la direction de votre attaque, en ligne droite, sur 3 cases. \n Une personne touché par vos vagues perd une partie de sa vue pendant 1 tour (-2 roll des attaques) et devient vulnérable à des attaques critiques pendant 1 tour (19 devient un critique).",
    "Artémis" : "Un tir raté peut se transformer en critique (une fois par jour)",
    "Athéna" : "Chaque premier coup d'un combat qui aurait dû touché rate",
    "Aphrodite" : "Capacité de charmer n'importe quel PNJ pour obtenir quelque chose de lui, ou l'empêcher de vous attaquer (jusqu'à ce que vous l'attaquiez vous même).  Les personnes que vous attaquez peuvent lacher leur arme.",
    "Demeter" : "Des plantes rares et recherchées apparaissent plus souvent autour de vous. Votre main est capable de faire pousser des plantes de petites tailles quand vous le souhaitez sur une surface propice.",
    "Dionysos" : "Vous êtes immunisé aux effets négatifs de l'alcool. La première coupe de vin bu de la journée, vous gagnez un bonus aléatoire qui dure une journée parmis :\n+ 1 a toutes les caractéristiques.\n+ 10 faveurs à tous les dieux.\n+ 20% de point de vie.\nEffet d'un chant aléatoire positif du rhapsode.",
    "Hermès" : "Le prix des objets est réduit de 25% et chaque fois que vous mettez hors combat un adversaire, vous regagnez une action. ",
    "Apollo" : "Peut générer une boule de lumière qui éblouis tout ceux autour de lui. Vous êtes également capable de photosynthèse et régénérer des points de vie au soleil hors combat à un rythme très lent.",
    #"Héphaïstos" : "Peut créer une colonne de feu devant lui qui brûle les projectiles et quiconque s'en approche. Vous pouvez également forger une lame de feu."
}
Coleres = {
    "Zeus" : "La première attaque fatale que vous auriez dû faire dans un combat fait tomber un éclair sur la victime. Celle-ci est prise d'un sursaut et revient à la vie avec 1 point de vie.",
    "Ares" : "Chaque coup raté peut vous faire tomber vos armes",
    "Poséidon" : "Vous avez le mal de mer chaque fois que vous êtes sur un bateau. Ce bateau se rendra à destination en 5 fois plus de temps et à plus de chance d'échouer.",
    "Artémis" : "Un échec critique à l'arc la flèche revient vers vous, malus de dégâts aux bêtes",
    "Athéna" : "Réduis votre défense et les chances d'esquiver.",
    "Aphrodite" : "Malus à l'éloquence, malus contre les personnes du dernier sexe avec lequel vous avez eu une relation. Si vous n'avez eu aucune relation, il s'agit du sexe opposé.",
    "Demeter" : "Les effets bénéfique des plantes curatives sont réduit de 50%",
    "Dionysos" : "Vous ne pouvez recevoir aucun bonus de rhapsode. S'il n'y a aucun rhapsode dans votre groupe, chaque musique que vous entendez vous est tellement insupportable que vous ne pouvez y rester a proximité, si c'est le cas, vous serez a genoux à vous boucher les oreilles.",
    "Hermès" : "Le prix des objets augmente de 15%. Votre vitesse de déplacement est réduite de 2 cases.",
    "Apollo" : "Les soins qui vous sont procurés ne marchent pas le jour, vous ne pouvez être soigné à la lumière du soleil (à l'ombre ne suffit pas)",
    "Héphaïstos" : "Le métal devient plus lourd pour vous, il est tellement lourd que porter plusieurs pièces d'équipement est impossible (1 arme + 1 pièces d'armure)"
}
Maledictions = {
    "Zeus" : "Chaque fois que vous tuez un ennemi ou utilisez un pouvoir d'un autre dieu, un éclair tombe sur vous infligeant quelques dégâts à vous et aux personnes proches",
    "Ares" : "A une chance de rater une attaque qui aurait dû être un coup fatal. Si c'est le cas, l'ennemi peut contre attaquer ",
    "Poséidon" : "chaque bateau sur le quel vous naviguerez coulera. L'eau vous brûle et vous êtes incapable de nager.",
    "Artémis" : "Les flèches qui vous visent touchent toujours leur cible.",
    "Athéna" : "Vous ne pouvez pas toucher quelqu'un qui porte un bouclier",
    "Aphrodite" : "Personne ne peut vous aimer comme vous pouvez le faire, et vous déborder d'un amour à rendre, ce qui crée un manque affectif. Vos points de vie maximum sont réduits de 25%",
    "Demeter" : "Toutes plantes que tiens le joueur meurent sur le coup. Impossibilité de se soigner avec des herbes curatives.",
    "Dionysos" : "Vous avez les symptômes de l'ivresse sans boire, couplé à une gueule de bois. Chaque lancé de dés ne peut dépasser 14",
    "Hermès" : "Le prix des objets augmente de 100%.\nSi un ennemi rate une attaque sur vous, il a une deuxième chance pour vous attaquer gratuitement.",
    "Apollo" : "Les moyennes et fortes lumières sont insupportables pour ses yeux le forçant a être \"aveugle\" la journée",
    "Héphaïstos" : "Toute surface de métal est brûlante au toucher."
}

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
    "Ares" : 50,
    "Athéna" : 50,
    "Aphrodite" : 50,
    "Dionysos" : 50,
    "Demeter" : 50,
    "Hermès" : 50,
    "Apollo" : 50,
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
        match classe : 
            case "Hoplite" :
                classe = Hoplite()
            case "Lutteur" :
                classe = Lutteur()
            case "Champion" :
                classe = Champion()
            case "Spartiate" :
                classe = Spartiate()
            case "Spadassin" :
                classe = Spadassin()
            case "Rhapsode" :
                classe = Rhapsode()
            case "Prophète" :
                classe = Prophete()
        if "Sang-mélé" in classe :
            Olympe = ["Zeus","Ares","Poséidon","Artémis","Athéna","Aphrodite","Demeter","Dionysos","Hermès","Apollo","Héphaïstos"]
            dieux = classe.split(" / ")
            if dieux[1] in Olympe and dieux[2] in Olympe :
                classe = SangMele(dieux[1],dieux[2])
            else :
                classe = SangMele()
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
        self.niv,self.xp,self.monnaie=niveau,payload.get("xp",0),payload.get("monnaie",0)
        self.classe.user = self
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
        self.usedDay = []
        self.usedCombat = []
        for dieu in self.dieux.keys() :
            if self.dieux[dieu] < 25 :
                if not (type(self.classe) == SangMele and self.classe.dieuBonus!=dieu and self.classe.dieuMalus!=dieu):
                    self.bonus.append(f"Faveur de {dieu} : {Coleres[dieu]}\n")
                    self.faveurs.append(dieu)
            if self.dieux[dieu] > 75:
                if not (type(self.classe) == SangMele and self.classe.dieuBonus!=dieu and self.classe.dieuMalus!=dieu):
                    self.malus.append(f"Colère de {dieu} : {Faveurs[dieu]}\n")
                    self.coleres.append(dieu)
        if type(self.classe) == SangMele :
            if self.dieux[self.classe.dieuBonus]>30-(5*self.niv):
                self.bonus.append(f"Bénédiction de {self.classe.dieuBonus} : {Benedictions[self.classe.dieuBonus]}")
                self.benedictions.append(dieu)
            if self.dieux[self.classe.dieuMalus]<80-(5*self.niv):
                self.malus.append(f"Malédiction de {self.classe.dieuMalus} : {Maledictions[self.classe.dieuMalus]}")
                self.maledictions.append(dieu)
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
        setattr(self,self.getStatName(stat),getattr(self,self.getStatName(stat))+nb)
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
    def getStatValue(self,stat):
        return getattr(self,self.getStatName(stat))
    def newDay(self) :
        self.usedDay = []
        self.usedCombat = []
        return 
    def roll(self , stat="charisme"):
        a=randint(1,20)
        if "Dionysos"  in self.faveurs and stat=="charisme" :
            while a+int(self.getStatValue(stat)/2)<10 :
                a=randint(1,20)  
        if "Dionysos" in self.maledictions :
            while a+int(self.getStatValue(stat)/2)>14 :
                a=randint(1,20)
        if a ==20 :
            return 20
        if a!=1:
            if stat=="charisme" :
                if "Aphrodite" in self.faveurs :
                    a+=2
                if "Aphrodite" in self.coleres :
                    a-=2
            return min(19,a+int(self.getStatValue(stat)/2))
        else : 
            return 1
    def subitdegat(self,nb,typeDegat,who=None):
        if who!=None and "Héphaïstos" in self.faveurs and "Héphaïstos" in self.usedCombat : 
            who.subitdegat(3,"feu")
        if who!=None and "Athéna" in self.benedictions and "Athéna" not in self.usedCombat :
            self.usedCombat = "Athéna"
            return 0
        for equipement in self.inventaire :
            if type(equipement) == Armure :
                if "Athéna" in self.faveurs and equipement.nom == "Bouclier" :
                    nb-=2
        if "Athéna" in self.faveurs :
            nb-=2
        if nb<0 :
            nb=1
        if typeDegat=="poison":
            self.poison=True
            self.compteur=0
        self.pv-=nb
        if self.pv <= 0 :
            self.pv=0
            if "Ares" in self.benedictions and "Ares" not in self.usedDay :
                self.usedDay.append("Ares")
                self.pv = self.maxpv
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
    def updateFaveurs(self,dieu,nb) :
        if dieu == "all" :
            for dieuK in self.dieux.keys() :
                self.dieux[dieuK]+=nb
            return self.dieux
        self.dieux[dieu]+=nb
        return {dieu : self.dieux[dieu]}
    def soin(self,nb):
        self.pv+=nb
        self.poison=False
        self.compteur=0
        if self.pv>self.maxpv:
            self.pv=self.maxpv
    def heal(self,qql,nb):
        qql.soin(nb)
    def attaque(self,qql,arme,coef=1,critique = False):
        a=0
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
        if "Ares" in self.faveurs :
            a+=2
            self.soin(2)
        if "Zeus" in self.benedictions and critique :
            a+=2
        if type(arme)==Arme :
            a = int(arme.roll(self.force)*coef)
        if type(arme)==ArmeLegendaire:
            a = int(arme.roll(self.force,self.getStatValue(arme.bonus))*coef)
        if critique :
            a*=2
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
        for item in range(len(self.inventaire)) :
            if type(jsonmap["inventaire"][item]) != str :   
                jsonmap["inventaire"][item] = self.inventaire[item].toJSON()
        with open("PlayerData/"+self.nom+".json","w") as outfile :
            json.dump(jsonmap,outfile,indent=2)
        return json.dumps(jsonmap,indent=2)
    
    def __str__(self):
        a=f"# Stats de {self.nom} : \n **force** : {self.force } \n **habilité** : {self.habilité}"
        a+=f"\n **constitution** : {self.constitution}\n **charisme** : {self.charisme} \n **foi** : {self.foi}"
        a+=f"\n\n# info : \n **pv** : {self.pv} (**pv max*self.niv*self.niv** : {self.maxpv}) \n **niveau** : {self.niv}"
        a+=f"\n **exp** : {self.xp}, il reste {30+5*self.niv*self.niv} exp avant de level up \n "
        a+=f"**point de compétence à utiliser** : {self.point}\n **monnaie** : {self.monnaie} \n **classe** : {self.classe}"
        if self.dieux != {} : 
            a+=f"\n### Relations divines :"
            for dieu in self.dieux.keys() :
                a+=f"\n\t**{dieu}** : {self.dieux[dieu]}"
        return a
    def __repr__(self):
        return str(self)
    def lv(self,nb):
        return