from random import *
import os

#declaration de toutes les variables pour quelles soient global

#jet de dés
des1=0
des2=0
totalDes=0

#nb de tours
tour=0

scoreDes= False             #définition de la variable pour activer la spécificité du jet de dés quand on se trouve sur 0
caseOie=0                   #définition de la case oie pour pouvoir changer sa valeur dans les fonctions

#-----------------------Variables mode solo uniquement-----------------------
#tours sans pouvoir jouer
tourHotelPuitsPrisonj=0
tourHotelPuitsPrisono=0

j=0  #score du joueur
o=0  #score de l'ordinateur

#-----------------------Variables mode multi uniquement-----------------------

nom = []
score = [0,0,0,0,0]
tourHotelPuitsPrison = [0,0,0,0,0]

#-----------------------Toutes les fonctions du code-----------------------

#-----------------------Fonctions mode solo ou solo et multi-----------------------

#fonction aleatoire pour les dés
def jeterDeDes():
    global totalDes             #utilisation des variables globles
    global des1
    global des2
    des1=randint(1,6)           #jet aleatoire des dés
    des2=randint(1,6)
    totalDes=des1+des2          #total des deux dés

def jeterDeDesJoueur():
    print("Vous avez fait "+str(des1)+" et "+str(des2)+", vous avancez de "+str(totalDes)+" cases")

def jeterDeDesOrdi():
    print("L'ordinateur a fait "+str(des1)+" et "+str(des2)+", il avance de "+str(totalDes)+" cases")

def jeterDeDesJoueurs():
    print(nom[i],"vous avez fait "+str(des1)+" et "+str(des2)+", vous avancez de "+str(totalDes)+" cases")

#fonction pour empècher le dépacement de la case 63
def pasPlusDeLaCase63():
    global o
    global j
    if j>63:                #quand le joueur dépasse 63 retourne en arrière
       reste=j%63
       j=63-reste
    elif o>63:              #idem avec ordinateur
       reste=o%63
       o=63-reste

#quand le premier score des dés du joueur fait 6 et 3 ou 5 et 4 on arrive à une case précise
def scoreDesTour1j():
    global des1
    global des2
    global scoreDes
    global j
    if j==0:
        if (des1==6 or des1==3 and des2==6 or des2==3) and des1+des2==9:      #test de la combinaison des dés pour 3 et 6, si bonne combi va direct à la case 26
            scoreDes=True
            j=26
        elif (des1==5 or des1==4 and des2==5 or des2==4) and des1+des2==9:    #test de la combinaison des dés pour 4 et 5, si bonne combi va direct à la case 53
            scoreDes=True
            j=53

#idem pour l'ordinateur
def scoreDesTour1o():
    global des1
    global des2
    global scoreDes
    global o
    if o==0:
        if (des1==6 or des1==3 and des2==6 or des2==3) and des1+des2==9:
            scoreDes=True
            o=26
        elif (des1==5 or des1==4 and des2==5 or des2==4) and des1+des2==9:
            scoreDes=True
            o=53

#toutes les cases où s'effectue des actions spéciales
def eventj():
    global j
    global tourHotelPuitsPrisonj
    if plateau_de_jeu[j] == 1:      #partie pour doubler le score des dés du joueur si il tombe sur une case oie
        j=j+totalDes
        pasPlusDeLaCase63()
        print("Vous tombez sur une case Oie, vous avez doublé votre score ! Donc vous avancez de nouveau de "+str(totalDes))
        print(nomDuJoueur+", vous êtes maintenant sur la case "+str(j))
    elif plateau_de_jeu[j] == 2 :
        print("Vous tombez dans un puits, vous pourrez sortir dans 3 tours ou si l'ordinateur tombe sur la même case que vous, au quel cas il prendra votre place")
        tourHotelPuitsPrisonj=3     #3 tours d'attente
    elif plateau_de_jeu[j] == 6 :
        print("Vous arrivez dans une prison vous pourrez sortir dans 3 tours ou si l'ordinateur tombe sur la même casse que vous, au quel cas il prendra votre place")
        tourHotelPuitsPrisonj=3     #3 tours d'attente
    elif plateau_de_jeu[j] == 3:
        print("Vous vous sentez fatigué(e), vous desidez de vous arrêter dans un hotel. Vous passez 2 tours")
        tourHotelPuitsPrisonj=2     #2 tours d'attente
    elif plateau_de_jeu[j] == 4:
        print("Vous vous êtes perdu(e) dans un labytrinte ! Vous êtes de retour à la case 30")
        j=30                        #retour case 30
        print(nomDuJoueur+", vous êtes maintenant sur la case "+str(j))
    elif plateau_de_jeu[j] == 5:
        print("Vous tombez dans un piège mortel ! Vous recommencez du début !")
        j=0                         #retour case 0
        print(nomDuJoueur+", vous êtes maintenant sur la case "+str(j))

