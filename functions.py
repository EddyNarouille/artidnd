import codecs
from random import randint
import unicodedata 
import json
from os import listdir
from classes.classeCombat.monstre import Monstre
from data import *
from effetDieux import *



def attaqueFurtive(arme: Arme,self : Perso,qql : Perso,critique,coef=1) :
    a=2+randint(1,10)
    oneShot = qql.pv == self.maxpv
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
        a = int(arme.roll(self.force)*coef)
    if type(arme)==ArmeLegendaire:
        a = int(arme.roll(self.force,self.getStatValue(arme.bonus))*coef)
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
def execution(cible) :
    cible.subitdegat(cible.maxpv,"")

def donneStuff(inventaire) :
    newInventory = []
    for item in inventaire :
        for stuff in lstArme+lstArmure : 
            if stuff.nom==item :
                newInventory.append(stuff)
    return newInventory
def recreate() :
    path= "PlayerData/"
    files = listdir(path)
    for file in files :
        data = open(path+file,"r")
        payload = json.load(data)
        payload["inventaire"] = donneStuff(payload["inventaire"])
        nvJoueur = Joueur(payload)
        lstJoueur.append(nvJoueur)
        lstId[payload["joueurid"]] = nvJoueur
recreate()
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
    try : 
        if type(nom) == str and nom[0:2] == "<@":
            nom2 = int(nom[2:len(nom)-1])
            for id in lstId.keys() :
                if nom2==id:
                    return lstId[id]
    finally : 
        try :
            nom2 = int(nom)
            for id in lstId.keys() :
                if nom2==id:
                    return lstId[id]
        except ValueError :
            for id in lstId.keys() :
                if nom==id:
                    return lstId[id]
            for mob in lstJoueur+lstMob:
                if mob.nom==nom:
                    return mob
    return None
