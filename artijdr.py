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
Guerrier1 = Creature("Sam",5,6,0,5,2,1,1,0,humain,guerrier)
Guerrier2 = Guerrier1.copie()
Guerrier2.nom="Brise-Roche"
Guerrier3 = Guerrier1.copie()
Guerrier3.nom="Adam"
Guerrier4 = Guerrier1.copie()
Guerrier4.nom="Munch"
Guerrier5 = Guerrier1.copie()
Guerrier5.nom="Henry"
Squelette1 = Creature("Squelette1",6,6,0,6,2,0,0,0,mort,archer)
Squelette2 = Creature("Squelette2",6,6,0,6,2,0,0,0,mort,guerrier)
Squelette3 = Creature("Squelette3",6,6,0,6,2,0,0,0,mort,mage)
Squelette4 = Creature("Squelette4",6,6,0,6,2,0,0,0,mort,guerrier)
Squelette5 = Creature("Squelette5",6,6,0,6,2,0,0,0,mort,guerrier)
Squelette6 = Creature("Squelette6",6,6,0,6,2,0,0,0,mort,guerrier)
Squelette7 = Creature("Squelette7",6,6,0,6,2,0,0,0,mort,archer)
Squelette8 = Creature("Squelette8",6,6,0,6,2,0,0,0,mort,archer)
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


lstMob=[Wergla,Dragon,Alduin,Sorcier,Sorcier2,Sorcier3,Guerrier1,Guerrier2 ,Guerrier3,Guerrier4,Guerrier5,Squelette1 ,Squelette2 ,Squelette3 ,Squelette4,Squelette5,Squelette6,Squelette7,Squelette8,Slime1,Slime2,Slime3,Slime4 ,Slime5,Loup1,Loup2,Loup3,Loup4,Loup5]
""""
💪Poing : 0 
🏹Dague : 1 a 6 dégâts (multipliable par 2 si dans le dos) 
🏹Arc : 0 a 9 dégâts 
💪 masse et marteau : 2 a 8 dégâts 
🏹Lance : 2 a 7 dégâts
💪Épée courte : 3 a 5 dégâts 
💪Épée longue : 3 a 7 dégâts 
💪Hache : 4 a 6 dégâts
🧠 Sort faible offensif  : 0 à 3 dégâts
🧠 Sort puissant offensif : 3 a 11 dégâts 
💪 = Plus 1 dégâts tous les 2 points de force
🏹 = Plus 1 dégâts tous les 2 points de dextérité
🧠 = plus 1 dégâts tous les 2 points d'intelligence
"""
dague = Arme("dague",1,6,"dex","tranchant") 
arc= Arme("arc",0,9,"dex","perçant")
masse=Arme("masse",2,5,"force","impact",2)
lance=Arme("lance",2,4,"dex","perçant",2)
epeeCourte=Arme("epeeCourte",3,5,"force","tranchant")
epeeLongue=Arme("epeeLongue",2,6,"force","tranchant",2)
Hache = Arme("hache",3,5,"force","tranchant",2)
sortFaible = []
sortFort = []
sortDeZone = []
Arbalete = Arme("arbalete",2,6,"dex","perçant")
serpe = Arme("serpe",1,3,"dex","tranchant",3)
briselame = Arme("briselame",1,3,"dex","perçant")
poing=Arme("poing",0,1,"force","impact")

FendDragon = ArmeLegendaire("FendDragon","force","magie",6,12,8,5,"tranchant")
ArcDeZephyr = ArmeLegendaire("ArcDeZephyr","dex","perception",1,4,6,8,"perçant",4)
lstArme= [poing,dague,arc,masse,lance,epeeCourte,epeeLongue,Hache,Arbalete,serpe,briselame,FendDragon]
PotionSoinMineur = Potion("Soin Mineur",5,10,"aucun")
Potions = []
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
    joueur.maxpv=(4+joueur.niv)*joueur.end+10+lst[14]
    joueur.maxmana=int(joueur.magie +joueur.niv*2 + joueur.intel/2) * joueur.race.magie * joueur.classe.magie
    maxpvInf=0
    if type(joueur)==Joueur :
        maxpvInf = (4+joueur.niv)*joueur.end+10+lst[14]
    if joueur.maxpv < maxpvInf :
        print(joueur.nom," a une erreur de pvmax")
        print(joueur.maxpv, " : ", maxpvInf)




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

sortFort.append(Sort("Elementumkinesis - Feu",3,9,"feu",cout=4))
sortFort.append(Sort("Elementumkinesis - Foudre",3,9,"foudre",cout=4))
sortFort.append(Sort("Elementumkinesis - Eau",3,9,"glace",cout=4))
sortFort.append(Sort("Elementumkinesis - Terre",3,9,"terre",cout=4))

