from random import randint, shuffle
import discord
from discord.ext import commands
from bot_help import bothelp
from classes.classeArme import Arme
from classes.classeArmeLegendaire import ArmeLegendaire
from classes.classeBoss import Boss
from classes.classeCreature import Creature
from classes.classeJoueur import *
from classes.classeCombat.archer import Archer
from classes.classeCombat.assassin import Assassin
from classes.classeCombat.autreClasse import AutreClasse
from classes.classeCombat.druide import Druide
from classes.classeCombat.guerrier import Guerrier
from classes.classeCombat.mage import Mage
from classes.classeCombat.necromancien import Necromancien
from classes.classeCombat.paladin import Paladin
from classes.Race.elfe import Elfe
from classes.Race.geant import Geant
from classes.Race.humain import Humain
from classes.Race.mort import Mort
from classes.Race.nain import Nain
from classes.Race.Omniman import Omniman
from classes.Race.orc import Orc
from classes.classeCombat.berserker import Berserker
from classes.Race.raceAutre import AutreRace
from classes.classePotion import Potion
from classes.classePotionEffet import PotionEffet
from classes.classeSort import Sort
import unicodedata 

elfe = Elfe()
geant = Geant()
humain = Humain()
mort = Mort()
nain = Nain()
omniman = Omniman()
orc = Orc()


archer = Archer()
assassin = Assassin()
druide= Druide()
guerrier = Guerrier()
mage= Mage()
necromancien = Necromancien()
paladin=Paladin()
berserker = Berserker()


Wergla = Boss("Wergla",20,5,5,20,4,7,10,9,AutreRace("feu","glace"),AutreClasse("sacre","tranchant"))
Dragon = Boss("Dragon",7,18,4,14,13,4,8,12,AutreRace("foudre","glace"),AutreClasse("impact","tranchant"))
Alduin = Boss("Alduin",7,18,4,14,13,4,8,12,AutreRace("foudre","feu"),AutreClasse("impact","tranchant"))
Sorcier = Creature("Maxim",1,1,5,3,2,2,1,5,humain,mage)
Sorcier2 = Sorcier.copie()
Sorcier2.nom="Somea"
Sorcier3 = Sorcier.copie()
Sorcier3.nom="Vyse"
DemonAntiOmega = Boss("Chatiment du doute",10,9,3,9,7,9,3,0, AutreRace("",""),AutreClasse("",""))
"""Guerrier1 = Creature("Sam",5,6,0,5,2,1,1,0,humain,guerrier)
Guerrier2 = Guerrier1.copie()
Guerrier2.nom="Brise-Roche"
Guerrier3 = Guerrier1.copie()
Guerrier3.nom="Adam"
Guerrier4 = Guerrier1.copie()
Guerrier4.nom="Munch"
Guerrier5 = Guerrier1.copie()
Guerrier5.nom="Henry"""
Squelette1 = Creature("Squelette1",6,6,0,6,2,0,0,0,mort,archer)
Squelette2 = Creature("Squelette2",6,6,0,6,2,0,0,0,mort,guerrier)
Squelette3 = Creature("Squelette3",6,6,0,6,2,0,0,0,mort,mage)
Squelette4 = Creature("Squelette4",6,6,0,6,2,0,0,0,mort,guerrier)
Squelette5 = Creature("Squelette5",6,6,0,6,2,0,0,0,mort,guerrier)
Squelette6 = Creature("Squelette6",6,6,0,6,2,0,0,0,mort,guerrier)
Squelette7 = Creature("Squelette7",6,6,0,6,2,0,0,0,mort,archer)
Squelette8 = Creature("Squelette8",6,6,0,6,2,0,0,0,mort,archer)
"""Gob1 = Creature("1",4,3,1,5,2,2,2,1,AutreRace("feu","poison"), guerrier)
Gob2 = Gob1.copie("2")
Gob5 = Gob1.copie("6")"""
Slime1= Creature("Slime1",0,0,0,20,0,0,0,0,AutreRace("foudre","impact"),AutreClasse("feu","tranchant"))
Slime2 = Slime1.copie("Slime2")
Slime3 = Slime1.copie("Slime3")
Slime4 = Slime1.copie("Slime4")
Slime5 =Slime1.copie("Slime5")
Loup1 = Creature("Loup1",5,6,1,5,2,0,1,0,omniman,AutreClasse("tranchant","poison"))
Loup2 = Loup1.copie("Loup2")
Loup3 = Loup1.copie("Loup3")
Loup4 = Loup1.copie("Loup4")
Loup5 = Loup1.copie("Loup5")


lstMob=[Wergla,Dragon,Alduin,DemonAntiOmega,Sorcier,Sorcier2,Sorcier3,Squelette1 ,Squelette2 ,Squelette3 ,Squelette4,Squelette5,Squelette6,Squelette7,Squelette8,Slime1,Slime2,Slime3,Slime4 ,Slime5,Loup1,Loup2,Loup3,Loup4,Loup5]

dague = Arme("dague",1,6,"dex","tranchant") 
arc= Arme("arc",2,9,"dex","perçant")
masse=Arme("masse",2,5,"force","impact",2)
lance=Arme("lance",2,4,"dex","perçant",2)
epeeCourte=Arme("epeeCourte",3,5,"force","tranchant")
epeeLongue=Arme("epeeLongue",2,6,"force","tranchant",2)
Hache = Arme("hache",3,5,"force","tranchant",2)
Arbalete = Arme("arbalete",2,6,"dex","perçant")
serpe = Arme("serpe",1,3,"dex","tranchant",3)
briselame = Arme("briselame",1,3,"dex","perçant")
poing=Arme("poing",0,1,"force","impact")

