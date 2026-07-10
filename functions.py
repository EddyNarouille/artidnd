import codecs
from random import randint, shuffle
import unicodedata 
import json
from classes.classeArme import Arme
from classes.classeArmeLegendaire import ArmeLegendaire
from classes.classeBoss import Boss
from classes.classeCreature import Creature
from classes.classeJoueur import *
from classes.classeCombat.champion import *
from classes.classeCombat.lutteur import *
from classes.classeCombat.prophete import *
from classes.classeCombat.rhapsode import *
from classes.classeCombat.sangmelé import *
from classes.classeCombat.spadassin import *
from classes.classeCombat.spartiate import *
from classes.classePotion import Potion
from classes.classePotionEffet import PotionEffet
from classes.classeArmure import *

lutteur = Lutteur()
prophete = Prophete()
spadassin =  Spadassin()
hoplite =  Hoplite()
spartiate = Spartiate()
sangmele = SangMele()
rhapsode = Rhapsode()
champion = Champion()


dague = Arme("dague",1,6,"tranchant") #m : 3.5 (mais 2 fois plus d'attaque par tour si une dans chaque main) 🛡️
arc= Arme("arc",2,8,"perçant") #m 5 
masse=Arme("masse",2,5,"impact",2) #m : 7 🛡️
lance=Arme("lance",1,4,"perçant",2) #m : 5 🛡️
hallebarde = Arme("hallebarde",3,10,"tranchant") #m : 6.5
epeeCourte=Arme("xiphos",1,12,"tranchant") #m : 6.5 🛡️
eventailDeGuerre = Arme("Aihata",1,6,"tranchant") #m : 3.5 🛡️
arbalete = Arme("gastrophète", 1,3, "perçant",2) #m : 4
epeeLongue=Arme("kopis",0,8,"tranchant",2) #m : 8
Hache = Arme("hache",2,5,"tranchant",2) #m : 7 🛡️
poing=Arme("poing",0,1,"impact")

PotionSoinMineur = Potion("Soin Mineur",1,6,"aucun",heal=1,nbroll=2)
PotionSoinMajeur = Potion("Soin Majeur",1,8,"aucun",heal=1,nbroll=3)
Antidote = Potion("Antidote",0,0,"aucun","aucun",heal=1,descEffet="Soigne les effets de poison et les maladies")
AntidoteFort = Potion("Antidote puissant",1,4,"aucun","aucun",heal=1,descEffet="Soigne les effets de poison les plus fort et soigne les plus petites plaies")

PotionDeForce = PotionEffet("Potion de force",lambda joueur : augmenteStat("force",joueur),"Augmente la force de la personne qui la boie de 3",3,lambda joueur : augmenteStat("force",joueur,-3))
Aphrodisiaque = PotionEffet("Aphrodisiaque", lambda joueur : augmenteStat("charisme",joueur,6),"Augmente le charisme de 6",10,lambda joueur : augmenteStat("charisme",joueur,-6))

bouclier = Armure("Bouclier",2)
armureDeCuir = Armure("Armure de cuir",2) #spadassin
tunique = Armure("Vêtements",0) #prophete et rhapsode
armureDeFer = Armure("Armure en fer", 5) #champion
casque = Armure("Casque",1) #champion spartiate, hoplite, sang mele?
armuredeSpartiate= Armure("Armure de Spartiate",4) #spartiate
armureEnAcier = Armure("Armure en acier",6) # hoplite
armureDeBronze = Armure("Armure en bronze",3) #sang mele


Potions = [PotionSoinMineur,PotionSoinMajeur,Antidote, AntidoteFort, PotionDeForce,Aphrodisiaque]
lstArme= [poing,dague,arc,masse,lance,epeeCourte,epeeLongue,Hache,arbalete,hallebarde]
lstMob = []

Alina = Joueur("Ariane",2,8,3,8,4,[dague, eventailDeGuerre,tunique],{
    "Zeus" : 50,
    "Poséidon" : 50,
    "Artémis" : 50,
    "Ares" : 50,
    "Athéna" : 55,
    "Aphrodite" : 50,
    "Dionysos" : 50,
    "Demeter" : 50,
    "Hermès" : 50,
    "Apollo" : 50,
    "Héphaïstos" : 50
}, rhapsode) #humain assassin (ct corvo ici)
Omega = Joueur("Apolinna Lyscalie",8,8,5,4,0,[lance,bouclier,armureDeBronze,casque], {
    "Zeus" : 30,
    "Poséidon" : 50,
    "Artémis" : 50,
    "Ares" : 50,
    "Athéna" : 50,
    "Aphrodite" : 80,
    "Dionysos" : 50,
    "Demeter" : 50,
    "Hermès" : 50,
    "Apollo" : 50,
    "Héphaïstos" : 50
}, sangmele) #humain necromancien
Nick = Joueur("Emesthée", 3,2,7,2, 8,[arc,tunique],{
    "Zeus" : 50,
    "Poséidon" : 50,
    "Artémis" : 50,
    "Ares" : 50,
    "Athéna" : 50,
    "Aphrodite" : 50,
    "Dionysos" : 60,
    "Demeter" : 50,
    "Hermès" : 50,
    "Apollo" : 50,
    "Héphaïstos" : 50
}) #elf druide
Ange = Joueur("Luryä Dëlcanis",10, 9, 4,2,0,[hallebarde,armureDeCuir],{
    "Zeus" : 55,
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
}, spadassin) #humain mage
Ivan = Joueur("Ivan Khaos",10,4,4,5,7,6,3,1,40)

