from pathlib import Path
import sys

parent_dir = str(Path(__file__).resolve().parent.parent)

if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from functions import *

joueur1= Joueur({
    "point" : 0,
    "xp" : 0,
    "potion" : {},
    "monnaie" : 0,
    "joueurid" : -1,
    "nom" : "MonJoueur",
    "force" : 4,
    "habilité" : 3,
    "constitution" : 6,
    "charisme" : 3,
    "foi" : 5,
    "inventaire" : [lance],
    "classe" : "Pharmakeutês",
    "niv" : 1
})
mob1 = Creature({
    "point" : 0,
    "xp" : 0,
    "potion" : {},
    "monnaie" : 0,
    "joueurid" : -1,
    "nom" : "MonMob",
    "force" : 4,
    "habilité" : 3,
    "constitution" : 6,
    "charisme" : 3,
    "foi" : 5,
    "inventaire" : [lance],
    "classe" : "Monstre|2|1",
    "niv" : 1
})
boss1 = Boss({
    "point" : 0,
    "xp" : 0,
    "potion" : {},
    "monnaie" : 0,
    "joueurid" : -1,
    "nom" : "MonBoss",
    "force" : 4,
    "habilité" : 3,
    "constitution" : 6,
    "charisme" : 3,
    "foi" : 5,
    "inventaire" : [lance],
    "classe" : "Monstre|3|1",
    "niv" : 1
})
def testType() :
    for armure in lstArmure :
        assert type(armure) == Armure
    for arme in lstArme + lstArmeLegendaire + lstArmeMob:
        assert (type(arme)== Arme or type(arme) == ArmeLegendaire)
    for joueur in lstJoueur : 
        assert type(joueur) == Joueur
    for id in lstId.keys() :
        assert type(id)==int
    for idJoueur in lstId.values() :
        assert type(idJoueur) == Joueur
def testPv() :
    assert mob1.maxpv > joueur1.maxpv
    assert boss1.maxpv > mob1.maxpv
    pvAvantAttaque = mob1.pv
    joueur1.attaque(mob1,lance)
    assert pvAvantAttaque>mob1.pv
def testInitClasse() :
    joueur2= Joueur({
    "point" : 0,
    "xp" : 0,
    "potion" : {},
    "monnaie" : 0,
    "joueurid" : -1,
    "nom" : "MonJoueur",
    "force" : 4,
    "habilité" : 3,
    "constitution" : 6,
    "charisme" : 3,
    "foi" : 5,
    "inventaire" : [lance],
    "classe" : "Pharmakeutês",
    "niv" : 1
    })
    assert type(joueur2.classe)==Pharmakeutes
    assert joueur2.classe.user==joueur2
    joueur2= Joueur({
    "point" : 0,
    "xp" : 0,
    "potion" : {},
    "monnaie" : 0,
    "joueurid" : -1,
    "nom" : "MonJoueur",
    "force" : 4,
    "habilité" : 3,
    "constitution" : 6,
    "charisme" : 3,
    "foi" : 5,
    "inventaire" : [lance],
    "classe" : "Hoplite",
    "niv" : 1
    })
    assert type(joueur2.classe)==Hoplite
    joueur2= Joueur({
    "point" : 0,
    "xp" : 0,
    "potion" : {},
    "monnaie" : 0,
    "joueurid" : -1,
    "nom" : "MonJoueur",
    "force" : 4,
    "habilité" : 3,
    "constitution" : 6,
    "charisme" : 3,
    "foi" : 5,
    "inventaire" : [lance],
    "classe" : "Lutteur",
    "niv" : 1
    })
    assert type(joueur2.classe)==Lutteur
    joueur2= Joueur({
    "point" : 0,
    "xp" : 0,
    "potion" : {},
    "monnaie" : 0,
    "joueurid" : -1,
    "nom" : "MonJoueur",
    "force" : 4,
    "habilité" : 3,
    "constitution" : 6,
    "charisme" : 3,
    "foi" : 5,
    "inventaire" : [lance],
    "classe" : "Monstre|2|1",
    "niv" : 1
    })
    assert type(joueur2.classe)==Monstre
    assert joueur2.classe.nivDanger==2
    assert joueur2.classe.toUpdate==False
def testInitArmure() :
    stuff = []
    def getArmure(stuff: Armure) :
        return stuff.armure
    for armure in lstArmure :
        stuff.append(armure)
        joueur2= Joueur({
            "point" : 0,
            "xp" : 0,
            "potion" : {},
            "monnaie" : 0,
            "joueurid" : -1,
            "nom" : "MonJoueur",
            "force" : 4,
            "habilité" : 3,
            "constitution" : 6,
            "charisme" : 3,
            "foi" : 5,
            "inventaire" : [lance]+stuff,
            "classe" : "Monstre|2|1",
            "niv" : 1
            })
        
        assert joueur2.armure==10+sum(list(map(getArmure,stuff)))
    joueur2.updateFaveurs("Héphaïstos",-50)
    assert joueur2.armure==10+stuff[0].armure
    joueur2.updateFaveurs("Athéna",-50)
    assert joueur2.armure==10+stuff[0].armure-2
    joueur2.updateFaveurs("Héphaïstos",50,True)
    assert joueur2.armure==10+sum(list(map(getArmure,stuff)))-2
    joueur2.updateFaveurs("Athéna",100,True)
    
    
    
testType()    
testPv()
testInitClasse()
testInitArmure()