FendDragon = ArmeLegendaire("FendDragon","force","magie",6,12,8,5,"tranchant")
ArcDeZephyr = ArmeLegendaire("ArcDeZephyr","dex","perception",1,4,6,8,"perçant",4)
lstArme= [poing,dague,arc,masse,lance,epeeCourte,epeeLongue,Hache,Arbalete,serpe,briselame,FendDragon]
PotionSoinMineur = Potion("Soin Mineur",5,10,"aucun",heal=1)
PotionSoinMajeur = Potion("Soin Majeur",15,30,"aucun",heal=1)
Antidote = Potion("Antidote",0,0,"aucun","aucun",heal=1,descEffet="Soigne les effets de poison et les maladies")
AntidoteFort = Potion("Antidote puissant",1,6,"aucun","aucun",heal=1,descEffet="Soigne les effets de poison les plus fort et soigne les plus petites plaies")
def augmenteStat(stat,joueur: Joueur,nb=3):
    joueur.modifStat(stat,nb)
augmenteForce =  lambda joueur : augmenteStat("force",joueur)
PotionDeForce = PotionEffet("Potion de force",augmenteForce,"Augmente la force de la personne qui la boie de 3",3,lambda joueur : augmenteStat("force",joueur,-3))
PotionDeSensAccru = PotionEffet("Potion de sens accrus", lambda joueur : augmenteStat("perception",joueur,6),"Augmente les sens du buveur et augmente sa perception de 6",10,lambda joueur : augmenteStat("perception",joueur,-6))

Potions = []
nbTurn = [0,0] #Nombre de tour passé, numéro de la personne qui doit jouer
OrdreTour =[]
PersonneSousEffet = {}
def lire(joueur):
    file = "PlayerData/"+joueur.nom
    f=open(file,"r")
    lst =[]
    for i in f:
        lst.append(int(i))
    f.close()
    return lst
def remake(joueur):
    lst=lire(joueur)
    joueur.force=lst[0]
    joueur.dex=lst[1]
    joueur.intel=lst[2]
    joueur.end=lst[3]
    
    joueur.perception=lst[4]
    joueur.eloquence=lst[5]
    joueur.esprit=lst[6]
    joueur.magie=lst[7]
    joueur.pv=lst[8]
    joueur.niv=lst[9]
    joueur.xp=lst[10]
    joueur.monnaie=lst[11]
    joueur.point=lst[12]
    joueur.mana=lst[13]
    joueur.bonus=lst[14]
    joueur.coordX= lst[15]
    joueur.coordY = lst[16]
    joueur.maxpv=(2)*joueur.end+5+joueur.bonus
    joueur.maxmana=int(joueur.magie +joueur.niv*2 + joueur.intel/2) * joueur.race.magie * joueur.classe.magie
    if type(joueur)==Joueur :
        joueur.maxpv=(4+joueur.niv)*joueur.end+10+joueur.bonus
        
def remakeEnnemy() :
    file = "ennemyData/ennemy-PV"
    f=open(file,"r")
    dico = {}
    for i in f:
        info = (i.split(" "))
        nom = ""
        for elt in info[:len(info)-3]:
            nom+=elt+" "
        dico[nom.strip()] = info[len(info)-3:]
    f.close()
    for ennemy in lstMob:
        ennemy.pv,ennemy.coordX,ennemy.coordY = dico[ennemy.nom]
remakeEnnemy()


Eddy = Joueur("Corvo Attano",3,10,4,5,6,3,5,4,35,humain,assassin) #humain assassin
Emma = Joueur("Nimrodel", 3,5,7,4,5,2,8,6,5,elfe,archer) #demi-elf archer
Monke = Joueur("Kogla",8,8,2,7,4,0,5,6,0,omniman,guerrier ) #singe hom-nimaux barbare
Omega = Joueur("Omega",4,3,5,4,7,3,6,8,15,humain,necromancien) #humain necromancien
Nexo = Joueur("Tayo",4,10,6,2,10,2,5,1,10,elfe,archer) #elf de la nuit archer
Nick = Joueur("Elpiguio", 3,2,7,2, 8,6,5,7,7,elfe,druide) #elf druide
Ange = Joueur("Laÿre",2, 6, 8,3,6,5, 4,6,16,humain,mage) #humain mage
PvP = Joueur("Mickaël Front",10,5,5,5,5,3,1,6,0,humain,mage) #humain mage de guerre
Ivan = Joueur("Ivan Khaos",10,4,4,5,7,6,3,1,40,humain,berserker)

OmegaBlue = Joueur("OmegaBlue",4,3,5,4,7,3,6,8,Omega.monnaie,humain,necromancien)
OmegaRed = Joueur("OmegaRed",8,3,2,7,6,0,6,8,Omega.monnaie,humain,necromancien)
OmegaGreen = Joueur("OmegaGreen",4,6,2,4,2,6,8,8,Omega.monnaie,humain,necromancien)
Ombre,rage=False,False

Stinger = Creature("Stinger",2,10,0,4,4,0,0,0,mort,archer)
Reaper = Creature("Reaper",2,4,0,4,10,0,0,0,mort,guerrier)
Fafnir = Creature("Fafnir",4,3,0,4,9,0,0,0,mort,omniman)
Lizardo = Creature("Lizardo",2,9,0,9,0,0,0,0,mort,omniman)
Slasher = Creature("Slasher",9,5,0,6,0,0,0,0,mort,guerrier)

remake(Eddy)
remake(Emma)
remake(Monke)
remake(Omega)
remake(OmegaRed)
remake(OmegaBlue)
remake(OmegaGreen)
for Omegas in (OmegaGreen,OmegaRed,OmegaBlue):
    Omegas.mana=Omega.mana
    Omegas.pv=Omega.pv
    Omegas.xp = Omega.xp
    Omegas.monnaie = Omega.monnaie
    Omegas.point=Omega.point
remake(Nexo)
remake(Nick)
remake(Ange)
remake(PvP)
remake(Stinger)
remake(Reaper)
remake(Fafnir)
remake(Lizardo)
remake(Slasher)
remake(Ivan)
Nick.faiblesse.append("Fafnir")
Nexo.faiblesse.append("sa taille")
Ivan.resistance.append("les femmes contrairement à l'admin")