omegaid=494889341554786315
eddyid = 624291608258543657
lstJoueur=[Alina,Omega,Nick,Ange,Ivan]
alinaid = 1213903654655107114
angeid=957766156922531851
nickid=729086467779067995
ivanid=751592622308589622
lstId= {omegaid : Omega ,alinaid : Alina ,eddyid : None ,angeid :Ange ,nickid : Nick, ivanid : Ivan}


def lire(joueur):
    file = "PlayerData/"+joueur.nom+".json"
    try :  
        f=open(file,"r")
        return json.load(f)
    except FileNotFoundError : 
        print("Fichier non trouvé")
        return None
def remake(joueur):
    map=lire(joueur)
    if map == None:
        return
    joueur.force=map["force"]
    joueur.habilité=map["habilité"]
    joueur.constitution=map["constitution"]
    joueur.charisme=map["charisme"]
    joueur.foi=map["foi"]
    joueur.pv=map["pv"]
    joueur.niv=map["niv"]
    joueur.xp=map["xp"]
    joueur.monnaie=map["monnaie"]
    joueur.point=map["point"]
    joueur.coordX= map["coordX"]
    joueur.coordY = map["coordY"]
    joueur.maxpv=map["maxpv"]
    joueur.emoji = map["emoji"]
    joueur.inventaire = map["inventaire"]
    joueur.dieux = map["dieux"]
def remakeEnnemy() :
    file = "ennemyData/ennemy-PV"
    f=open(file,"r")
    dico = {}
    for i in f:
        info = (i.split(" "))
        nom = ""
        for elt in info[:len(info)-5]:
            nom+=elt+" "
        dico[nom.strip()] = info[len(info)-5:len(info)-1]
    f.close()
    for ennemy in lstMob:
        try :
            ennemy.pv,ennemy.coordX,ennemy.coordY,ennemy.emoji = dico[ennemy.nom]
            ennemy.emoji = codecs.decode(ennemy.emoji[2:-1], "unicode_escape").encode("latin1").decode("utf-8")
        except KeyError :
            continue
        
def R(nom,stat="dex"):
    return nom.roll(stat)

def augmenteStat(stat,joueur: Joueur,nb=3):
    joueur.modifStat(stat,nb)
def donneInfo(nom):
    for id in lstId.keys() :
        if nom==id:
            return lstId[id]
    for mob in lstMob:
        if mob.nom==nom:
            return mob
    if nom.lower()=="ange" or nom==Ange.nom:
        return Ange
    if nom=="Nick" or nom=="Elpi" or nom==Nick.nom:
        return Nick
    if nom=="Omega":
        return Omega
    if nom in ("Tykae","Ivan","ivan","tykae","Khaos","khaos","Ivan Khaos" ):
        return Ivan
    return None
def Dé(nb):
    if nb>=10:
        return """‎ 
                ⢀⣠⡴⣶⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⠶⠛⠁⠀⡇⠈⠙⠷⣤⣀⠀⠀⠀
⣴⠞⠫⠥⠄⠐⠒⠲⢓⠒⠂⠠⠤⠽⠳⢦⡀
⣿⠆⠀⠀⠀⠀⡰⠁⠀⢢⠀⠀⠀⠀  ⢠⢻⡇
⣿⠈⡄⠀⠀⡐             ⠣⠀⠀⢀⠆  ⣿
⣿⠀⠰⡀⡜⠀    **{}**   ⠀  ⠱⡀⡌⠀  ⣿⠀
⣿⢀⠠⠻⡒⠒⠒⠒⠒⠒⠒⢒⠟⠤⡀⣿
⠻⢧⣄⠀⠈⢄⠀⠀⠀⠀⡠⠊⠀⣀⣴⠟⠁
⠀⠀⠉⠛⢶⣄⡡⡀⠀⢔⣡⡴⠟⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠿⠾⠛⠁⠀⠀⠀⠀⠀⠀ 
    """.format(nb)

    else: 
        return """‎ 
                ⢀⣠⡴⣶⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⠶⠛⠁⠀⡇⠈⠙⠷⣤⣀⠀⠀⠀
⣴⠞⠫⠥⠄⠐⠒⠲⢓⠒⠂⠠⠤⠽⠳⢦⡀
⣿⠆⠀⠀⠀⠀⡰⠁⠀⢢⠀⠀⠀⠀  ⢠⢻⡇
⣿⠈⡄⠀⠀⡐             ⠣⠀⠀⢀⠆   ⣿
⣿⠀⠰⡀⡜⠀    **{}**  ⠀   ⠱⡀⡌       ⣿⠀
⣿⢀⠠⠻⡒⠒⠒⠒⠒⠒⠒⢒⠟⠤⡀⣿
⠻⢧⣄⠀⠈⢄⠀⠀⠀⠀⡠⠊⠀⣀⣴⠟⠁
⠀⠀⠉⠛⢶⣄⡡⡀⠀⢔⣡⡴⠟⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠿⠾⠛⠁⠀⠀⠀⠀⠀⠀
    """.format(nb)
