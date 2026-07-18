import codecs
from random import randint
import unicodedata 
import json
from os import listdir
from data import *
    



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
    for arme in lstArme:
        if arme.nom==name:
            return arme
    return poing
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
def getClasse(nom):
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