from random import randint, shuffle
import discord
from discord.ext import commands
from discord import app_commands
from discord.utils import MISSING
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

intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix="!",intents=intents)

for key in open("token","r"):
    token =key 
@client.command()
async def roll(ctx, stat="habilité",nom=""):
    if nom=="":
        nom=ctx.author.id
    try :
        stat=getStat(stat)
        a,bonus,limit =R(donneInfo(nom), stat)
        if a!=None:
            await ctx.send("https://tenor.com/view/angry-birds-gif-12007401521632546156")
            await ctx.send(f"Le résultat du dé est :\n\n{Dé(a)}\n\nRécapitulatif :\n\tjet initial : {bonus[0]}\n\tbonus et malus : {bonus[1:len(bonus)][1:(len(bonus)-1)*3-1]}\n\t{limit}")
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
        if user==None  :
            await ctx.send("Nom attaquant invalide")
        if dest==None  :
            await ctx.send("Nom cible invalide")
        if potion==None :
            await ctx.send("Nom potion invalide")
        return
    verif= type(user)==Joueur
    if verif :
        verif = potion.nom not in user.potion.keys()
    if verif :
        await ctx.send("Vous n'avez pas cette potion dans votre inventaire")
        return
    user.retirerPotion(potion)
    await ctx.send(f"{user.nom} lance {potion.nom} sur {dest.nom}, la potion sera instannément comme bu")
    await ctx.send(coup(user,dest,potion))
    update2()
@client.command()
async def attaque(ctx,dest,arme="poing",user="",critique = False):
    critique = bool(critique)
    if user=="":
        user=ctx.author.id
    user=donneInfo(user)
    dest=donneInfo(dest)
    arme=knowweapon(arme)
    if user==None  or arme==None or dest==None  or (arme not in user.inventaire and arme != poing):
        await ctx.send("Param invalide :")
        if user==None  :
            await ctx.send("Nom attaquant invalide")
        if dest==None :
            await ctx.send("Nom cible invalide")
        if arme==None :
            await ctx.send("Nom arme invalide")
        if arme not in user.inventaire :
            await ctx.send("Vous n'avez pas cet arme (rip bozo)")
        return
    
    
    if critique :
        await ctx.send(f"{user.nom} attaque {dest.nom} avec {arme.nom} (coup critique)")
    else :
        await ctx.send(f"{user.nom} attaque {dest.nom} avec {arme.nom}")
    await ctx.send(coup(user,dest,arme,critique))
    update2()
    
@client.command()
async def prendreHerbe(ctx,dest="",taille = "petite") :
    if dest=="":
        dest=ctx.author.id
    dest= donneInfo(dest)
    if dest==None   :
        await ctx.send("Param invalide : nom de la personne qui prend des herbes tah Bob Marley")
        return
    herbe= HerbeDeSoin
    if taille == "grande" :
        herbe = GrandeHerbeDeSoin
    herbe(dest)
    await ctx.send(f"Vous appliquez les herbes curatives sur {dest.nom}")
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
        if a==None :
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
        if a==None :
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
    user = donneInfoDieuArme(user)
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
async def usePower(ctx,dieu,user=""):
    if user=="":
        user=ctx.author.id
    user = donneInfo(user)
    
    Dieux = [
        "Zeus","Arès" ,"Poséidon","Artémis" ,"Athéna","Aphrodite","Déméter","Dionysos","Hermès","Apollon" ,"Héphaïstos" 
    ]
    if user==None  :
        await ctx.send("Personne invalide")
        return
    if dieu not in Dieux :
        await ctx.send("Dieu invalide")
        return
    await ctx.send(user.usePower(dieu))
    update2()