def changestats(self : Perso,AutreSelf : Perso):
        self.force=AutreSelf.force
        self.dex=AutreSelf.dex
        self.intel = AutreSelf.intel
        coef = self.pv/self.maxpv
        self.pv =  int(AutreSelf.maxpv*coef)
        self.end=AutreSelf.end
        self.maxpv=10 + AutreSelf.end*(4+self.niv)
        self.esprit=AutreSelf.esprit
        self.magie=AutreSelf.magie
        self.eloquence=AutreSelf.eloquence
        self.perception=AutreSelf.perception
def knowweapon(name):
    for arme in lstArme:
        if arme.nom==name:
            return arme
    return poing
def update2():
    file = "ennemyData/ennemy-PV"
    f = open(file,"w")
    f.write("")
    f.close()
    upd = []
    for i in lstJoueur:
        upd.append(i)
    for player in upd:
        file = "PlayerData/"+player.nom+".json"
        f = open(file,"w")
        data = str(player.toJsonMap())
        f.write(data)
        f.close()
    file = "ennemyData/ennemy-PV"
    f = open(file,"a")
    for ennemy in lstMob :
        emoji = ennemy.emoji
        if emoji != "O" :
            emoji= str(ennemy.emoji.encode("utf-8"))
        data = f"{ennemy.nom} {ennemy.pv} {ennemy.coordX} {ennemy.coordY} {emoji} \n"
        f.write(data)
    f.close()
    return
def donneSort(name,user=None) :
    if user != None :
        for sort in user.sortTout :
            if sort.nom == name :
                return sort


def donnePotion(name):
    for potions in Potions:
        if potions.nom==name:
            return potions
def coup(user,dest,arme):
    if type(arme) == "A CHANGER ICI POUR SORTS ET CHANTS" and arme.heal:
        a=user.heal(dest,randint(arme.mini,arme.maxi))
        return f'{user} a soigné {dest} de {a} pv'
    else :
        a= user.attaque(dest,arme)
        a=int(a/2)+2
    if type(dest)!=Joueur :
            user.lv(a)
    if dest.pv<=0:
        dest.pv=0
        if type(dest)==Boss:
            user.lv(80)
        else :
            user.lv(10)
        lstMob.remove(dest)
        return f"{dest.nom} est mort"
        
    else :
        return f"il reste {dest.pv} pv à {dest.nom}"
def normalize(text):
    # Supprime les accents et met en minuscules
    return ''.join(
        c for c in unicodedata.normalize('NFD', text.lower())
        if unicodedata.category(c) != 'Mn'
    )
def getStat(nom):
    nom_normalise = normalize(nom)

    statnom = {
    # Charisme
    "charme": "charisme",
    "cha": "charisme",
    "chrm": "charisme",
    "charisme": "charisme",

    # Force
    "force":"force",
    "for": "force",
    "fo": "force",
    "frc": "force",
    "f": "force",

    # Habilité
    "habilite":"habilité",
    "hab": "habilité",
    "habi": "habilité",
    "habil": "habilité",
    "ha": "habilité",
    "h": "habilité",

    # Constitution
    "constitution":"constitution",
    "const": "constitution",
    "con": "constitution",
    "c": "constitution",
    "co": "constitution",

    # Foi
    "foi":"foi",
}
    if nom_normalise not in statnom.keys():
        raise ValueError()
    

    return statnom[nom_normalise]
def getRaceClasse(nom):
    nom_normalise = normalize(nom)

    raceClasse = {
        "lutteur": Lutteur(),
        "prophete": Prophete(),
        "spadassin": Spadassin(),
        "hoplite": Hoplite(),
        "spartiate": Spartiate(),
        "sangmele": SangMele(),
        "rhapsode": Rhapsode(),
        "champion": Champion(),
    }

    return raceClasse[nom_normalise]