Sort("Napalm",2,4,"feu",cout=5) # Sort de PVP que je garde au cas ou
Eddy.apprend(Sort("Assassinat",10,14,"perçant","dex",cout=6))
Eddy.apprend(Sort("Téléportation",0,0,"aucun","aucune",cout=2,porte=30))

Emma.apprend(Sort("Elementumkinesis - Feu",3,9,"feu",cout=4,porte=15))
Emma.apprend(Sort("Elementumkinesis - Foudre",3,9,"foudre",cout=4,porte=15))
Emma.apprend(Sort("Elementumkinesis - Eau",3,9,"glace",cout=4,porte=15))
Emma.apprend(Sort("Elementumkinesis - Terre",3,9,"terre",cout=4,porte=15))
Emma.apprend(Sort("Elementumkinesis - Vide",5,12,"aucun",cout=6,porte=10))


Monke.apprend(Sort("Singerie Ultime",3,9,"impact","force"))

Nick.apprend(Sort("Petites racines",0,2,"terre",porte=20))
Nick.apprend(Sort("Grandes racines",3,6,"terre",cout=6,porte=15))
Nick.apprend(Sort("Empoisonnement",0,1,"poison","esprit",porte=8))

Ange.apprend(Sort("Embrasement",0,3,"feu",porte=30))
Ange.apprend(Sort("Flèche de foudre",3,9,"foudre",cout=4,porte=30))
Ange.apprend(Sort("Nosferatu",3,3,"aucun","aucune",cout=3,porte=15))
Ange.apprend(Sort("Soin",4,8,"sacre","aucune",1,cout=2))

lstJoueur=[Eddy,Emma,Monke,Nexo,PvP,Slasher,Stinger,Omega,Nick,Ange,Reaper,Fafnir,Lizardo,Ivan]


#changestats(Omega,4,3,5,4,7,3,6,8) # 🔵 FORME BLEU 🔵
#changestats(Omega,8,3,2,7,6,0,6,8) # 🔴 FORME ROUGE 🔴
#changestats(Omega,4,6,2,4,2,6,8, 8) # 🟢 FORME VERT 🟢

def R(nom,stat="dex"):
    return nom.roll(stat)
omegaid=494889341554786315
eddyid = 624291608258543657
monkeid= 371985604994531329
emmaid = 685932363255251008
nexoid=545598839823007754
angeid=957766156922531851
nickid=729086467779067995
pvpid=487293928715059233
ivanid=751592622308589622
lstId= {omegaid : Omega ,monkeid : Monke ,eddyid : Eddy ,emmaid : Emma ,nexoid : Nexo,angeid :Ange ,nickid : Nick ,pvpid : PvP, ivanid : Ivan}
def donneInfo(nom):
    for id in lstId.keys() :
        if nom==id:
            return lstId[id]
    for mob in lstMob:
        if mob.nom==nom:
            return mob
    if nom.lower()=="ange" or nom==Ange.nom:
        return Ange
    if nom in ("Eddy","Corvo Attano","Corvo"):
        return Eddy
    if nom in ("PvP","Mickaël","Mickael","Mick","Ewan"):
        return PvP
    if nom=="Nexo" or nom=="Tayo":
        return Nexo
    if nom in ("Nimrodel","Emma","Nim"):
        return Emma
    if nom=="Monke" or nom=="Kogla":
        return Monke
    if nom=="Nick" or nom=="Elpi" or nom==Nick.nom:
        return Nick
    if nom=="Omega":
        return Omega
    if nom=="Slasher":
        return Slasher
    if nom=="Reaper":
        return Reaper
    if nom=="Fafnir":
        return Fafnir
    if nom=="Lizardo":
        return Lizardo
    if nom=="Stinger":
        return Stinger
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
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!",intents=intents)

for key in open("token","r"):
    token =key 
@client.command()
async def roll(ctx, stat="dex",nom=""):
    if nom=="":
        nom=ctx.author.id
    try :
        stat=getStat(stat)
        a =R(donneInfo(nom), stat)
        if a!=None:
            await ctx.send("https://tenor.com/view/angry-birds-gif-12007401521632546156")
            await ctx.send("Le résultat du dé est :")
            await ctx.send(Dé(a))
        else :
            await ctx.send("Merci de corriger votre commande")
            await ctx.send(f'{nom},{stat}')
    except ValueError :
        await ctx.send("Stat invalide")

def update2():
    file = "ennemyData/ennemy-PV"
    f = open(file,"w")
    f.write("")
    f.close()
    upd = []
    for i in lstJoueur:
        upd.append(i)
    upd.append(Slasher)
    upd.append(Reaper)
    upd.append(Fafnir)
    upd.append(Lizardo)
    upd.append(Stinger)
    upd.append(OmegaBlue)
    upd.append(OmegaGreen)
    upd.append(OmegaRed)
    for player in upd:
        file = "PlayerData/"+player.nom
        f = open(file,"w")
        data = player.getstat()+"\n"+player.getInfo()
        f.write(data)
        f.close()
    file = "ennemyData/ennemy-PV"
    f = open(file,"a")
    for ennemy in lstMob :
        data = f"{ennemy.nom} {ennemy.pv} {ennemy.coordX} {ennemy.coordY}\n"
        f.write(data)
    f.close()
    return
@client.command()
async def update(ctx):
    update2()
    await ctx.send("Données des joueurs mis à jour dans les fichiers. Merci")
