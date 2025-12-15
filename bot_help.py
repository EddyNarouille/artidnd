

def bothelp(commande="all"):
    if commande=="aide" :
        return"""```Voici comment utiliser la commande aide : \n un '*' après un nom de variable signifie qu'il est optionel\n !aide commande * : permet de renvoyé l'aide sur une commande, si rien n'est précisé, toutes les commandes s'affichent```"""
    elif commande=="roll":
        return "```Voici comment utiliser la commande roll :\n un '*' après un nom de variable signifie qu'il est optionel \n !roll stat user * : permet de lancer un dé, en mentionnant user, vous préciser qui va roll, et stat, la stat associé au roll```"   
    elif commande=="info":
        return "```Voici comment utiliser la commande info :\n un '*' après un nom de variable signifie qu'il est optionel  \n !info user * : permet d'afficher les informations d'un personnage, ses stats et ses infos actuelles```"
    elif commande =="attaque" :
        return "```Voici comment utiliser la commande attaque :\n un '*' après un nom de variable signifie qu'il est optionel\n !attaque cible arme attaquant*: permet d'attaquer la cible en incarnant l'attaquant qui se bat avec arme, pour la liste des armes : \n dague, arc, masse, lance, epeeCourte, epeeLongue, hache, arbalete, assassinat, serpe, briselame, FendDragon \nveuillez être sûr de pouvoir attaquer (avec un roll) et de verifier que vous pouvez avoir cette arme.```"    
    elif commande=="heal" :
        return "```Voici comment utiliser la commande heal :\n !heal cible nombre : permet de soigner un joueur de X points de vie```"   
    elif commande=="changeForme"  :
        return """```Voici comment utilier la commande changeForme :
    \n !changeForme forme : pour les joueurs ayant des "formes" (Omega, Monke, Eddy), permet de changer de forme \n pour Omega : mettre la couleur de sa forme. \n pour Monke : mettre rage ou Rage pour entrer en mode ANGRY, mettre autre chose pour en sortir```""" 
    elif commande=="paye" or commande=="payeNPC" :
        return """```Voici comment utiliser les commandes de paye : \n un "*" après un nom de variable signifie qu'il est optionel
    \n !payeNpc nombre Qui * : vous fait perdre de l'argent, juste une action rp\n !paye  PourQui nombre Qui *: permet de vous donner entre joueurs de l'argent si vous le voulez```"""
    elif commande=="level" :
        return """```Voici comment utiliser la commande de level up :\n !level stat : augmente la stat indiqué de 1 si vous avez un point de compétence```"""
    elif commande=="ordre" :
        return """```Voici comment utiliser la commande ordre :\n !ordre Nom1 Nom2 Nom3 (autant que vous voulez) : permet de définir l'ordre des joueurs dans un combat'''"""
    elif commande=="update" :
        return """```Voici comment utiliser la commande update :\n !update : Met à jour vos stats dans la sauvegarde. Utile si mon pc vient a s'éteindre'''"""
    elif commande=="admin" :
        return """addMoney(user,nb)
                \nremoveMoney(user,nb)
                \naddXP(user,nb)
                \nremoveXP(user,nb)
                \nsetMaxMob(nb)
                \nsetMaxBoss(nb)
                \ncreateMob(nom,force,dex,intel,end,percep,elo,esp,magie)
                \ncreateBoss(nom,force,dex,intel,end,percep,elo,esp,magie)
                \n\ncommandes uniquement pour Eddy
                En plus vous avez la forme dégueulasse pour python ptdr"""
    elif commande=="lanceSort":
        return "```Voici comment utiliser la commande lanceSort :\n !lanceSort cible NomSort attaquant * : lance le sort dit (nom du sort soit bien correct)\n Si un de vos sorts __offensifs__ n'apparrait pas, veuillez me le dire.```"
    else :
        return """```Voici l'entièreté des commandes disponibles ainsi que leur fonctionnement:
                        \n un "*" après un nom de variable signifie qu'il est optionel
                        \n !aide commande * : permet de renvoyé l'aide sur une commande, si rien n'est précisé, ce message s'affiche 
                        \n !roll stat user *: permet de lancer un dé, en mentionnant user, vous préciser qui va roll, et stat, la stat associé au roll
                        \n !info user * : permet d'afficher les informations d'un personnage, ses stats et ses infos actuelles
                        \n !attaque cible attaquant *: permet d'attaquer la cible en incarnant l'attaquant qui se bat avec arme\nveuillez être sûr de pouvoir attaquer (avec un roll) et de vérifier que vous pouvez avoir cette arme.
                        \n !lanceSort cible NomSort attaquant * : lance le sort dit (nom du sort soit bien correct)
                        \n !heal cible nombre : permet de soigner un joueur de X points de vie
                        \n !changeForme forme : pour les joueurs ayant des "formes" (Omega, Monke, Eddy), permet de changer de forme \n pour Omega : mettre la couleur de sa forme. \n pour Monke : mettre rage ou Rage pour entrer en mode ANGRY, mettre autre chose pour en sortir
                        \n !payeNpc nombre Qui *: vous fait perdre de l'argent, juste une action rp
                        \n !paye PourQui nombre Qui *: permet de vous donner entre joueurs de l'argent si vous le voulez
                        \n !level stat : augmente la stat indiqué de 1 si vous avez un point de compétence
                        \n !ordre Nom1 Nom2 Nom3 (autant que vous voulez) : permet de définir l'ordre des joueurs dans un combat
                        \n !update : Met à jour vos stats dans la sauvegarde. Utile si mon pc vient a s'éteindre```"""
