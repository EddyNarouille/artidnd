from random import randint, shuffle
import discord
from discord.ext import commands
from bot_help import bothelp
from classes.classeBoss import Boss
from classes.classeCreature import Creature
from classes.classeJoueur import *
from functions import *



nbTurn = [0,0] #Nombre de tour passé, numéro de la personne qui doit jouer
OrdreTour =[]
PersonneSousEffet = {}

remakeEnnemy()




eddyid = 624291608258543657

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
            await ctx.send(user.augmentStat(a))
            update2()
        except ValueError:
            await ctx.send("Stat invalide")

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
async def attaque(ctx,dest,arme="poing",user=""):
    if user=="":
        user=ctx.author.id
    user=donneInfo(user)
    dest=donneInfo(dest)
    arme=knowweapon(arme)
    if user==None or arme==None or dest==None or arme not in user.inventaire:
        await ctx.send("Param invalide :")
        if user==None :
            await ctx.send("Nom attaquant invalide")
        if dest==None :
            await ctx.send("Nom cible invalide")
        if arme==None :
            await ctx.send("Nom arme invalide")
        if arme not in user.inventaire :
            await ctx.send("Vous n'avez pas cet arme (rip bozo)")
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
        for p in a:
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
        for p in a:
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
    user = donneInfo(user)
    if user==None :
        await ctx.send("Personne invalide")
        return
    await ctx.send(user)
@client.command()
async def inventaire(ctx,user="") :
    if user=="":
        user=ctx.author.id
    user = donneInfo(user)
    if user==None :
        await ctx.send("Personne invalide")
        return
    await ctx.send(user.monStuff())

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
async def faveurs(ctx,user=""):
    if user=="":
        user=ctx.author.id
    user=donneInfo(user)
    if user==None :
        await ctx.send("Personne invalide")
        return
    await ctx.send(user.getDieux())
    
nbC=0

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
async def updateFaveur(ctx,user,dieu,nb):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        if user=="all":
            for p in lstJoueur:
                if type(p)== Joueur :
                    p.updateFaveurs(dieu,nb)
        else :
            user=donneInfo(user)
            if user== None :
                await ctx.send("Bro even u ? For real man ???")
                return
            user.updateFaveurs(dieu,nb)
        await ctx.send(f'Faveur modifié')
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
        indiceJoueur = couple.split(". ")
        OrdreTour.insert(int(indiceJoueur[0]),indiceJoueur[1])
    await ctx.send("Ordre refait a partir du message donnée")
@client.command()
async def getOrdre(ctx):
    global OrdreTour
    string=f"Numéro du tour : {nbTurn[0]+1}"
    for i in range(len(OrdreTour)):
        string+="\n"+str(i+1)+". "+OrdreTour[i]
    string+=f"\nC'est au tour de {OrdreTour[nbTurn[1]]}"
    await ctx.send(string)
@client.command()
async def next(ctx):
    global nbTurn
    global OrdreTour
    global PersonneSousEffet
    nbTurn[1]=(nbTurn[1]+1)%len(OrdreTour)
    if nbTurn[1]==0:
        nbTurn[0]+=1
    PersonneJoue= OrdreTour[nbTurn[1]]
    #Ici, mettre le code pour verifier que les effets ou les sorts qui ont une durée, s'arretent ou non 
    #(je me rend compte ca fait tres ia ce commentaire wtf)
    perso = donneInfo(PersonneJoue)
    if perso.poison : 
        perso.compteur+=1
        perso.subitdegat(2,"aucun")
        await ctx.send(f"{perso.nom} prend 2 points de dégat dû au poison")
        if perso.compteur==3 :
            perso.poison = False
            await ctx.send(f"{perso.nom} n'est plus empoisonné")
    for personne in PersonneSousEffet.keys():
        PersonneSousEffet[personne][0]+=1 
        if PersonneSousEffet[personne][0]>=PersonneSousEffet[personne][1]:
            PersonneSousEffet[personne][2](personne)
            del PersonneSousEffet[personne]
    await ctx.send(f"C'est au tour de {PersonneJoue}")