@client.command()
async def level(ctx,stat):
    user=ctx.author.id
    user = donneInfo(user)
    if user==None :
        await ctx.send("Param invalide : Nom personnage")
    else :
        try :
            a = getStat(stat)
            if user == Omega :
                for Omegas in (OmegaGreen,OmegaRed,OmegaBlue):
                    Omegas.mana=Omega.mana
                    Omegas.pv=Omega.pv
                    Omegas.xp = Omega.xp
                    Omegas.monnaie = Omega.monnaie
                    Omegas.point=Omega.point
                    await ctx.send(Omegas.augmentStat(a))
            await ctx.send(user.augmentStat(a))
            update2()
        except ValueError:
            await ctx.send("Stat invalide")
def donneSort(name,user=None) :
    if user != None :
        for sort in user.sortTout :
            if sort.nom == name :
                return sort


def donnePotion(name):
    for potions in Potions:
        if potions.nom==name:
            return potions
@client.command()
async def lancePotion(ctx,dest,potion,user=""):
    if user=="":
        user=ctx.author.id
    user=donneInfo(user)
    dest=donneInfo(dest)
    potion = donnePotion(potion)
    if user==None or potion==None or dest==None:
        await ctx.send("Param invalide :")
        if user==None :
            await ctx.send("Nom attaquant invalide")
        if dest==None :
            await ctx.send("Nom cible invalide")
        if potion==None :
            await ctx.send("Nom sort invalide")
        return
    verif= type(user)==Joueur
    if verif :
        verif = potion.nom not in user.potion.keys()
    if verif :
        await ctx.send("Vous n'avez pas cette potion dans votre inventaire")
        return
    user.retirerPotion(potion)
    await ctx.send(f"{user.nom} lance {potion.nom} sur {dest.nom}, la potion sera instannément bu")
    await ctx.send(coup(user,dest,potion))
    update2()
@client.command()
async def lanceSort(ctx,dest,sort,user=""):
    if user=="":
        user=ctx.author.id
    user=donneInfo(user)
    dest=donneInfo(dest)
    sort = donneSort(sort,user)
    if user==None or sort==None or dest==None:
        await ctx.send("Param invalide :")
        if user==None :
            await ctx.send("Nom attaquant invalide")
        if dest==None :
            await ctx.send("Nom cible invalide")
        if sort==None :
            await ctx.send("Nom sort invalide")
        return
    verif= type(user)==Joueur
    if verif :
        verif = sort.nom not in user.sorts
    if verif :
        await ctx.send("Vous n'avez pas ce sort dans votre grimoire")
        return
    if verif :
        verif = user.mana - sort.cout <0
    if verif :
        await ctx.send("Vous n'avez pas assez de mana")
        return
    user.EnleveMana(sort.cout) 
    await ctx.send(f"{user.nom} lance {sort.nom} sur {dest.nom}")
    await ctx.send(coup(user,dest,sort))
    update2()
def coup(user,dest,arme):
    if type(arme) == Sort and arme.heal:
        a=user.heal(dest,randint(arme.mini,arme.maxi))
        return f'{user} a soigné {dest} de {a} pv'
    else :
        a= user.attaque(dest,arme)
        a=int(a/2)+2
    if type(dest)!=Joueur :
        if user.nom in ("Slasher","Reaper","Fafnir","Lizardo","Stinger") :
                Omega.lv(int(a/8))
                Eddy.lv(int(a/8))
                Ange.lv(int(a/8))
                PvP.lv(int(a/8))
                Nexo.lv(int(a/8))
                Nick.lv(int(a/8))
                Monke.lv(int(a/8))
                Emma.lv(int(a/8))
        else :
                user.lv(a)
    if dest.pv<=0:
        dest.pv=0
        if type(dest)==Boss:
            if user.nom in ("Slasher","Reaper","Fafnir","Lizardo","Stinger") :
                Omega.lv(80/8)
                Eddy.lv(int(80/8))
                Ange.lv(int(80/8))
                PvP.lv(int(80/8))
                Nexo.lv(int(80/8))
                Nick.lv(int(80/8))
                Monke.lv(int(80/8))
                Emma.lv(int(80/8))
            else :
                user.lv(80)
            lstMob.remove(dest)
        else :
            if user.nom in ("Slasher","Reaper","Fafnir","Lizardo","Stinger") :
                Omega.lv(int(10/8))
                Eddy.lv(int(10/8))
                Ange.lv(int(10/8))
                PvP.lv(int(10/8))
                Nexo.lv(int(10/8))
                Nick.lv(int(10/8))
                Monke.lv(int(10/8))
                Emma.lv(int(10/8))
            else :
                user.lv(10)
            lstMob.remove(dest)
        return f"{dest.nom} est mort"
        
    else :
        return f"il reste {dest.pv} pv à {dest.nom}"
@client.command()
async def attaque(ctx,dest,arme="poing",user=""):
    if user=="":
        user=ctx.author.id
    user=donneInfo(user)
    dest=donneInfo(dest)
    arme=knowweapon(arme)
    
    if user==None or arme==None or dest==None:
        await ctx.send("Param invalide :")
        if user==None :
            await ctx.send("Nom attaquant invalide")
        if dest==None :
            await ctx.send("Nom cible invalide")
        if arme==None :
            await ctx.send("Nom arme invalide")
        
        return
    
    
    
    await ctx.send(f"{user.nom} attaque {dest.nom} avec {arme.nom}")
    await ctx.send(coup(user,dest,arme))
    update2()
@client.command()
async def heal(ctx,dest,nb):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
        return
    if dest=="all":
        a=lstJoueur
        for p in a+[OmegaBlue,OmegaGreen,OmegaRed]:
            p.soin(int(nb))
            await ctx.send(f"{p.nom} a {p.pv} pv")
    else :
        a=donneInfo(dest)
        if a==None:
            await ctx.send("Cible invalide")
            return
        try :
            a.soin(int(nb))
            await ctx.send(f"{a.nom} a {a.pv} pv")
            update2()
        except ValueError :
            await ctx.send("Le deuxième paramètre doit être un nombre")