@client.command()
async def chanter(ctx, chant,chanteur="") :
    reverse = ctx.author.id == eddyid #permet a un ennemi d'etre un rhapsode si je fais les commandes
    chant = chant.lower()
    
    if not reverse :
        user=ctx.author.id if chanteur == "" else chanteur
        user = donneInfo(user)
        if user == None  :
            await ctx.send("Personnage invalide")
            return
        for perso in lstMob + lstJoueur :
            for chant in perso.effect.keys() :
                if user in perso.effect[chant] :
                    perso.effect[chant].remove(user) 
        if type(user.classe) != Rhapsode : 
            await ctx.send("Seuls les Rhapsodes sont doués d'un talent de chant.")
            return
        if chant in ("courage","bouclier") :
            if chant  == "bouclier" and user.niv <3 :
                await ctx.send("Vos talents de Rhapsode ne sont pas encore assez développés pour chanter cette mélodie.")
                return
            for player in lstJoueur :
                player.effect.append(chant)
        if chant in ("dramatique","frayeur") :
            if chant  == "frayeur" and user.niv <4 :
                await ctx.send("Vos talents de Rhapsode ne sont pas encore assez développés pour chanter cette mélodie.")
                return
            for mob in lstMob :
                mob.effect.append(chant)
        if chant == "soin" :
            if user.niv < 2 : 
                await ctx.send("Vos talents de Rhapsode ne sont pas encore assez développés pour chanter cette mélodie.")
                return
            if "soin" in user.usedDay :
                await ctx.send("Vous avez déjà chanter cette poésie aujourd'hui, les gens s'en sont lassés pour aujourd'hui et aucun effet n'a été appliqué.")
                return
            user.usedDay.append(chant)
            for player in lstJoueur :
                nb = player.maxpv//5
                player.soin(nb)
                user.lv(nb)
        if chant == "divin" :
            if user.niv < 5 : 
                await ctx.send("Vos talents de Rhapsode ne sont pas encore assez développés pour chanter cette mélodie.")
                return
            if "divin" in user.usedDay :
                await ctx.send("Vous avez déjà chanter cette poésie aujourd'hui, les gens s'en sont lassés pour aujourd'hui et aucun effet n'a été appliqué.")
                return
            user.usedDay.append(chant)
            for player in lstJoueur :
                nb = player.maxpv//5
                player.soin(nb)
                player.effect.append("courage")
                player.effect.append("bouclier")
            for mob in lstMob :
                mob.effect.append("frayeur")
                mob.effect.append("dramatique")
        particule = {
            "courage" : "du ",
            "soin" : "de ",
            "dramatique" : "",
            "bouclier" : "du ",
            "frayeur" : "de ",
            "divin" : ""
        }
        await ctx.send(f"{user.nom} chante le chant {particule[chant]}{chant}")
    if reverse :
        chanteur = donneInfo(chanteur)
        if chanteur == None  or type(chanteur.classe) != Rhapsode :
            await ctx.send("Personnage invalide (pas Rhapsode ou nom incorrect)")
            return
        for perso in lstMob + lstJoueur :
            for chant in perso.effect.keys() :
                if chanteur in perso.effect[chant] :
                    perso.effect[chant].remove(chanteur)
        if chant in ("courage","bouclier") :
            for player in lstMob :
                player.effect[chant].append(chanteur)
        if chant in ("dramatique","frayeur") :
            for mob in lstJoueur :
                mob.effect[chant].append(chanteur)
        if chant == "soin" :
            for player in lstMob :
                nb = player.maxpv//5
                player.soin(nb)
        if chant == "divin" :
            for player in lstMob :
                nb = player.maxpv//5
                player.soin(nb)
                player.effect["courage"].append(chanteur)
                player.effect[chant].append(chanteur)
                player.effect["bouclier"].append(chanteur)
            for mob in lstJoueur :
                mob.effect[chant].append(chanteur)
                mob.effect["frayeur"].append(chanteur)
                mob.effect["dramatique"].append(chanteur)
        particule = {
            "courage" : "du ",
            "soin" : "de ",
            "dramatique" : "",
            "bouclier" : "du ",
            "frayeur" : "de ",
            "divin" : ""
        }
        await ctx.send(f"{chanteur.nom} chante le chant {particule[chant]}{chant}")
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
    

@client.command()
async def paye(ctx,nb,cible="",user=""):
    if user=="":
        user=ctx.author.id
    user=donneInfo(user)
    c = cible
    cible=donneInfo(cible)
    if user==None or (cible==None and c !="") :
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
            if user== None  :
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
        try :
            nb=int(nb)
        except ValueError :
            ctx.send("pas un nombre")
            return 
        if user=="all":
            for p in lstJoueur:
                if type(p)== Joueur :
                    p.updateFaveurs(dieu,nb)
        else :
            user=donneInfo(user)
            if user== None   :
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
            if user== None   :
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
            if user== None  :
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
            if user== None   :
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
        i.usedCombat = []
        if type(i.classe)==Lutteur and i.niv>=5 :
            i.classe.updateMartiaux(1)
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
async def newDay(ctx):
    for player in lstJoueur + lstMob :
        player.newDay()
    await ctx.send("C'est un nouveau jour qui se lève...")
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
    if perso != None :
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
        nvDanger=1
        indexDebut = 0
        if classe.lower() in "monstre" :
            try :
                nvDanger = int(args[0])
                indexDebut = 1
            except ValueError :
                nvDanger = 1
            except IndexError :
                nvDanger = 1
        payload = {
            "nom" : nom,
            "force" : int(force),
            "habilité" : int(habilite),
            "constitution" : int(constitution),
            "charisme" : int(charisme),
            "foi" : int(foi),
            "classe" : str(getClasse(classe,nvDanger)),
            "inventaire" : donneStuff(args[indexDebut:len(args)]),
            "niv" :  int(niveau),
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
            "force" : int(force),
            "habilité" : int(habilite),
            "constitution" : int(constitution),
            "charisme" : int(charisme),
            "foi" : int(foi),
            "classe" : str(getClasse(classe)),
            "inventaire" : donneStuff(args),
            "niv" :  int(niveau),
            }
        lstMob.append(Boss(payload))
        await ctx.send(nom+ " apparait...")