#idem pour l'ordinateur
def evento():
    global o
    global tourHotelPuitsPrisono
    if plateau_de_jeu[o] == 1:
        o=o+totalDes
        pasPlusDeLaCase63()
        print("Il tombe donc sur une case Oie, il double son score ! Il avance de nouveau de "+str(totalDes))
        print("Il est maintenant sur la case "+str(o))
    elif plateau_de_jeu[o] == 2:
        print("Il tombe dans un puits il pourra sortir dans 3 tours ou si vous tombez sur la même case que lui, au quel cas vous prendrez sa place")
        tourHotelPuitsPrisono=3
    elif plateau_de_jeu[o] == 6:
        print("Il arrive dans une prison il pourra sortir dans 3 tours ou si vous tombez sur la même case que lui, au quel cas vous prendrez sa place")
        tourHotelPuitsPrisono=3
    elif plateau_de_jeu[o] == 3 :
        print("Il s'arrête dans un hotel, où il va y passer 2 tours")
        tourHotelPuitsPrisono=2
    elif plateau_de_jeu[o] == 4:
        print("l'ordinateur s'est perdu dans un labytrinte ! Il se retrouve à la case 30")
        o=30
        print("L'ordinateur est maintenant sur la case "+str(o))
    elif plateau_de_jeu[o] == 5:
        print("l'ordinateur est tombé dans un piège mortel ! Il recommence du début !")
        o=0
        print("L'ordinateur est maintenant sur la case "+str(o))

def event():
    global score
    global tourHotelPuitsPrison
    if plateau_de_jeu[score[i]] == 1:                              #partie pour doubler le score des dés du  joueur si il tombe sur une case oie
        score[i]=score[i]+totalDes
        pasPlusDeLaCase63Multi()
        print("Vous tombez sur une case Oie, vous avez doublé votre score ! Donc vous avancez de nouveau de "+str(totalDes))
        print(nom[i]+", vous êtes maintenant sur la case "+str(score[i]))
    elif plateau_de_jeu[score[i]] == 2 :
        print("Vous tombez dans un puits, vous pourrez sortir dans 3 tours ou si l'ordinateur tombe sur la même case que vous, au quel cas il prendra votre place")
        tourHotelPuitsPrison[i]=3     #3 tours d'attente
    elif plateau_de_jeu[score[i]] == 6 :
        print("Vous arrivez dans une prison vous pourrez sortir dans 3 tours ou si l'ordinateur tombe sur la même casse que vous, au quel cas il prendra votre place")
        tourHotelPuitsPrison[i]=3     #3 tours d'attente
    elif plateau_de_jeu[score[i]] == 3:
        print("Vous vous sentez fatigué(e), vous desidez de vous arrêter dans un hotel. Vous passez 2 Tours")
        tourHotelPuitsPrison[i]=2     #2 tours d'attente
    elif plateau_de_jeu[score[i]] == 4:
        print("Vous vous êtes perdu(e) dans un labytrinte ! Vous êtes de retour à la case 30")
        score[i]=30
        print(nom[i]+", vous êtes maintenant sur la case "+str(score[i]))
    elif plateau_de_jeu[score[i]] == 5:
        print("Vous tombez dans un piège mortel ! Vous recommencez du début !")
        score[i]=0
        print(nom[i]+", vous êtes maintenant sur la case "+str(score[i]))

#fonction pour rejouer une partie
def rejouerPartie():
    global j
    global o
    global tour
    global score
    print("")
    rejouer=input("Voulez-vous rejouer, oui ou non ?")

    while rejouer != "Oui" and rejouer != "Non" and rejouer != "oui" and rejouer != "non":      #si l'utilisateur ne rentre pas Oui ou Non repose la question
        rejouer=input("Veuillez répéter votre choix : ")

    if rejouer == "Oui" or rejouer == "oui":                    #quand oui remet tous les scores à 0
        j=0
        o=0
        score = [0,0,0,0,0]
        tour=0
        print("")
        recommancerLaPartie=input("Appuyez sur entrée pour recommencer une partie")
    elif rejouer == "Non" or rejouer == "non":
        print("")
        input("Appuyez sur entrée pour quitter la partie")      #quand non ferme la console
        sys.exit()
    os.system("cls")


#-----------------------Fonctions mode multi-----------------------

#même fonction que pour mode solo avec une liste
def scoreDesTour1():
    global des1
    global des2
    global scoreDes
    global score
    if score[i]==0:
        if ((des1==6 or des1==3) or (des2==6 or des2==3)) and des1+des2==9:      #test de la combinaison des dés pour 3 et 6
            scoreDes=True
            score[i]=26
        elif ((des1==5 or des1==4) or (des2==5 or des2==4)) and des1+des2==9:    #test de la combinaison des dés pour 4 et 5
            scoreDes=True
            score[i]=53