@client.command()
async def hit(ctx,dest,nb):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
        return
    if dest=="all":
        a=lstJoueur
        for p in a+[OmegaBlue,OmegaGreen,OmegaRed]:
            p.subitdegat(int(nb),"aucun")
            await ctx.send(f"{p.nom} a {p.pv} pv")
    else :
        a=donneInfo(dest)
        if a==None:
            await ctx.send("Cible invalide")
            return
        try :
            a.subitdegat(int(nb),"aucun")
            await ctx.send(f"{a.nom} a {a.pv} pv")
            update2()
        except ValueError :
            await ctx.send("Le deuxième paramètre doit être un nombre")
@client.command()
async def info(ctx,user=""):
    if user=="":
        user=ctx.author.id
    if donneInfo(user)==None :
        await ctx.send("Personne invalide")
        return
    await ctx.send(donneInfo(user))

def textDiscord(txt):
    if txt=="":
        return " "
    i = 0
    while txt[i]=="`":
        i+=1
    i=3-i
    j = len(txt)-1
    k=0
    while txt[j]=="`":
       j-=1
       k+=1
    j=3-k
    return "`"*i+txt+"`"*j

@client.command()
async def aide(ctx,commande="all"):
    msg = bothelp(commande)
    if len(msg)<=2000:
        await ctx.send(msg)
    else :
        nb = len(msg)
        for i in range(0,nb,1500):
            await ctx.send(textDiscord(msg[i:i+1500]))

@client.command()
async def mesSorts(ctx,user=""):
    if user=="":
        user=ctx.author.id
    user=donneInfo(user)
    if user.sorts==[]:
        await ctx.send("Vous n'avez aucun sort offensif")
        return
    a= str(user.sortTout)
    await ctx.send("Voici l'ensemble des sorts que vous possédez\n"+a[1:len(a)-1])
    
nbC=0
fAnge = Ange.force
dAnge = Ange.dex
iAnge = Ange.intel
mAnge = Ange.magie
@client.command()
async def changeForme(ctx,couleur=""):
    if ctx.author.id==omegaid:
        for Omegas in (OmegaGreen,OmegaRed,OmegaBlue):
            Omegas.mana=Omega.mana
            Omegas.pv=Omega.pv
            Omegas.xp = Omega.xp
            Omegas.monnaie = Omega.monnaie
            Omegas.point=Omega.point
        if Omega.mana<2 :
            ctx.send("Pas assez de mana")
            return
        if couleur in ("bleu","Bleu","blue","Blue"):
            changestats(Omega,OmegaBlue) # 
            Omega.EnleveMana(2)
            a = "🔵 FORME BLEUE 🔵"
        elif couleur in ("Rouge","rouge","Red","red"):
            changestats(Omega,OmegaRed) #
            Omega.EnleveMana(2) 
            a="🔴 FORME ROUGE 🔴"
        elif couleur in ("Vert","vert","Green","green"):
            changestats(Omega,OmegaGreen) # 
            Omega.EnleveMana(2)
            a="🟢 FORME VERTE 🟢"
        await ctx.send(a)
        update2()
    elif ctx.author.id==eddyid:
        global Ombre
        if couleur in ("Ombre","ombre"):
            if Eddy.mana < 4 :
                ctx.send("Pas assez de mana")
                return
            if Eddy.dex<16 and Eddy.perception<16:
                Ombre=True
                Eddy.dex+=6
                Eddy.perception+=6
                Eddy.EnleveMana(4)
                await ctx.send("🥷🏻Forme de l'ombre activée🥷🏻")
                return
            await ctx.send("Vous êtes déjà assez OP comme ca chef")
        else :
            if Eddy.dex<=10:
                await ctx.send("Vous êtes déjà pas assez OP comme ca chef")
                return
            Ombre=False
            Eddy.dex+=-6
            Eddy.perception+=-6
            await ctx.send("👤Forme de l'ombre désactivée👤")
        update2()
    elif ctx.author.id==monkeid:
        if couleur in ("Rage","rage"):
            global rage
            if not rage :
                rage=True
                Monke.force+=6
                Monke.dex+=6
                await ctx.send("😡Rage activée😡")
        else :
            if rage:
                Monke.force-=6
                Monke.dex-=6
                rage = False
                await ctx.send("🐒Rage désactivée🐒")
        update2()
    elif ctx.author.id == ivanid :
        global nbC
        if couleur.lower() == "normal":
            Ivan.force=14
            Ivan.dex=4
            nbC=0
            await ctx.send("Retour à votre taille normal")
        else :
            if Ivan.magie<4:
                ctx.send("Pas assez de mana")
                return                
            Ivan.force+=5
            Ivan.dex-=1
            nbC+=1
            Ivan.EnleveMana(4)
            await ctx.send(f"💪Vos muscles grandissent💪 (nombre d'utilisation consécutif : {nbC})")
        update2()
    elif ctx.author.id == nexoid:
        if couleur.lower() == "chaud":
            await ctx.send("https://tenor.com/view/il-fait-tarpin-chaud-meteo-m%C3%A9t%C3%A9o-grindingo-ta-grand-mere-gif-17456097805847733349")
            Nexo.resistance=["poison", "glace"]
        elif couleur.lower() == "froid":
            await ctx.send("Il fait pas tarpin chaud")
            Nexo.faiblesse=["glace, tranchant, sa taille"]
            Nexo.resistance+=["feu"]
        else :
            await ctx.send("Tu es de nouveau dans ta forme de base")
            Nexo.resistance=["poison", "foudre"]
            Nexo.faiblesse=["feu", "tranchant", "sa taille"]
        update2()
    elif ctx.author.id==angeid:
        couleur="épée"
        if Ange.magie <6 :
            couleur = "magie"
        if couleur.lower() =="épée" :
            Ange.force-=-6
            Ange.dex-=-6
            Ange.intel+=-4
            Ange.magie+=-4
        if couleur.lower() == "magie" :
            Ange.force-=6
            Ange.dex-=6
            Ange.intel+=4
            Ange.magie+=4
        await ctx.send(f"Changement de forme : mode {couleur}")
        update2()
    else :
        await ctx.send("Vous n'êtes pas utilisateur de forme")