@client.command()
async def createMob(ctx,nom,force,habilite,constitution,charisme,foi,classe,niveau, *args):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        payload = {
            "nom" : nom,
            "force" : force,
            "habilité" : habilite,
            "constitution" : constitution,
            "charisme" : charisme,
            "foi" : foi,
            "classe" : str(getClasse(classe)),
            "inventaire" : donneStuff(args),
            "niveau" :  niveau,
            }
        lstMob.append(Creature(payload))
        await ctx.send(nom+ " vous fait face !")
@client.command()
async def createBoss(ctx,nom,force,habilite,constitution,charisme,foi,classe,niveau,*args):
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        payload = {
            "nom" : nom,
            "force" : force,
            "habilité" : habilite,
            "constitution" : constitution,
            "charisme" : charisme,
            "foi" : foi,
            "classe" : str(getClasse(classe)),
            "inventaire" : donneStuff(args),
            "niveau" :  niveau,
            }
        lstMob.append(Boss(payload))
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
        await ctx.send(f'{user.nom} a désormais {user.maxpv} PV max (actuel : {user.pv})')
        update2()
        
@client.command()
async def concocter(ctx,potion,personne,nb=1):
    if ctx.author.id not in (eddyid):
        await ctx.send("Eddy ou Nick tu n'es pas, te faire foutre tu vas !")
    else :
        perso = donneInfo(personne)
        potion=donnePotion(potion)
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
    except IndexError :
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
    await ctx.send(f"Voici l'ensemble des potions que vous possédez\n{potionsListe[1:len(potionsListe)-1]}")
@client.command()
async def boirePotion(ctx, potion, buveur = ""):
    global PersonneSousEffet
    if buveur == "":
        buveur = ctx.author.id
    buveur = donneInfo(buveur)
    potion = donnePotion(potion)
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
    if type(potion) == PotionEffet :
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
        x= int(character.coordX)
        y=int(character.coordY)
        if x !=-1 and y != -1 and (character.pv>0 or type(character) == Perso):
            if y >= len(carte):
                ctx.send(f"ligne invalide pour {character.nom}")
                continue
            if x >= len(carte[y]):
                ctx.send(f"colonne invalide pour {character.nom}")
                continue
            if type(character)== Joueur:
                emoji = "<:"+normalize(character.nom.replace(" ",""))+":"+emojis[normalize(character.nom.replace(" ",""))]+">"
                carte[y][x] = emoji
            else :
                carte[y][x] = character.emoji
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
smolspace = "\u202F"
@client.command()
async def getMap(ctx):
    global carte
    axis = f""
    for i in range(len(carte[0])):
        axis+=["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟","⏸️","⑫"][i]
    affichage=f"Echelle : Une case = 2.5m\n{axis}\n"
    i=0
    for ligne in carte :
        i+=1
        for char in ligne :
            affichage+=char
        affichage+= str(i) 
        affichage+="\n"
    await ctx.send(affichage)
emojis = {"elpiguio" : "1344778833768874015","corvoattano" : "1345107588668199012","omega":"1344777152595230750","nimrodel" : "1344778054979027078","tayo":"1344788022205612203","layre":"1344795520975114270","ivankhaos" : "1480290105662112006"}
@client.command()
async def positionner(ctx,user,x,y,emj=""):
    x=int(x)-1
    y=int(y)-1
    global carte
    if y >= len(carte) or y<0:
        await ctx.send("ligne invalide")
        return
    if x >= len(carte[y]) or x<0:
        await ctx.send("colonne invalide")
        return
    if carte[y][x] != "⬛" :
        await ctx.send("Position invalide, cette place est déjà prise")
        return
    if user == "obstacle" : 
        carte[y][x] ="🧱"
        await ctx.send("Position de l'obstacle validé")
        return 
    user=donneInfo(user)
    if user==None :
        await ctx.send("Utilisateur invalide")
        return
    if type(user) == Joueur :
        emoji = "<:"+normalize(user.nom.replace(" ",""))+":"+emojis[normalize(user.nom.replace(" ",""))]+">"
        carte[y][x] = emoji
    else :
        carte[y][x] = emj
        user.emoji = emj
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