#idem
def pasPlusDeLaCase63Multi():
    global score
    if score[i]>63:
       reste=score[i]%63
       score[i]=63-reste

#fonction pour tester toutes les possibilitées que deux personnes soit sur la même case
def liberation():
    global score
    global tourHotelPuitsPrison
    if score[0]==score[1]==31 or score[0]==score[2]==31 or score[0]==score[3]==31 or score[0]==score[4]==31 or score[1]==score[2]==31 or score[1]==score[3]==31 or score[1]==score[4]==31 or score[2]==score[3]==31 or score[2]==score[4]==31 or score[3]==score[4]==31:
        tourHotelPuitsPrison[i]=0               #si deux personnes sont sur la même case annule les tours d'attente de la case 31
        print("Un autre joueur a pris votre place dans le piège")
    elif score[0]==score[1]==52 or score[0]==score[2]==52 or score[0]==score[3]==52 or score[0]==score[4]==52 or score[1]==score[2]==52 or score[1]==score[3]==52 or score[1]==score[4]==52 or score[2]==score[3]==52 or score[2]==score[4]==52 or score[3]==score[4]==52:
        tourHotelPuitsPrison[i]=0               #si deux personnes sont sur la même case annule les tours d'attente de la case 52
        print("Un autre joueur a pris votre place dans le piège")

#-----------------------Plateau de jeu-----------------------

plateau_de_jeu = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,3,0,0,0,1,0,0,0,0,0,0,0,2,0,1,0,0,0,0,0,0,1,0,4,0,0,0,0,0,1,0,0,0,6,0,0,0,0,1,5,0,0,0,0,0]

#-----------------------Commencement de l'affichage-----------------------

#-----------------------Choix de son mode-----------------------

print("Voulez vous jouer en multijoueur ou en solo?")
modeDeJeu=input("Tapez 'multi' pour le mode multijoueur et 'solo' pour le mode solo : ")

while modeDeJeu != "solo" and modeDeJeu != "multi":             #verifie le mode de jeu
    print("Erreur veillez ressaisir la commande")               #redemande si réponse différente de multi ou solo
    modeDeJeu=input("taper 'muti' pour le mode mulltijoueur et 'solo' pour le mode solo : ")

#-----------------------Mode de jeu solo-----------------------

if modeDeJeu == "solo":
    #Rentré du nom du joueur
    nomDuJoueur=input("Quel est votre nom ?")
    print("Bienvenue dans le jeu de l'oie " + nomDuJoueur)
    print(nomDuJoueur + " vous allez jouer contre un ordinateur")
    os.system("cls")

    #repéter les tours tant qu'un des joueur n'est pas sur la derinère case (63)
    while j<63 and o<63 :
        tour=tour+1                             #annonce des tours
        print("Tour "+str(tour))
        print(nomDuJoueur+" = "+str(j))         #annonce des scores
        print("Ordinateur = "+str(o))
        print("")

    #le joueur joue
        if j==o==31 or j==o==52:                #quand l'ordi tombe sur la même case libert le joueur du piege en suprimant les tours d'attente
            tourHotelPuitsPrisonj=0
            print("L'ordinateur a pris votre place dans le piège")
        if tourHotelPuitsPrisonj!=0:            #met un terme au tour du joueur si le joueur a des tours d'attente
            print("Vous ne pouvez pas jouer ce tour")
        else:                                   #tour normale d'un joueur
            print("A ton tour de jouer !")
            lancerDeDes=input("Pour lancer les dés appuyez sur entrée")
            jeterDeDes()                        #suite de fonction pour le tour du joueur (lancé de dés, combinaisons spéciales pour le tour 1)
            scoreDesTour1j()
            if scoreDes==True:                  #si bonne combinaison de dés racourssis sur le plateau
                scoreDes=False                  #True en False sinon boucle et impossible de continuer
                print("Vous avez fait " + str(des1) + " et "+ str(des2) , nomDuJoueur + ", vous trouvez un raccourcis et atterrissez sur la case "+str(j))
            else:
                jeterDeDesJoueur()
                j=j+totalDes                    #score du joueur actualisé
                pasPlusDeLaCase63()             #permet de ne pas dépasser 63
                print(nomDuJoueur+", vous êtes sur la case "+str(j))
                eventj()                        #cases special (oie, hotel, puits, labyrinte, prison, piège mortel)
        if tourHotelPuitsPrisonj>0:
            tourHotelPuitsPrisonj=tourHotelPuitsPrisonj-1           #réduction de un tour d'arret de jeu
            if j==31 or j==52:                                      #différents textes selon la case special (prison,puits) ou (hotel)
                print("Il vous reste "+str(tourHotelPuitsPrisonj+1)+" tours à attendre si personne ne vous sauve")
            else:
                print("Vous vous reposez encore pendant "+str(tourHotelPuitsPrisonj+1)+" tours")
        terminerLeTour=input("Appuyez sur entrée pour terminer votre tour")
        print("")                               #laisse un espace pour la beautée

    #idem pour l'ordinateur en remplaçant les fonctions
        if j==o==31 or j==o==52:
            tourHotelPuitsPrisono=0
            print("Vous avez pris la place de l'ordinateur dans le piège")
        if tourHotelPuitsPrisono!=0:
            print("L'ordinateur ne peux pas jouer ce tour")
        else:
            print("Au tour de l'ordinateur !")
            jeterDeDes()
            scoreDesTour1o()
            if scoreDes==True:
                scoreDes=False
                print("L'ordinateur a fait " + str(des1) + " et "+ str(des2) ,"il a trouvé un raccourcis et a atterri sur la case "+str(j))
            else:
                jeterDeDesOrdi()
                o=o+totalDes
                pasPlusDeLaCase63()
                print("L'ordinateur est sur la case "+str(o))
                evento()
        if tourHotelPuitsPrisono>0:
            tourHotelPuitsPrisono = tourHotelPuitsPrisono - 1
            if o==31 or o==52:
                print("Il reste "+str(tourHotelPuitsPrisono + 1)+" tours à l'ordinateur, à attendre si personne ne le sauve")
            else:
                print("L'ordinateur se repose encore "+str(tourHotelPuitsPrisono+1)+" tours")
        terminerLeTour=input("Appuyez sur entrée pour commencer votre tour")
        os.system("cls")

    #différante phrase selon si le joueur ou l'ordi gagne
        if j==63:
            print("Bienjoué(e) "+nomDuJoueur+" vous avez gagné cette partie contre l'ordinateur !")
            rejouerPartie()                     #fonction pour choisir d'arrêter ou de recommencer
        elif o==63:
            print("l'ordinateur a gagné ! Vous aurez peut-être plus de chance la prochaine fois")
            rejouerPartie()                     #idem