@client.command()
async def payeNPC(ctx,nb,user=""):
    if user=="":
        user=ctx.author.id
    user=donneInfo(user)
    if user==None :
        await ctx.send("Param invalide :")
        if user==None :
            await ctx.send("Nom 1 invalide")
        return
    try :
        nb=int(nb)
        await ctx.send(user.paye(nb))
        update2()
    except ValueError :
        await ctx.send("Le premier paramètre doit être un nombre")
@client.command()
async def paye(ctx,cible,nb,user=""):
    if user=="":
        user=ctx.author.id
    user=donneInfo(user)
    cible=donneInfo(cible)
    if user==None or cible==None:
        await ctx.send("Param invalide :")
        if user==None :
            await ctx.send("Nom 1 invalide")
        if cible==None :
            await ctx.send("Nom 2 invalide")
        return
    try :
        nb=int(nb)
        await ctx.send(user.paye(nb,cible))
        update2()
    except ValueError :
        await ctx.send("Le deuxieme paramètre doit être un nombre")
@client.command()
async def addMoney(ctx,user,nb):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        if user=="all":
            for p in lstJoueur:
                if type(p)== Joueur :
                    p.monnaie+=int(nb)
                    await ctx.send(f'{p.nom} a {p.monnaie} pièces')
        else :
            user=donneInfo(user)
            if user== None :
                await ctx.send("Bro even u ? For real man ???")
                return
            user.monnaie+=int(nb)
            await ctx.send(f'{user.nom} a {user.monnaie} pièces')
        update2()
@client.command()
async def removeMoney(ctx,user,nb):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        if user=="all":
            for p in lstJoueur :
                if type(p)== Joueur :
                    p.monnaie-=int(nb)
                    await ctx.send(f'{p.nom} a {p.monnaie} pièces')
        else :
            user=donneInfo(user)
            if user== None :
                await ctx.send("Bro even u ? For real man ???")
                return
            user.monnaie-=int(nb)
            await ctx.send(f'{user.nom} a {user.monnaie} pièces')
        update2()
@client.command()
async def addXP(ctx,user,nb):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        if user=="all":
            for p in lstJoueur:
                if type(p)== Joueur :
                    p.lv(int(nb))
                    await ctx.send(f'ajout de {nb} xp a {p.nom}, il a désormais {p.xp} xp')
        else :
            user=donneInfo(user)
            if user== None :
                await ctx.send("Bro even u ? For real man ???")
                return
            user.lv(int(nb))
            await ctx.send(f'ajout de {nb} xp a {user.nom}, il a désormais {user.xp} xp')
        update2()
@client.command()
async def removeXP(ctx,user,nb):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        if user=="all":
            for p in lstJoueur:
                if type(p)== Joueur:
                    p.delv(int(nb))
                    await ctx.send(f'suppression de {nb} xp a {p.nom}, il a désormais {p.xp} xp')
        else :
            user=donneInfo(user)
            if user== None :
                await ctx.send("Bro even u ? For real man ???")
                return
            user.delv(int(nb))
            await ctx.send(f'suppression de {nb} xp a {user.nom}, il a désormais {user.xp} xp')
        update2()
        
string=""
@client.command()
async def ordre(ctx,*args):
    global string
    global OrdreTour
    retu =[]
    for i in lstJoueur:
        retu.append(i.nom)
    for i in args:
        retu.append(i)
    shuffle(retu)
    OrdreTour = retu
    string=""
    for i in range(len(retu)):
        string+="\n"+str(i+1)+". "+retu[i]
    await ctx.send(string)
@client.command()
async def refaireOrdre(ctx,grandeChaine):
    #La grande chaine est le message produit par la commande ordre, etant donné qu'au redemarrage, le bot oublie l'ordre de tour
    #on peut lui redonner en renvoyant exactement le message qu'il avait envoyé
    global OrdreTour
    couplesRangPersonne = grandeChaine.split("\n")
    for couple in couplesRangPersonne :
        OrdreTour.insert(couple[0],couple[1])
    ctx.send("Ordre refait a partir du message donnée")
@client.command()
async def getOrdre(ctx):
    global OrdreTour
    string=f"Numéro du tour : {nbTurn[0]+1}"
    for i in range(len(OrdreTour)):
        string+="\n"+str(i+1)+". "+OrdreTour[i]
    string+=f"C'est au tour de {OrdreTour[nbTurn[1]]}"
    await ctx.send(string)
@client.command()
async def next(ctx):
    global nbTurn
    global OrdreTour
    global PersonneSousEffet
    nbTurn[1]=(nbTurn[1]+1)%len(OrdreTour)
    if nbTurn[1]==0:
        nbTurn[0]+=1
    #Ici, mettre le code pour verifier que les effets ou les sorts qui ont une durée, s'arretent ou non
    for personne in PersonneSousEffet.keys():
        PersonneSousEffet[personne][0]+=1 
        if PersonneSousEffet[personne][0]>=PersonneSousEffet[personne][1]:
            PersonneSousEffet[personne][3](personne)
            del PersonneSousEffet[personne]
    ctx.send(f"C'est au tour de {OrdreTour[nbTurn[1]]}")
@client.command()
async def setMaxMob(ctx,nb):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        global maxMob
        maxMob=int(nb)
        await ctx.send("done")
@client.command()
async def setMaxBoss(ctx,nb):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        global maxBoss
        maxBoss=int(nb)
        await ctx.send("done")
maxMob=20


def normalize(text):
    # Supprime les accents et met en minuscules
    return ''.join(
        c for c in unicodedata.normalize('NFD', text.lower())
        if unicodedata.category(c) != 'Mn'
    )
