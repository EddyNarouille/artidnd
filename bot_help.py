

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
                \naugmentePV(ctx,nom,nb)
                \ncreateMob(ctx,nom,force,habilite,constitution,charisme,foi,classe,niveau, *args))
                \ncreateBoss(ctx,nom,force,habilite,constitution,charisme,foi,classe,niveau, *args)
                \nconcocter(ctx,potion,nom,nb=1) 
                \nhit(ctx,dest,nb)
                \nordre(ctx,*args)
                \nnewDay(ctx, heal = False)
                \nrefaireOrdre(ctx,grandeChaine):
                \n\ncommandes uniquement pour Eddy
                En plus vous avez la forme dégueulasse pour python ptdr"""
    elif commande=="lancePotion":
        return "```Voici comment utiliser la commande lancePotion :\n !lanceSort cible nomPotion envoyeur * : lance la potion dite (nom de la potion soit bien correct)\n La potion fera ainsi automatiquement avoir les mêmes effets que si bu par la personne.```"
    elif commande == "seDeplacer" :
        return "```Voici comment utiliser la commande seDeplacer :\n !seDeplacer x y : positionne votre personnage aux coordonnées indiqués si la place est libre, il faut que la position sois a maximum deux cases de vous (vous pouvez vous deplacer en diagonal de 2 places), si vous souhaitez courir et vous déplacer plus loin au prix d'une action, faites cette commande deux fois.\nVous pouvez traverser les obstacles en théorie avec cette commande, si vous le faites, je vous frappe```"
    elif commande == "prendreHerbe" :
        return "```Voici comment utiliser la commande prendreHerbe :\n !prendreHerbe nomJoueur taille * (par défaut petit) : permet de soigner un joueur hors combat en lui donnant des herbes curratives, petites ou grandes. Voyez avec Eddy pour savoir si vous en avez.```"
    else :
        return """```Voici l'entièreté des commandes disponibles ainsi que leur fonctionnement:
                        \n un "*" après un nom de variable signifie qu'il est optionel
                        \n !aide commande * : permet de renvoyé l'aide sur une commande, si rien n'est précisé, ce message s'affiche 
                        \n !roll stat user *: permet de lancer un dé, en mentionnant user, vous préciser qui va roll, et stat, la stat associé au roll
                        \n !info user * : permet d'afficher les informations d'un personnage, ses stats et ses infos actuelles
                        \n !attaque cible attaquant *: permet d'attaquer la cible en incarnant l'attaquant qui se bat avec arme\nveuillez être sûr de pouvoir attaquer (avec un roll) et de vérifier que vous pouvez avoir cette arme.
                        \n !lancePotion cible NomPotion attaquant * : lance la potion dite (nom de la potion soit bien correct)
                        \n !heal cible nombre : permet de soigner un joueur de X points de vie
                        \n !changeForme forme : pour les joueurs ayant des "formes" (Omega, Monke, Eddy), permet de changer de forme \n pour Omega : mettre la couleur de sa forme. \n pour Monke : mettre rage ou Rage pour entrer en mode ANGRY, mettre autre chose pour en sortir
                        \n !payeNpc nombre Qui *: vous fait perdre de l'argent, juste une action rp
                        \n !paye PourQui nombre Qui *: permet de vous donner entre joueurs de l'argent si vous le voulez
                        \n !level stat : augmente la stat indiqué de 1 si vous avez un point de compétence
                        \n !ordre Nom1 Nom2 Nom3 (autant que vous voulez) : permet de définir l'ordre des joueurs dans un combat
                        \n !update : Met à jour vos stats dans la sauvegarde. Utile si mon pc vient a s'éteindre
                        \n !positionner : place un joueur au coordoonnées données
                        \n !r NdM : avec N le nombre de dé à lancer et M le nombre de face du dé : !r 3d6 = roll 3 dé à 6 faces
                        \n !getMap : permet de voir la map
                        \n !getOrdre : permet de voir le tour de combat et qui doit jouer
                        \n !next : termine le tour d'un joueur pour passer au suivant
                        \n !seDeplacer : permet de repositionner son personnage aux coordonnées demandées*
                        \n !prendreHerbe : permet de se la jouer Bob Marley et de se soigner avec
                        \n !mesPotions : vous permet de voir vos potions et leur quantité
                        \n !boirePotion : permet de boire une potion, écrivez bien le nom de la potion```"""
