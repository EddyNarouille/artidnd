from classes.classeArme import Arme
from classes.classeArmeLegendaire import ArmeLegendaire
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
from random import randint


lutteur = Lutteur()
prophete = Prophete()
spadassin =  Spadassin()
hoplite =  Hoplite()
spartiate = Spartiate()
sangmele = SangMele()
rhapsode = Rhapsode()
champion = Champion()


def soinHerbe(nb,joueur : Perso) :
    nb=nb+randint(1,nb)
    if "Déméter" in joueur.faveurs :
        nb*=2
    if "Déméter" in joueur.coleres :
        nb*=0.5
    if "Déméter" in joueur.maledictions :
        nb=0
    joueur.soin(nb)
HerbeDeSoin = lambda joueur : soinHerbe(4,joueur)
GrandeHerbeDeSoin = lambda joueur : soinHerbe(10,joueur)
PotionSoinMineur = Potion("Soin Mineur",1,6,heal=1,nbroll=3)
PotionSoinMajeur = Potion("Soin Majeur",1,8,heal=1,nbroll=4)
Antidote = Potion("Antidote",0,0,heal=1,descEffet="Soigne les effets de poison et les maladies")
AntidoteFort = Potion("Antidote puissant",1,4,heal=1,descEffet="Soigne les effets de poison les plus fort et soigne les plus petites plaies")
nectar = Potion("Nectar",1,12,1,4)
ambroisie = Potion("Ambroisie",1,8,1,6)
PotionDeForce = PotionEffet("Zythogala",lambda joueur : joueur.modifStat("force",3),"Augmente la force de la personne qui la boie de 3",3,lambda joueur : joueur.modifStat("force",-3))
Aphrodisiaque = PotionEffet("Aphrodisiaque", lambda joueur : joueur.modifStat("charisme",6),"Augmente le charisme de 6",10,lambda joueur : joueur.modifStat("charisme",-6))

dague = Arme("dague",1,6,"tranchant",uneMain=True) #m : 3.5 (mais 2 fois plus d'attaque par tour si une dans chaque main) 🛡️
arc= Arme("arc",2,8,"perçant") #m 5 
masse=Arme("masse",2,5,"impact",2,True) #m : 7 🛡️
lance=Arme("lance",1,5,"perçant",2,True) #m : 6 🛡️
hallebarde = Arme("hallebarde",3,10,"tranchant") #m : 6.5
epeeCourte=Arme("xiphos",1,12,"tranchant",uneMain=True) #m : 6.5 🛡️
eventailDeGuerre = Arme("aihata",1,6,"tranchant",uneMain=True) #m : 3.5 🛡️
arbalete = Arme("gastrophète", 1,3, "perçant",2) #m : 4
epeeLongue=Arme("kopis",0,8,"tranchant",2) #m : 8
marteauDeFeuHephaistos = ArmeLegendaire("Dédale","foi",mini=2,maxi=9,nbroll=2,req1=0,req2=0,type="feu")
Hache = Arme("hache",2,5,"tranchant",2,uneMain=True) #m : 7 🛡️
poing=Arme("poing",1,2,"impact")
bouclier = Armure("Bouclier",1)
armureDeCuir = Armure("Armure de cuir",1) #spadassin
tunique = Armure("Tunique",0) #prophete et rhapsode
armureDeFer = Armure("Armure en fer", 4) #champion
casque = Armure("Casque",1) #champion spartiate, hoplite, sang mele?
armuredeSpartiate= Armure("Armure de Spartiate",3) #spartiate
armureEnAcier = Armure("Armure en acier",5) # hoplite
armureDeBronze = Armure("Armure en bronze",2) #sang mele
bouclierAsWeapon = Arme("bouclier",1,2,"contendant",uneMain=True)
lstArme= [poing,dague,arc,masse,lance,epeeCourte,epeeLongue,Hache,arbalete,hallebarde]
lstArmure = [bouclier,armureDeBronze,armureEnAcier,armureDeCuir,armureDeFer,armuredeSpartiate,casque,tunique]
lstArmeMob = [Arme("griffes"),1,4,"tranchant"]
lstArmeLegendaire = [marteauDeFeuHephaistos]
Potions = [PotionSoinMineur,PotionSoinMajeur,Antidote, AntidoteFort, PotionDeForce,Aphrodisiaque]

lstMob = []
eddyid = 624291608258543657
emojis = {"elpiguio" : "1344778833768874015",
          "corvoattano" : "1345107588668199012",
          "omega":"1344777152595230750",
          "nimrodel" : "1344778054979027078",
          "tayo":"1344788022205612203",
          "layre":"1344795520975114270",
          "ivankhaos" : "1480290105662112006"}
"""omegaid=494889341554786315
alinaid = 1213903654655107114
angeid=957766156922531851
nickid=729086467779067995
ivanid=751592622308589622
Alina = Joueur("Ariane",2,8,3,8,4,[dague, eventailDeGuerre,tunique],{
    "Zeus" : 50,
    "Poséidon" : 50,
    "Artémis" : 50,
    "Arès" : 50,
    "Athéna" : 55,
    "Aphrodite" : 50,
    "Dionysos" : 50,
    "Déméter" : 50,
    "Hermès" : 50,
    "Apollon" : 50,
    "Héphaïstos" : 50
}, rhapsode,joueurid= alinaid) #humain assassin (ct corvo ici)
Omega = Joueur("Apolinna Lyscalie",8,8,5,4,0,[lance,bouclier,armureDeBronze,casque], {
    "Zeus" : 30,
    "Poséidon" : 50,
    "Artémis" : 50,
    "Arès" : 50,
    "Athéna" : 50,
    "Aphrodite" : 80,
    "Dionysos" : 50,
    "Déméter" : 50,
    "Hermès" : 50,
    "Apollon" : 50,
    "Héphaïstos" : 50
}, sangmele,joueurid=omegaid) #humain necromancien
Nick = Joueur("Emesthée", 3,2,7,2, 8,[arc,tunique],{
    "Zeus" : 50,
    "Poséidon" : 50,
    "Artémis" : 50,
    "Arès" : 50,
    "Athéna" : 50,
    "Aphrodite" : 50,
    "Dionysos" : 60,
    "Déméter" : 50,
    "Hermès" : 50,
    "Apollon" : 50,
    "Héphaïstos" : 50
},prophete,joueurid=nickid) #elf druide
Ange = Joueur("Luryä Dëlcanis",10, 9, 4,2,0,[hallebarde,armureDeCuir],{
    "Zeus" : 55,
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
}, spadassin,joueurid=angeid) #humain mage
Ivan = None#Joueur("Ivan Khaos",10,4,4,5,7,6,3,1,40)

"""
lstJoueur=[]
lstId= {}