@client.command()
async def augmentePV(ctx,nom,nb) :
    if ctx.author.id!=eddyid:
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        user = donneInfo(nom)
        if user== None   :
            await ctx.send("Bro even u ? For real man ???")
            return
        user.maxpv+=int(nb)
        user.pv+=int(nb)
        await ctx.send(f'{user.nom} a désormais {user.maxpv} PV max (actuel : {user.pv})')
        update2()
        
@client.command()
async def concocter(ctx,potion,personne,nb=1):
    if ctx.author.id not in (eddyid):
        await ctx.send("Eddy tu n'es pas, te faire foutre tu vas !")
    else :
        perso = donneInfo(personne)
        potion=donnePotion(potion)
        if potion==None :
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
    if user==None  :
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
class Vue(discord.ui.View) :
    @discord.ui.button(label="test",style=discord.ButtonStyle.red,emoji="⚔️")
    async def clickTest(self,interaction,button) :
        await interaction.response.send_message("ntm")
CreationTemporaire = {}
class CreationModal(discord.ui.Modal, title="Création du personnage"): 
    nom = discord.ui.TextInput( label="Nom du personnage", placeholder="Ex : Achille", required=True, max_length=50 )
    async def on_submit(self, interaction: discord.Interaction):
        nom = self.nom.value
        
        personnage = {"nom" : nom}
        CreationTemporaire[interaction.user.id] = personnage
        await interaction.response.send_message(
            "✅ Nom enregistré !\n\n"
            "**Clique sur Continuer pour choisir tes statistiques.**",
            view=ContinuerStatsView(personnage),
            ephemeral=True
        )