def getStat(nom):
    nom_normalise = normalize(nom)

    statnom = {
    # Éloquence
    "elo": "eloquence",
    "eloquence": "eloquence",
    "eloq": "eloquence",
    "el": "eloquence",

    # Force
    "force":"force",
    "for": "force",
    "fo": "force",
    "frc": "force",
    "f": "force",

    # Dextérité
    "dexterite":"dex",
    "dex": "dex",
    "dext": "dex",
    "dexte": "dex",
    "dx": "dex",
    "d": "dex",

    # Intelligence
    "intelligence":"intel",
    "int": "intel",
    "intel": "intel",
    "intell": "intel",
    "inte": "intel",
    "i": "intel",

    # Endurance
    "endurance":"end",
    "end": "end",
    "endu": "end",
    "endur": "end",
    "en": "end",

    # Esprit
    "esprit":"esprit",
    "esp": "esprit",
    "espr": "esprit",
    "es": "esprit",
    "espri": "esprit",

    # Perception
    "perception":"perception",
    "per": "perception",
    "perc": "perception",
    "perce": "perception",
    "pc": "perception",
    "p": "perception",

    # Magie
    "magie":"magie",
    "mag": "magie",
    "ma": "magie",
    "m": "magie",
    "magi": "magie",
}
    if nom_normalise not in statnom.keys():
        raise ValueError()
    

    return statnom[nom_normalise]
def getRaceClasse(nom):
    nom_normalise = normalize(nom)

    raceClasse = {
        "paladin": paladin,
        "archer": archer,
        "assassin": assassin,
        "druide": druide,
        "guerrier": guerrier,
        "mage": mage,
        "necromancien": necromancien,
        "necro": necromancien,
        "humain": humain,
        "elfe": elfe,
        "elf" :elfe,
        "geant": geant,
        "mort": mort,
        "nain": nain,
        "omniman": omniman,
        "homnimaux" : omniman,
        "homnimal" : omniman,
        "hom-nimaux" : omniman,
        "hom-nimal" : omniman,
        "orc": orc
    }

    return raceClasse[nom_normalise]
@client.command()
async def createMob(ctx,nom,force,dex,intel,end,percep,elo,esp,magie,race,classe):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        if int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie) >maxMob :
            await ctx.send("retirer " + str(int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie)-maxMob)+" points")
        if int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie) <maxMob :
            await ctx.send("ajouter " + str(maxMob-(int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie)))+" points")
        else :
            lstMob.append(Creature(nom,int(force),int(dex),int(intel),int(end) , int(percep) , int(elo) , int(esp) , int(magie),getRaceClasse(race),getRaceClasse(classe)))
            await ctx.send(nom+ " vous fait face !")
@client.command()
async def createMobAutre(ctx,nom,force,dex,intel,end,percep,elo,esp,magie,race1,race2,classe1,classe2):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        if int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie) >maxMob :
            await ctx.send("retirer " + str(int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie)-maxMob)+" points")
        if int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie) <maxMob :
            await ctx.send("ajouter " + str(maxMob-(int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie)))+" points")
        else :
            lstMob.append(Creature(nom,int(force),int(dex),int(intel),int(end) , int(percep) , int(elo) , int(esp) , int(magie),AutreRace(race1,race2),AutreClasse(classe1,classe2)))
            await ctx.send(nom+ " vous fait face !")
maxBoss=80
@client.command()
async def createBoss(ctx,nom,force,dex,intel,end,percep,elo,esp,magie,race,classe):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        if int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie) >maxBoss :
            await ctx.send("retirer " + str(int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie)-maxBoss)+" points")
        if int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie) <maxBoss :
            await ctx.send("ajouter " + str(maxBoss-(int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie)))+" points")
        else :
            lstMob.append(Boss(nom,int(force),int(dex),int(intel),int(end) , int(percep) , int(elo) , int(esp) , int(magie),getRaceClasse(race),getRaceClasse(classe)))
            await ctx.send(nom+ " apparait...")
@client.command()
async def createBossAutre(ctx,nom,force,dex,intel,end,percep,elo,esp,magie,race1,race2,classe1,classe2):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        if int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie) >maxBoss :
            await ctx.send("retirer " + str(int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie)-maxBoss)+" points")
        if int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie) <maxBoss :
            await ctx.send("ajouter " + str(maxBoss-(int(force)+int(dex)+int(intel)+int(end) + int(percep) + int(elo) + int(esp) + int(magie)))+" points")
        else :
            lstMob.append(Boss(nom,int(force),int(dex),int(intel),int(end) , int(percep) , int(elo) , int(esp) , int(magie),AutreRace(race1,race2),AutreClasse(classe1,classe2)))
            await ctx.send(nom+ " apparait...")
@client.command()
async def augmentePV(ctx,nom,nb) :
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        user = donneInfo(nom)
        if user== None :
            await ctx.send("Bro even u ? For real man ???")
            return
        user.maxpv+=int(nb)
        user.pv+=int(nb)
        user.bonus+=int(nb)
        await ctx.send(f'{user.nom} a désormais {user.maxpv} PV max (actuel : {user.pv})')
        update2()
@client.command()
async def addMana(ctx,nom,nb):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        user = donneInfo(nom)
        if user== None :
            await ctx.send("Bro even u ? For real man ???")
            return
    user.AjouteMana(int(nb))
    await ctx.send(f'{user.nom} a désormais {user.mana} mana')
    update2()
@client.command()
async def concocter(ctx,potion,nb=1,personne="Nick"):
    perso = Nick
    if personne != "Nick" :
        perso = donneInfo(personne)
    if ctx.author.id not in (eddyid,nickid):
        await ctx.send("Eddy ou Nick tu n'es pas, te faire foutre tu vas !")
    else :
        potion=donneSort(potion)
        if potion==None:
            await ctx.send(f"Nom de potion invalide")
            return
        await ctx.send(f"ajout de {nb} {potion.nom} dans l'inventaire de {perso.nom}")
        perso.ajouterPotion(potion,nb)
        