def donneInfoDieuArme(nom):
    Dieux = [
                "Zeus","Arès" ,"Poséidon","Artémis" ,"Athéna","Aphrodite","Déméter","Dionysos","Hermès","Apollon" ,"Héphaïstos" 
            ]
    if nom in Dieux :
        explicationDieu = {
            "Zeus" : f"""# Zeus
Dieu du ciel, de la foudre et roi de l'Olympe, il est le dieu le plus craint et le plus vénéré.

**Bonus et malus :**
Faveur : {Faveurs["Zeus"]}
Bénédiction : {Benedictions["Zeus"]}
Colère : {Coleres["Zeus"]}
Malédiction : {Maledictions["Zeus"]}

**Comment obtenir/perdre des points faveurs de Zeus :**
Gain : 
Respecter et obéir à son dirigeant +
Être brave  ++
Respecter les aigles +
Amener la paix ++

Perte :
Tenter de surpasser les dieux ---
Être un Titan ou apprécié un Titan --
Obtenir des gains de faveurs d'Ares --
Mentir ou tromper une personne -
""",
            "Arès" : f"""# Arès
Dieu de la guerre et du combat sanglat, Arès est craint et parfois détesté.

**Bonus et malus :**
Faveur : {Faveurs["Arès"]}
Bénédiction : {Benedictions["Arès"]}
Colère : {Coleres["Arès"]}
Malédiction : {Maledictions["Arès"]} 

**Comment obtenir/perdre des points faveurs d'Arès :**
Gain :
Battre un ennemi. +
Affronter plusieurs personnes à la fois. ++
Battre un adversaire plus fort que soi. +++

Perte :
Fuir un combat. ---
Laisser un adversaire fuir.  --
Tomber au combat. -
""" ,
            "Poséidon" : f"""# Poséidon
Dieu de la mer et frère de Zeus, il est un dieu respecté et apprécié, bien qu'il puisse être rancunier.

**Bonus et malus :**
Faveur : {Faveurs["Poséidon"]}
Bénédiction : {Benedictions["Poséidon"]}
Colère : {Coleres["Poséidon"]}
Malédiction : {Maledictions["Poséidon"]}

**Comment obtenir/perdre des points faveurs de Poséidon :**
Gain : 
Sauver/prendre soin d'un cheval. +
Le prier avant d'aller en mer. ++
Pêcher sans le faire en masse. +
Respecter les marins. + 

Perte : 
Humilier un de ses nombreux enfants. ---
Partir en mer sans le prier. -
Souiller l'eau. --
Détruire ou piller un bateau marchand. -
            """,
            "Artémis" : f"""# Artémis
Déesse de la chasse, des animaux et de la forêt.

**Bonus et malus :**
Faveur : {Faveurs["Artémis"]}
Bénédiction : {Benedictions["Artémis"]}
Colère : {Coleres["Artémis"]}
Malédiction : {Maledictions["Artémis"]}

**Comment obtenir/perdre des points faveurs d'Artémis :**
Gain :
Tirer a l'arc et faire un critique. +
Suivre discrètement une personne. ++
Sauvez un animale. +++
Chasser avec parcimonie. +

Perte : 
Tuez trop d'animaux ou un animal dans une zone sacrée. --
Être violent envers une mère. --
Être violent envers une femme enceinte. ----
Être violent envers un enfant. --
Faire l'amour. -
""",
            "Athéna" : f"""# Athéna
Déesse de la sagesse et de la justice, elle est également une grande guerrière et stratège.

**Bonus et malus :**
Faveur : {Faveurs["Athéna"]}
Bénédiction : {Benedictions["Athéna"]}
Colère : {Coleres["Athéna"]}
Malédiction : {Maledictions["Athéna"]}

**Comment obtenir/perdre des points faveurs d'Athéna :**
Gain :
Encaisser un coup pour quelqu'un. +
Protéger des gens et les sauver. ++
Laisser un adversaire se rendre. ++
Affronter des criminels. ++

Perte :
Tuer un innocent. ---
Achever une personne qui se rend. --
Tuer une personne dans le dos, ou qui est désarmé. --
Laisser un camarade souffrir. -
            """,
            "Aphrodite" : f"""# Aphrodite
Déesse de la beauté, de la séduction, de l'amour et de la fertilité (humaine).

**Bonus et malus :**
Faveur : {Faveurs["Aphrodite"]}
Bénédiction : {Benedictions["Aphrodite"]}
Colère : {Coleres["Aphrodite"]}
Malédiction : {Maledictions["Aphrodite"]}
            
**Comment obtenir/perdre des points faveurs d'Aphrodite :**
Gain :
Séduire quelqu'un. +
Finir au lit avec quelqu'un. ++

Perte :
Dire d'une femme qu'elle est plus belle qu'Aphrodite. -----
Payer pour du sexe. -
""",
            "Déméter" : f"""# Déméter
Déesse des saisons, de la météo, de l'agriculture et de la fertilité des terres.

**Bonus et malus :**
Faveur : {Faveurs["Déméter"]}
Bénédiction : {Benedictions["Déméter"]}
Colère : {Coleres["Déméter"]}
Malédiction : {Maledictions["Déméter"]}

**Comment obtenir/perdre des points faveurs de Déméter :**
Gain :
Respecter la nourriture. +
Prendre soin de la nature. ++
Offrir de la nourriture aux plus affamés. ++

Perte : 
Détruire des champs. ---
Empoisonner la nourriture. --
Ne pas finir son assiette. -
            """,
            "Dionysos" : f"""# Dionysos
Dieu du vin et de la fête, il est toujours de bonne humeur et préfère s'éloigner des soucis.

**Bonus et malus : **
Faveur : {Faveurs["Dionysos"]}
Bénédiction : {Benedictions["Dionysos"]}
Colère : {Coleres["Dionysos"]}
Malédiction : {Maledictions["Dionysos"]}

**Comment obtenir/perdre des points faveurs de Dionysos :**
Boire du vin. +
Faire la fête. ++
Jouer de la musique. +++

Perte :
Tomber dans un coma éthylique. -
Refuser de faire la fête ou de boire un verre de vin offert. --
Troubler une fête. ---
            """,
            "Hermès" : f"""# Hermès
Dieu des commerçants, de la vitesse et messager des dieux.

**Bonus et malus : **
Faveur : {Faveurs["Hermès"]}
Bénédiction : {Benedictions["Hermès"]}
Colère : {Coleres["Hermès"]}
Malédiction : {Maledictions["Hermès"]} 

**Comment obtenir/perdre des points faveurs de Hermès :**
Gain :
Commercer. +
Livrer un message. +
Respecter les liens familiaux et les rapports de puissance. +
Voyager. +

Perte :
Voler un commerçant. ---
Ne pas montrer d'empathie. --
            """,
            "Apollon" : f"""# Apollon
Dieu de la lumière et de la poésie et la musique.

**Bonus et malus :**
Faveur : {Faveurs["Apollon"]}
Bénédiction : {Benedictions["Apollon"]}
Colère : {Coleres["Apollon"]}
Malédiction : {Maledictions["Apollon"]}

**Comment obtenir/perdre des points faveurs d'Apollon :**
Gain :
Protéger des enfants. ++
Dire la vérité. +
Lire des livres. +
Se faire le plus beau possible. ++

Perte :
Être fourbe. --
Être arrogant. ---
            """,
            "Héphaïstos" : f"""# Héphaïstos
Dieu de l'artisanat, de la forge et du feu.

**Bonus et malus :**
Faveur : {Faveurs["Héphaïstos"]}
Bénédiction : {Benedictions["Héphaïstos"]}
Colère : {Coleres["Héphaïstos"]}
Malédiction : {Maledictions["Héphaïstos"]}

**Comment obtenir/perdre des points faveurs de Héphaïstos :**
Gain : 
Forger/Améliorer une arme/armure +++
Acheter des armures et armes. +
Allumer un feu. +

Perte : 
Ne pas prendre soin d'une arme et armure. ---
Ne pas respecter les forgerons. --
Voler de l'équipement. --
            """     
        }
        return explicationDieu[nom]
    if type(nom) == str :
        for arme in lstArme :
            if nom.lower()== arme.nom :
                return arme
    try : 
        if type(nom) == str and nom[0:2] == "<@":
            nom2 = int(nom[2:len(nom)-1])
            for id in lstId.keys() :
                if nom2==id:
                    return lstId[id]
    finally : 
        try :
            nom2 = int(nom)
            for id in lstId.keys() :
                if nom2==id:
                    return lstId[id]
        except ValueError :
            for id in lstId.keys() :
                if nom==id:
                    return lstId[id]
            for mob in lstJoueur+lstMob:
                if mob.nom==nom:
                    return mob
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
def knowweapon(name):
    for arme in lstArme+lstArmeMob+lstArmeLegendaire:
        if arme.nom==name:
            return arme
    return poing