#-----------------------Mode de jeu multijoueur-----------------------

elif modeDeJeu == "multi":
    nombreDeJoueur=int(input("Combien de joueurs êtes vous ? (max 5) : "))      #choix du nb de joueur avec une limite à 5

    while nombreDeJoueur < 2 or nombreDeJoueur > 5 :
        nombreDeJoueur=int(input("Combien de joueurs êtes vous ? : "))

    for i in range(nombreDeJoueur):                                             #ajout des noms à une liste
    	nom.append(input("Quel est votre nom du Joueur " + str(i+1) + " ?"))
    os.system("cls")

#idem que le mode solo avec des listes
    while score[0]<63 and score[1]<63 and score[2]<63 and score[3]<63 and score[4]<63 :
        tour=tour+1
        print("Tour "+str(tour))
        for i in range(nombreDeJoueur):
            print(nom[i]+" = "+str(score[i]))           #annonce des scores
        print("")
        for i in range(nombreDeJoueur):
            liberation()                                #fonction pour remettre à zéro les tours d'attente si qq un est sur la même case
            if tourHotelPuitsPrison[i]!=0:
                print(nom[i]+", vous ne pouvez pas jouer ce tour")
            else:
                print(nom[i],"à votre tour de jouer !")
                lancerDeDes=input("Pour lancer les dés appuyez sur entrée")
                jeterDeDes()
                scoreDesTour1()
                if scoreDes==True:
                    scoreDes=False
                    print(nom[i]+", vous avez fait " + str(des1) + " et "+ str(des2) , nom[i] + ", vous trouvez un raccourcis et atterrissez sur la case "+str(score[i]))
                else:
                    jeterDeDesJoueurs()
                    score[i]=score[i]+totalDes
                    pasPlusDeLaCase63Multi()
                    print(nom[i]+", vous êtes sur la case "+str(score[i]))
                    event()
                    print("")
            if tourHotelPuitsPrison[i]>0:
                tourHotelPuitsPrison[i]=tourHotelPuitsPrison[i]-1
                if score[i]==31 or score[i]==52:
                    print("Il vous reste "+str(tourHotelPuitsPrison[i]+1)+" tours à attendre si personne ne vous sauve")
                    print("")
                else:
                    print("Vous vous reposez encore pendant "+str(tourHotelPuitsPrison[i]+1)+" tours")
                    print("")
        terminerLeTour=input("Appuyez sur entrée pour terminer ce tour")
        os.system("cls")
        for i in range(nombreDeJoueur):
            if score[i]==63:
                print("Bienjoué(e) "+nom[i]+" vous avez gagné cette partie !")
                rejouerPartie()

#-----------------------Fin du code-----------------------