@client.command()
async def r(ctx,format="1d20"):
    if  "d" not in format :
        await ctx.send("Format invalide (format attendu NdM : exemple 1d6, 3d8, 12d14)")
        return
    Dice= format.split("d")
    nbDice = 0
    nbFace = 0
    try :
        nbDice = int(Dice[0])
        nbFace = int(Dice[1])
    except ValueError :
        await ctx.send("Format invalide (format attendu NdM : exemple 1d6, 3d8, 12d14)")
        return
    result = 0
    lstResult = []
    for i in range(nbDice) :
        nb = randint(1,nbFace)
        lstResult.append(nb)
        result += nb
    await ctx.send(f"Résultat du lancé de dé(s) :\n\trésultat : {result}\n\ttous les dés : {lstResult}")
@client.command()
async def mesPotions(ctx,user="") :
    if user == "":
        user = ctx.author.id
    user=donneInfo(user)
    if user==None :
        await ctx.send("Utilisateur invalide")
        return
    potionsListe = str(list(user.potion.items()))
    await ctx.send(f"Voici l'ensemble des sorts que vous possédez\n{potionsListe[1:len(potionsListe)-1]}")
@client.command()
async def boirePotion(ctx, potion, buveur = ""):
    global PersonneSousEffet
    if buveur == "":
        buveur = ctx.author.id
    buveur = donneInfo(buveur)
    potion = donneSort(potion)
    if buveur == None :
        await ctx.send("Utilisateur invalide")
        return
    if potion==None:
        await ctx.send(f"Nom de potion invalide")
        return
    if potion not in buveur.potion.keys() :
        await ctx.send("Vous n'avez pas cette potion dans votre inventaire")
        return
    buveur.retirerPotion(potion)
    numTurn = nbTurn[0]*len(OrdreTour)+nbTurn[1]
    PersonneSousEffet[buveur.nom] = [numTurn,numTurn+potion.duree*len(OrdreTour),potion.antieffect]
    potion.effet(buveur) 
carte = []
@client.command()
async def createMap(ctx,longueur,largeur) :
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
        return
    global carte
    carte = []
    for i in range(int(largeur)):
        carte.append(["⬛"]*int(longueur))
    await ctx.send("map faite")
@client.command()
async def recreateMap(ctx,longueur,largeur) :
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
        return
    global carte
    carte = []
    for i in range(int(largeur)):
        carte.append(["⬛"]*int(longueur))
    for character in lstJoueur+lstMob:
        x= character.coordX
        y=character.coordY
        if x !=-1 and y != -1:
            if y >= len(carte):
                ctx.send(f"ligne invalide pour {character.nom}")
                continue
            if x >= len(carte[y]):
                ctx.send(f"colonne invalide pour {character.nom}")
                continue
            if type(character)== Joueur:
                emoji = ":"+normalize(character.nom.replace(" ",""))+":"
                carte[y][x] = emoji
        
    await ctx.send("map refaite")
@client.command()
async def endCombat(ctx) :
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
        return
    for character in lstJoueur+lstMob: 
        character.coordX =-1
        character.coordY =-1
    await ctx.send("fin du combat")
@client.command()
async def getMap(ctx):
    global carte
    await ctx.send("Echelle : Une case = 2.5m")
    affichage=""
    for ligne in carte :
        for char in ligne :
            affichage+=char+" "
        affichage+="\n"
    await ctx.send(affichage[:len(affichage)-1])
emojis = {"elpiguio" : "1344778833768874015","corvoattano" : "1345107588668199012","omega":"1344777152595230750","nimrodel" : "1344778054979027078","tayo":"1344788022205612203","layre":"1344795520975114270","ivankhaos" : "1345476484738973798"}
@client.command()
async def positionner(ctx,user,x,y):
    x=int(x)-1
    y=int(y)-1
    global carte
    if y >= len(carte) or y<0:
        await ctx.send("ligne invalide")
        return
    if x >= len(carte[y]) or x<0:
        await ctx.send("colonne invalide")
        return
    user=donneInfo(user)
    if user==None :
        await ctx.send("Utilisateur invalide")
        return
    emoji = "<:"+normalize(user.nom.replace(" ",""))+":"+emojis[normalize(user.nom.replace(" ",""))]+">"
    if carte[y][x] != "⬛" :
        await ctx.send("Position invalide, cette place est déjà prise")
        return
    carte[y][x] = emoji
    user.coordX = x 
    user.coordY = y
    await ctx.send("Position du joueur validé")
@client.command()
async def seDeplacer(ctx,x,y,personnage =""):
    x=int(x)-1
    y=int(y)-1
    global carte
    if y >= len(carte) or y<0:
        await ctx.send("ligne invalide")
        return
    if x >= len(carte[y]) or x<0:
        await ctx.send("colonne invalide")
        return
    user=donneInfo(ctx.author.id)
    if personnage !="" and ctx.author.id==eddyid :
        user = donneInfo(personnage)
    if user==None :
        await ctx.send("Utilisateur invalide")
        return
    
    emoji = "<:"+normalize(user.nom.replace(" ",""))+":"+emojis[normalize(user.nom.replace(" ",""))]+">"
    if carte[y][x] != "⬛" :
        await ctx.send("Position invalide, cette place est déjà prise")
        return
    if abs(user.coordX - x )> 2 or abs(user.coordY - y) > 2 :
        await ctx.send("Vous essayez d'aller trop loin. Si vous souhaitez \"courir\", faite cette commande 2 fois")
        return
    carte[user.coordY][user.coordX] = "⬛"
    carte[y][x] = emoji
    user.coordX = x 
    user.coordY = y
    await ctx.send("Position du joueur validé")
client.run(token)
update2()
print("au revoir")