sortFort.append(Sort("Singerie Ultime",3,9,"impact","force"))

sortFaible.append(Sort("Petites racines",0,3,"terre"))
sortFort.append(Sort("Grandes racines",3,9,"terre",cout=6))
sortFaible.append(Sort("Empoisonnement",0,1,"poison","esprit"))

sortFaible.append(Sort("Soin",4,4,"sacre","aucune",1,cout=1))

sortFaible.append(Sort("Embrasement",0,3,"feu"))
sortFort.append(Sort("Flèche de foudre",3,9,"foudre",cout=4))
sortFaible.append(Sort("Nosferatu",3,3,"aucun","aucune",cout=3))

sortDeZone.append(Sort("Napalm",2,4,"feu",cout=5))
sortFort.append(Sort("Assassinat",10,14,"perçant","dex",cout=6))
sortFaible.append(Sort("Téléportation",0,0,"aucun","aucune",cout=2))
Eddy.apprend(Sort("Assassinat",10,14,"perçant","dex"))
Eddy.apprend(Sort("Téléportation",0,0,"aucun","aucune",cout=2))

Emma.apprend(Sort("Elementumkinesis - Feu",3,9,"feu"))
Emma.apprend(Sort("Elementumkinesis - Foudre",3,9,"foudre"))
Emma.apprend(Sort("Elementumkinesis - Eau",3,9,"glace"))
Emma.apprend(Sort("Elementumkinesis - Terre",3,9,"terre"))

Monke.apprend(Sort("Singerie Ultime",3,9,"impact","force"))

Nick.apprend(Sort("Petites racines",0,3,"terre"))
Nick.apprend(Sort("Grandes racines",3,9,"terre"))
Nick.apprend(Sort("Empoisonnement",0,1,"poison","esprit"))

Ange.apprend(Sort("Embrasement",0,3,"feu"))
Ange.apprend(Sort("Flèche de foudre",3,9,"foudre"))
Ange.apprend(Sort("Nosferatu",3,3,"aucun","aucune"))
Ange.apprend(Sort("Soin",4,4,"sacre","aucune",1))

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

def donneSort(name):
    for sort in sortDeZone+sortFaible+sortFort+Potions:
        if sort.nom==name:
            return sort
@client.command()
async def lanceSort(ctx,dest,sort,user=""):
    if user=="":
        user=ctx.author.id
    user=donneInfo(user)
    dest=donneInfo(dest)
    sort = donneSort(sort)
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
        if type(dest)==Joueur :
            if user.nom in ("Slasher","Reaper","Fafnir","Lizardo","Stinger") :
                Omega.lv(int(30/8))
                Eddy.lv(int(30/8))
                Ange.lv(int(30/8))
                PvP.lv(int(30/8))
                Nexo.lv(int(30/8))
                Nick.lv(int(30/8))
                Monke.lv(int(30/8))
                Emma.lv(int(30/8))
            else :
                user.lv(30)
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
            p.subitdegat(int(nb))
            await ctx.send(f"{p.nom} a {p.pv} pv")
    else :
        a=donneInfo(dest)
        if a==None:
            await ctx.send("Cible invalide")
            return
        try :
            a.subitdegat(int(nb))
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
async def MesSorts(ctx,user=""):
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
    retu =[]
    for i in lstJoueur:
        retu.append(i.nom)
    for i in args:
        retu.append(i)
    shuffle(retu)
    string=""
    for i in range(len(retu)):
        string+="\n"+str(i+1)+". "+retu[i]
    await ctx.send(string)
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
    "dexterite":"dextérité",
    "dex": "dextérité",
    "dext": "dextérité",
    "dexte": "dextérité",
    "dx": "dextérité",
    "d": "dextérité",

    # Intelligence
    "intelligence":"intelligence",
    "int": "intelligence",
    "intel": "intelligence",
    "intell": "intelligence",
    "inte": "intelligence",
    "i": "intelligence",

    # Endurance
    "endurance":"endurance",
    "end": "endurance",
    "endu": "endurance",
    "endur": "endurance",
    "en": "endurance",

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
    user.AjouteMana(nb)
    await ctx.send(f'{user.nom} a désormais {user.mana} mana')
    update2()
@client.command()
async def concocter(ctx,potion,nb=1):
    if ctx.author.id not in (eddyid,nickid):
        await ctx.send("Eddy ou Nick tu n'es pas, te faire foutre tu vas !")
    else :
        potion=donneSort(potion)
        if potion==None:
            await ctx.send(f"Nom de potion invalide")
            return
        await ctx.send(f"ajout de {potion} dans l'inventaire d'{Nick.nom}")
        Nick.ajouterPotion(potion,nb)
        
client.run(token)
update2()
print("au revoir")