class ContinuerStatsView(discord.ui.View):

    def __init__(self,personnage):
        self.personnage = personnage
        super().__init__(timeout=300)

    @discord.ui.button(
        label="Continuer",
        style=discord.ButtonStyle.primary
    )
    async def continuer(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_modal(
            StatModal(self.personnage)
        )
class StatModal(discord.ui.Modal) :
    def __init__(self, personnage, *, timeout = None, custom_id = MISSING):
        self.personnage = personnage
        super().__init__(title="Choix des stats :", timeout=timeout, custom_id=custom_id)
    force = discord.ui.TextInput( label="Force (0-10)", placeholder="Ex : 7", required=True, max_length=2 )
    habilete = discord.ui.TextInput( label="Habileté (0-10)", placeholder="Ex : 5", required=True, max_length=2 )
    constitution = discord.ui.TextInput( label="Constitution (0-10)", placeholder="Ex : 6", required=True, max_length=2 )
    charisme = discord.ui.TextInput( label="Charisme (0-10)", placeholder="Ex : 3", required=True, max_length=2 ) 
    foi = discord.ui.TextInput( label="Foi (0-10)", placeholder="Ex : 4", required=True, max_length=2 )
    async def on_submit(self, interaction: discord.Interaction):
        try:
            force = int(self.force.value) 
            habilete = int(self.habilete.value) 
            constitution = int(self.constitution.value) 
            charisme = int(self.charisme.value)
            foi = int(self.foi.value) 
        except ValueError: 
            await interaction.response.send_message( "❌ Toutes les statistiques doivent être des nombres.", ephemeral=True ) 
            return
        stats = [ force, habilete, constitution, charisme, foi ]
        for stat in stats :
            if stat <0 or stat >10 :
                await interaction.response.send_message( "❌ Chaque statistique doit être comprise entre 0 et 10.", ephemeral=True )
                return
        total = sum(stats) 
        if total != 25:
            await interaction.response.send_message( f"❌ La somme des statistiques doit être exactement 25.\n" f"Tu as actuellement **{total}**.", ephemeral=True ) 
            return
        self.personnage["stats"] = stats 
        CreationTemporaire[interaction.user.id] = self.personnage
        await interaction.response.send_message(f"**Choisis maintenant ta classe :**", view=ClasseView(self.personnage), ephemeral=True )
class ClasseView(discord.ui.View): 
    def __init__(self, personnage): 
        super().__init__(timeout=300) 
        self.add_item(ClasseSelect(personnage))
class ClasseSelect(discord.ui.Select):
    def __init__(self, personnage): 
        self.personnage = personnage
        options = [ discord.SelectOption( label="Sang-mêlé", value="Sang-mêlé", description="""Il est l'enfant d'un dieu, il est béni par ce dernier mais un autre dieu jaloux le punira."""),
                    discord.SelectOption(label="Champion", value="Champion",description="""Un combattant d'arène capable de se battre pour la gloire et divertir."""),
                    discord.SelectOption(label="Hoplite", value="Hoplite",description="""Un guerrier protecteur de première ligne. Il est lourdement équipé protéger ses alliés."""),
                    discord.SelectOption(label="Spadassin", value="Spadassin",description="""Un combattant qui préfère éviter de s'exposer. Il tire avantage des faiblesses de ses adversaires."""),
                    discord.SelectOption(label="Spartiate", value="Spartiate",description="""Un guerrier d'élite prêt à tous pour gagner ses combats, quitte à prendre de grand risque."""),
                    discord.SelectOption(label="Lutteur", value="Lutteur",description="""Un combattant qui utilise la force brute pour vaincre son adversaire avec ses techniques."""),
                    discord.SelectOption(label="Rhapsode", value="Rhapsode",description="""Un poète musicien qui parcourt le monde en but de nouvelles histoires. Ses chants aident son équipe."""),
                    discord.SelectOption(label="Prophète", value="Prophète",description="""Au service d'un dieu, il appelle à sa foi et aux dieux pour résoudre les soucis qu'il fait face."""),
                   ]
        super().__init__( placeholder="Choisis ta classe...", options=options )
    async def callback(self, interaction: discord.Interaction): 
        self.personnage["classe"] = self.values[0]
        classe = self.personnage["classe"]
        CreationTemporaire[interaction.user.id] = self.personnage

        nomClasse = classe
        if classe == "Sang-mêlé": 
            await interaction.response.edit_message( content=( f"**{self.personnage["nom"]}** sera un **Sang-mêlé**.\n\nChoisis maintenant ton **dieu gardien**." ), view=DieuProtecteurView(self.personnage) )
        else : 
            await interaction.response.edit_message( content=( f"**{self.personnage["nom"]}** sera un **{nomClasse}**.\n\nChoisis le dieu que tu vénères." ), view=DieuVenereView(self.personnage) )
class DieuProtecteurSelect(discord.ui.Select):
    def __init__(self, personnage):
        self.personnage = personnage
        self.dieux = ["Zeus","Arès","Poséidon","Artémis","Athéna","Aphrodite","Déméter","Dionysos","Hermès","Apollon","Héphaïstos"]
        options = [discord.SelectOption(label=self.dieux[i], value=self.dieux[i]) for i in range(len(self.dieux))]
        super().__init__( placeholder="Choisis ton dieu gardien.", options=options )
    async def callback(self, interaction: discord.Interaction):
        self.personnage["gardien"] = self.values[0]
        CreationTemporaire[interaction.user.id] = self.personnage
        await interaction.response.edit_message( content=( f"Ton dieu gardien sera **{self.personnage["gardien"]}**.\n\nSélectionne maintenant le dieu qui souhaite ta perte (Donné par ton MJ)." ), view=DieuEnnemiView(self.personnage) )
class DieuProtecteurView(discord.ui.View):
    def __init__(self, personnage): 
        super().__init__(timeout=300) 
        self.add_item(DieuProtecteurSelect(personnage))
class DieuEnnemiSelect(discord.ui.Select): 
    def __init__(self, personnage): 
        self.personnage = personnage 
        self.dieux = ["Zeus","Arès","Poséidon","Artémis","Athéna","Aphrodite","Déméter","Dionysos","Hermès","Apollon","Héphaïstos"]
        self.dieux.remove(self.personnage["gardien"])
        options = [discord.SelectOption(label=self.dieux[i], value=self.dieux[i]) for i in range(len(self.dieux))]
        super().__init__( placeholder="Sélectionne maintenant le dieu qui souhaite ta perte (Donné par ton MJ).", options=options )
    async def callback(self, interaction: discord.Interaction):
        dieu = self.values[0] 
        self.personnage["rival"] = dieu
        CreationTemporaire[interaction.user.id] = self.personnage
        await interaction.response.edit_message( content=( f"Le dieu qui souhaite ta perte est **{dieu}**.\n\nChoisis maintenant le dieu que tu vénères." ), view=DieuVenereView(self.personnage) )
class DieuEnnemiView(discord.ui.View): 
    def __init__(self, personnage): 
        super().__init__(timeout=300) 
        self.add_item(DieuEnnemiSelect(personnage))
class DieuVenereSelect(discord.ui.Select): 
    def __init__(self, personnage): 
        self.personnage = personnage 
        self.dieux = ["Zeus","Arès","Poséidon","Artémis","Athéna","Aphrodite","Déméter","Dionysos","Hermès","Apollon","Héphaïstos"]
        options = [discord.SelectOption(label=self.dieux[i], value=self.dieux[i]) for i in range(len(self.dieux))]
        super().__init__( placeholder="Choisis le dieu que tu vénères.", options=options )
    async def callback(self, interaction: discord.Interaction): 
        self.personnage["dieu_venere"] = self.values[0] 
        CreationTemporaire[interaction.user.id] = self.personnage
        await interaction.response.edit_message( content=( f"Tu vénères **{self.personnage["dieu_venere"]}**.\n\nChoisis maintenant ton armement.\nTu peux choisir **jusqu'à 4 armes**." ), view=ArmesView(self.personnage) )
class DieuVenereView(discord.ui.View): 
    def __init__(self, personnage): 
        super().__init__(timeout=300)
        self.add_item(DieuVenereSelect(personnage))
        
class ArmeSelect(discord.ui.Select): 
    def __init__(self, personnage): 
        self.personnage = personnage
        def uneMain(bool1) :
            if bool1 :
                return "Peut s'utiliser avec une autre arme ou un bouclier." 
            else :
                return "S'utilise à deux mains."
        options = [discord.SelectOption(label=lstArme[i].nom, value=lstArme[i].nom, description=f"{lstArme[i].mini*lstArme[i].nbroll} à {lstArme[i].maxi*lstArme[i].nbroll} dégât(s).\n\n{uneMain(lstArme[i].uneMain)}") for i in range(len(lstArme)) if lstArme[i]!=poing] + [discord.SelectOption(label=bouclier.nom, value=bouclier.nom, description="Un bouclier à une main qui augmente votre défense")]
        super().__init__( placeholder="Choisis tes armes.", options=options, min_values=1, max_values=4 )
    async def callback(self, interaction: discord.Interaction): 
        self.personnage["inventaire"] = self.values
        stuff = []
        match self.personnage["classe"] :
            case "Hoplite":
                stuff = [casque,armureEnAcier]
            case "Lutteur" :
                stuff = [armureDeCuir]
            case "Prophète" :
                stuff = [tunique]
            case "Rhapsode" :
                stuff = [tunique]
            case "Sang-mêlé" :
                stuff = [armureDeBronze]
            case "Spadassin" :
                stuff = [armureDeCuir,casque]
            case "Spartiate" :
                stuff = [casque, armuredeSpartiate]
            case "Champion" :
                stuff = [casque, armureDeFer]
        stuff = [armure.nom for armure in stuff]
        self.personnage["inventaire"] += stuff
        dieu = {
            "Zeus": 50,
            "Poséidon": 50,
            "Artémis": 50,
            "Arès": 50,
            "Athéna": 50,
            "Aphrodite": 50,
            "Dionysos": 50,
            "Déméter": 50,
            "Hermès": 50,
            "Apollon": 50,
            "Héphaïstos": 50
          }
        dieu[self.personnage["dieu_venere"]] += 5
        if self.personnage["classe"] == "Prophète" :
            dieu[self.personnage["dieu_venere"]] += 10
        if self.personnage["classe"] == "Sang-mêlé" :
            dieu[self.personnage["rival"]] -= 20
            dieu[self.personnage["gardien"]] += 20
        classe = self.personnage["classe"] 
        if classe == "Sang-mêlé" :
            classe += f" / {self.personnage['gardien']} / {self.personnage['rival']}"
        payload = {
            "nom": self.personnage["nom"],
            "force" : self.personnage["stats"][0],
            "habilité" : self.personnage["stats"][1],
            "constitution" : self.personnage["stats"][2],
            "charisme" : self.personnage["stats"][3],
            "foi" : self.personnage["stats"][4],
            "classe": classe,
            "niv": 1,
            "xp": 0,
            "monnaie": 0,
            "point": 0,
            "inventaire": donneStuff(self.personnage["inventaire"]),
            "dieux": dieu,
            "potion": {},
            "joueurid": interaction.user.id
        }
        
        del CreationTemporaire[interaction.user.id] 
        nouveauJoueur = Joueur(payload)
        lstId[payload["joueurid"]] = nouveauJoueur
        lstJoueur.append(nouveauJoueur)
        await interaction.response.edit_message( content=( f"### Personnage terminé !\n{nouveauJoueur}"), view=None )
class ArmesView(discord.ui.View):
    def __init__(self, personnage): 
        super().__init__(timeout=300) 
        self.add_item(ArmeSelect(personnage))
@client.tree.command(description="Commencez votre création de personnage")
async def start(interaction : discord.Interaction) :
    await interaction.response.send_modal(CreationModal())
idserver=1344769143425073193
@client.tree.command(description="lancer des dés dans le format 1d20 (1 dé à 20 faces) ou par exemple 3d6 ")
async def r(interaction : discord.Interaction,format : str ="1d20"):
    if  "d" not in format :
        await interaction.response.send_message("Format invalide (format attendu NdM : exemple 1d6, 3d8, 12d14)")
        return
    Dice= format.split("d")
    nbDice = 0
    nbFace = 0
    try :
        nbDice = int(Dice[0])
        nbFace = int(Dice[1])
    except ValueError :
        await interaction.response.send_message("Format invalide (format attendu NdM : exemple 1d6, 3d8, 12d14)")
        return
    except IndexError :
        await interaction.response.send_message("Format invalide (format attendu NdM : exemple 1d6, 3d8, 12d14)")
        return
    result = 0
    lstResult = []
    for i in range(nbDice) :
        nb = randint(1,nbFace)
        lstResult.append(nb)
        result += nb
    await interaction.response.send_message(f"Résultat du lancé de dé(s) :\n\trésultat : {result}\n\ttous les dés : {lstResult}")

async def autocomplete_stat(
    interaction: discord.Interaction,
    current: str
) :
    choix = []
    stats = ["force","habilité","constitution","charisme","foi"]
    for stat in stats :
        if normalize(current.lower()) in normalize(stat.lower()) :
            choix.append(
                app_commands.Choice(
                    name=stat,
                    value=stat
                )
            )
    return choix[:25]
async def autocomplete_cible(
    interaction: discord.Interaction,
    current: str
):
    choix = []
    for member in interaction.guild.members:
        if current.lower() in member.display_name.lower() and member.id in lstId.keys():
            choix.append(
                app_commands.Choice(
                    name=f"{member.display_name} - {lstId[member.id].nom}",
                    value=f"{member.id}"
                )
            )

    for mob in lstMob:
        if current.lower() in mob.nom.lower():
            choix.append(
                app_commands.Choice(
                    name=mob.nom,
                    value=mob.nom
                )
            )
    return choix[:25]
async def autocomplete_tout(
    interaction: discord.Interaction,
    current: str
):
    choix = []
    for member in interaction.guild.members:
        if current.lower() in member.display_name.lower() and member.id in lstId.keys():
            choix.append(
                app_commands.Choice(
                    name=f"{member.display_name} - {lstId[member.id].nom}",
                    value=f"{member.id}"
                )
            )

    for mob in lstMob:
        if current.lower() in mob.nom.lower():
            choix.append(
                app_commands.Choice(
                    name=mob.nom,
                    value=mob.nom
                )
            )
    Dieux = [
                "Zeus","Arès" ,"Poséidon","Artémis" ,"Athéna","Aphrodite","Déméter","Dionysos","Hermès","Apollon" ,"Héphaïstos" 
            ]
    for dieu in Dieux :
        if normalize(current.lower()) in normalize(dieu.lower()) :
            choix.append(
                        app_commands.Choice(
                            name=dieu,
                            value=dieu
                        )
                    )
    for arme in lstArme :
        if current.lower() in arme.nom.lower():
            choix.append(
                app_commands.Choice(
                    name=f"{arme.nom}",
                    value=f"{arme.nom}"
                )
            )
    return choix[:25]
async def autocomplete_arme(
    interaction: discord.Interaction,
    current: str
):
    user = donneInfo(interaction.user.id)
    if ( user == None ) and interaction.user.id != eddyid : 
        return []
    lst = lstArme.copy()
    if interaction.user.id == eddyid or (type(user.classe) == Hoplite and user.niv>= 2 and bouclier in user.inventaire)  :
        lst.append(bouclierAsWeapon)
    choix = []
    for arme in lst :
        if (interaction.user.id == eddyid or current.lower() in arme.nom.lower()) : #and arme in user.inventaire :
            choix.append(
                app_commands.Choice(
                    name=f"{arme.nom}",
                    value=f"{arme.nom}"
                )
            )
    return choix[:25]
async def autocomplete_herbe(
    interaction: discord.Interaction,
    current: str
):

    choix = []
    if current.lower() in "petite" :
            choix.append(
                app_commands.Choice(
                    name=f"petite",
                    value=f"petite"
                )
            )
    if current.lower() in "grande" :
                choix.append(
                    app_commands.Choice(
                        name=f"grande",
                        value=f"grande"
                    )
                )
    return choix[:25]
async def autocomplete_dieu(
    interaction: discord.Interaction,
    current: str
):
    Dieux = [
            "Zeus","Arès" ,"Poséidon","Artémis" ,"Athéna","Aphrodite","Déméter","Dionysos","Hermès","Apollon" ,"Héphaïstos" 
        ]
    choix = []
    for dieu in Dieux :
        if normalize(current.lower()) in normalize(dieu.lower()) :
            choix.append(
                        app_commands.Choice(
                            name=dieu,
                            value=dieu
                        )
                    )
    return choix[:25]
async def autocomplete_chant(
    interaction: discord.Interaction,
    current: str
):
    chants = ["bouclier","frayeur","soin","divin","dramatique","courage"]
    choix = []
    for chant in chants :
        if normalize(current.lower()) in normalize(chant.lower()) :
            choix.append(
                        app_commands.Choice(
                            name=chant,
                            value=chant
                        )
                    )
    return choix[:25]
@client.tree.command(description="lancer 1 dé 20 avec un personnage et une statistique")
@app_commands.autocomplete(nom=autocomplete_cible,stat=autocomplete_stat)
async def roll(interaction : discord.Interaction, stat :str ="habilité",nom : str = ""):
    if nom=="":
        nom=interaction.user.id
    try :
        stat=getStat(stat)
        a,bonus,limit =R(donneInfo(nom), stat)
        if a!=None:
            await interaction.response.send_message("https://tenor.com/view/angry-birds-gif-12007401521632546156")
            await interaction.followup.send(f"Le résultat du dé est :\n\n{Dé(a)}\n\nRécapitulatif :\n\tjet initial : {bonus[0]}\n\tbonus et malus : {str(bonus[1:len(bonus)])[1:(len(bonus)-1)*3-1]}\n\n{limit}")
        else :
            await interaction.response.send_message("Merci de corriger votre commande")
            await interaction.followup.send(f'{nom},{stat}')
    except ValueError :
        await interaction.response.send_message("Stat invalide")
@client.tree.command(description="passer un level pour augmenter une stat")
async def level(interaction : discord.Interaction, stat :str ):
    user=interaction.user.id
    user = donneInfo(user)
    if user==None :
        await interaction.response.send_message("Param invalide : Nom personnage")
    else :
        try :
            a = getStat(stat)
            await interaction.response.send_message(user.augmentStat(a))
            update2()
        except ValueError:
            await interaction.response.send_message("Stat invalide")
            
@client.tree.command(description="lancer une attaque sur un adversaire")
@app_commands.autocomplete(cible=autocomplete_cible,user=autocomplete_cible,arme=autocomplete_arme)
async def attaque(interaction : discord.Interaction,cible : str ,arme : str ="poing",user : str ="",critique : bool = False):
    critique = bool(critique)
    if user=="":
        user=interaction.user.id
    user=donneInfo(user)
    dest=donneInfo(cible)
    arme=knowweapon(arme)
    if user==None or arme==None or dest==None or (arme not in user.inventaire and arme != poing):
        await interaction.response.send_message("Param invalide :")
        if user==None  :
            await interaction.followup.send("Nom attaquant invalide")
        if dest==None  :
            await interaction.followup.send("Nom cible invalide")
        if arme==None :
            await interaction.followup.send("Nom arme invalide")
        if arme not in user.inventaire :
            await interaction.followup.send("Vous n'avez pas cet arme (rip bozo)")
        return
    
    
    if critique : 
        await interaction.response.send_message(f"{user.nom} attaque {dest.nom} avec {arme.nom} (coup critique)")
    else :
        await interaction.response.send_message(f"{user.nom} attaque {dest.nom} avec {arme.nom}")
    await interaction.followup.send(coup(user,dest,arme,critique))
    update2()
@client.tree.command(description="Soignez une personne en lui donnant une herbe de votre inventaire")
@app_commands.autocomplete(dest=autocomplete_cible,taille=autocomplete_herbe)
async def prendreherbe(interaction : discord.Interaction,dest : str ="",taille : str  = "petite") :
    if dest=="":
        dest=interaction.user.id
    dest= donneInfo(dest)
    if dest==None :
        await interaction.response.send_message("Param invalide : nom de la personne qui prend des herbes tah Bob Marley")
        return
    herbe= HerbeDeSoin
    if taille == "grande" :
        herbe = GrandeHerbeDeSoin
    herbe(dest)
    await interaction.response.send_message(f"Vous appliquez les herbes curatives sur {dest.nom}")
    update2()
@client.tree.command(description="Utilisez le pouvoir d'un dieu qui permet d'en avoir un.")
@app_commands.autocomplete(user=autocomplete_cible,dieu=autocomplete_dieu)
async def usepower(interaction : discord.Interaction,dieu: str,user : str=""):
    if user=="":
        user= interaction.user.id
    user = donneInfo(user)
    
    Dieux = [
        "Zeus","Arès" ,"Poséidon","Artémis" ,"Athéna","Aphrodite","Déméter","Dionysos","Hermès","Apollon" ,"Héphaïstos" 
    ]
    if user==None :
        await interaction.response.send_message("Personne invalide")
        return
    if dieu not in Dieux :
        await interaction.response.send_message("Dieu invalide")
        return
    await interaction.response.send_message(user.usePower(dieu))
    update2()
@client.tree.command(description="Retrouvez les informations sur le joueur ou l'ennemi de votre choix")
@app_commands.autocomplete(nom=autocomplete_tout)
async def info(interaction : discord.Interaction,nom : str=""):
    if nom=="":
        nom=interaction.user.id
    user = donneInfoDieuArme(nom)
    if user==None:
        await interaction.response.send_message("Personne invalide")
        return
    await interaction.response.send_message(user)
@client.tree.command(description="Regardez un inventaire")
@app_commands.autocomplete(cible=autocomplete_cible)
async def inventaire(interaction : discord.Interaction,cible : str="") :
    user = cible
    if user=="":
        user=interaction.user.id
    user = donneInfo(user)
    if user==None  :
        await interaction.response.send_message("Personne invalide")
        return
    await interaction.response.send_message(user.monStuff())
    
@client.tree.command(description="Regardez un inventaire")
@app_commands.autocomplete(cible=autocomplete_cible)
async def faveurs(interaction : discord.Interaction,cible : str="") :
    user = cible
    if user=="":
        user=interaction.user.id
    user = donneInfo(user)
    if user==None  :
        await interaction.response.send_message("Personne invalide")
        return
    await interaction.response.send_message(user.getDieux())
    
@client.tree.command(description="Découvrez les commandes")
async def aide(interaction : discord.Interaction,commande : str=""):    
    msg = bothelp(commande)
    if len(msg)<=2000:
        await interaction.response.send_message(msg)
    else :
        nb = len(msg)
        for i in range(0,nb,1500):
            if i ==0 :
                await interaction.response.send_message(textDiscord(msg[i:i+1500]))
            else :
                await interaction.followup.send(textDiscord(msg[i:i+1500]))
                
@client.tree.command(description="Utilisez vos talents de rhapsode.")
@app_commands.autocomplete(chanteur=autocomplete_cible,chant=autocomplete_chant)
async def chanter(interaction : discord.Interaction, chant : str,chanteur: str ="") :
    reverse = interaction.user.id == eddyid #permet a un ennemi d'etre un rhapsode si je fais les commandes
    chant = chant.lower()
    
    if not reverse :
        user=interaction.user.id if chanteur == "" else chanteur
        user = donneInfo(user)
        for perso in lstMob + lstJoueur :
            for chant in perso.effect.keys() :
                if user.nom in perso.effect[chant] :
                    perso.effect[chant].remove(user.nom)
        if type(user) != Perso or type(user) == Joueur : 
                    await interaction.response.send_message("Seuls les Rhapsodes sont doués d'un talent de chant.")
                    return 
        if type(user.classe) != Rhapsode : 
            await interaction.response.send_message("Seuls les Rhapsodes sont doués d'un talent de chant.")
            return
        if chant in ("courage","bouclier") :
            if chant  == "bouclier" and user.niv <3 :
                await interaction.response.send_message("Vos talents de Rhapsode ne sont pas encore assez développés pour chanter cette mélodie.")
                return
            for player in lstJoueur :
                player.effect.append(chant)
        if chant in ("dramatique","frayeur") :
            if chant  == "frayeur" and user.niv <4 :
                await interaction.response.send_message("Vos talents de Rhapsode ne sont pas encore assez développés pour chanter cette mélodie.")
                return
            for mob in lstMob :
                mob.effect[chant].append(user.nom)
        if chant == "soin" :
            if user.niv < 2 : 
                await interaction.response.send_message("Vos talents de Rhapsode ne sont pas encore assez développés pour chanter cette mélodie.")
                return
            if "soin" in user.usedDay :
                await interaction.response.send_message("Vous avez déjà chanter cette poésie aujourd'hui, les gens s'en sont lassés pour aujourd'hui et aucun effet n'a été appliqué.")
                return
            user.usedDay.append(chant)
            for player in lstJoueur :
                nb = player.maxpv//5
                player.soin(nb)
        if chant == "divin" :
            if user.niv < 5 : 
                await interaction.response.send_message("Vos talents de Rhapsode ne sont pas encore assez développés pour chanter cette mélodie.")
                return
            if "divin" in user.usedDay :
                await interaction.response.send_message("Vous avez déjà chanter cette poésie aujourd'hui, les gens s'en sont lassés pour aujourd'hui et aucun effet n'a été appliqué.")
                return
            user.usedDay.append(chant)
            for player in lstJoueur :
                nb = player.maxpv//5
                player.soin(nb)
                player.effect["courage"].append(user.nom)
                player.effect["bouclier"].append(user.nom)
            for mob in lstMob :
                mob.effect["frayeur"].append(user.nom)
                mob.effect["dramatique"].append(user.nom)
        particule = {
            "courage" : "du ",
            "soin" : "de ",
            "dramatique" : "",
            "bouclier" : "du ",
            "frayeur" : "de ",
            "divin" : ""
        }
        await interaction.response.send_message(f"{user.nom} chante le chant {particule[chant]}{chant}")
    if reverse :
        chanteur = donneInfo(chanteur)
        if chanteur == None   or type(chanteur.classe) != Rhapsode :
            await interaction.response.send_message("Personnage invalide (pas Rhapsode ou nom incorrect)")
            return
        for perso in lstMob + lstJoueur :
            for chant in perso.effect.keys() :
                if chanteur in perso.effect[chant] :
                    perso.effect[chant].remove(chanteur)
        if chant in ("courage","bouclier") :
            for player in lstMob :
                player.effect[chant].append(chanteur)
        if chant in ("dramatique","frayeur") :
            for mob in lstJoueur :
                mob.effect[chant].append(chanteur)
        if chant == "soin" :
            for player in lstMob :
                nb = player.maxpv//5
                player.soin(nb)
        if chant == "divin" :
            for player in lstMob :
                nb = player.maxpv//5
                player.soin(nb)
                player.effect["courage"].append(chanteur)
                player.effect[chant].append(chanteur)
                player.effect["bouclier"].append(chanteur)
            for mob in lstJoueur :
                mob.effect[chant].append(chanteur)
                mob.effect["frayeur"].append(chanteur)
                mob.effect["dramatique"].append(chanteur)
        particule = {
            "courage" : "du ",
            "soin" : "de ",
            "dramatique" : "",
            "bouclier" : "du ",
            "frayeur" : "de ",
            "divin" : ""
        }
        await interaction.response.send_message(f"{chanteur.nom} chante le chant {particule[chant]}{chant}")
@client.command()
async def armes(ctx) :
    a = "Liste des armes \n"
    for arme in lstArme :
        a+=str(arme)+"\n"
    await ctx.send(a)
@client.tree.command(description="Obtenez les infos sur toutes les armes.")
async def armes(interaction : discord.Interaction) :
    a = "Liste des armes \n"
    for arme in lstArme :
        a+=str(arme)+"\n"
    await interaction.response.send_message(a)
@client.event
async def on_ready():
    guild = discord.Object(id=idserver)

    client.tree.copy_global_to(guild=guild)
    await client.tree.sync()
    print("ready")
client.run(token)
update2()
print("au revoir")