def forger(user) :
    user.inventaire.append(marteauDeFeuHephaistos)
def update2():
    file = "ennemyData/ennemy-PV"
    f = open(file,"w",encoding="utf-8")
    f.write("")
    f.close()
    upd = []
    for i in lstJoueur:
        upd.append(i)
    for player in upd:
        if player == None :
            continue
        player.toJSON()
        
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
def coup(user,dest,arme,critique):
    if type(arme) == "A CHANGER ICI POUR SORTS ET CHANTS" and arme.heal:
        a =0
        if "Dionysos" not in dest.coleres :
            a=user.heal(dest,randint(arme.mini,arme.maxi))
            user.lv(a)
        return f'{user} a soigné {dest} de {a} pv'
    else :
        a= user.attaque(dest,arme,critique=critique)
        b=int(a/2)
    if type(dest)!=Joueur :
        user.lv(a)
        for player in lstJoueur : 
            if player != user :
                player.lv(b)
    if dest.pv<=0:
        dest.pv=0
        user.lv(5)
        if dest in lstMob :
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
    if nom_normalise not in list(statnom.keys()):
        raise ValueError()
    

    return statnom[nom_normalise]
def getClasse(nom,nvDanger=1):
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
        "monstre" : Monstre(nivDanger=nvDanger),
    }

    return raceClasse[nom_normalise]