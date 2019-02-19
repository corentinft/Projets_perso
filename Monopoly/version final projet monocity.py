import pygame, os, time, sys
from random import *

game = 1 #Variable de base du jeu
gameTour = 0 #Nombre de tours depuis le debut du jeu

#Variables des dés
dice1=0   #Dés 1
dice2=0  #Dés 2
totalDice=0    #Total de l'addition des dés 1 et 2

doubleForPrison = 0    #Variable denombre le nombre de double des dés par tours

playerPosition = [0,0]    #Liste Position du joueur en train de jouer

playerMoney = [1500,1500]    #Liste de l'argent des joueurs
parkMoney = 0     #Argent de la cagnotte de la case parc gratuit

resttour = 0    #Test nouveau tour (si oui =1)

printText = 0    #Test pour le texte

nom = ["Unname","Unname"]    #Liste des noms des joueurs

#Liste creent le plateau case de 0 à 39
plate = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
#Liste du nom des cases
plateName = ["Case départ","Rue Louis Loucheur","Caisse de Communauté","Rue Charlemagne","Impôt sur le revenu","Conseil général de Vendée","Rue Claude Debussy","Chance","Rue Molière","Boulevard Gaston Defferre","Case Prison","Avenue Picasso","Compagnie de Distribution d'électricité","Avenue de la Vallée Verte","Rue des Jaulnières","Hotel de Ville","Rue de Friedland","Caisse de Communauté","Boulevard le Corbusier","Place Maurice Mornet","Parc Gratuit","Boulevard d'Angleterre","Chance","Boulevard d’Eylau","Avenue Aliénor d'Aquitaine","VendéeSpace","Impasse Thalès","Jardin Mitterrand","Compagnie de Distribution des Eaux","Boulevard Aristide Briand","Allez en Prison","Haras de la Vendée","Rue du Marechal Joffre","Caisse de Communauté","Boulevard Lavoisier","Hôpital de La Roche sur Yon","Chance","Rue du President de Gaulle","Taxe de Luxe","Place Napoléon"]
#Liste des prix des propriétés (Achat terrain)
buyingPrice = [0,60,0,60,0,200,100,0,100,120,0,140,150,140,160,200,180,0,180,200,0,220,0,220,240,200,260,260,150,280,0,300,300,0,320,200,0,350,0,400]
#Liste des prix d'hypotheques des propriétés
hypothec = [0,30,0,30,0,100,50,0,50,60,0,70,75,70,80,100,90,0,90,100,0,110,0,110,120,100,130,130,75,140,0,150,150,0,160,100,0,175,0,200]
#Liste des prix de l'achat d'une maison (en fonction du terrain)
houseHotel = [0,50,50,0,0,50,0,50,50,0,100,0,100,100,0,100,0,100,100,0,150,0,150,150,0,150,150,0,150,0,200,200,0,200,0,0,200,0,200]

#Prix de base quand un joueur tombe sur une propriété qui n'est pas a lui
basePrice = [0,2,0,4,0,25,6,0,6,8,0,10,0,10,12,25,14,0,14,16,0,18,0,18,20,25,22,22,0,24,0,26,26,0,28,25,0,35,0,50]
#Prix a payer quand un joueur tombe sur une propriété qui n'est pas a lui (avec 1 maison)
oneHouse = [10,20,30,30,40,50,50,60,70,70,80,90,90,100,110,110,120,130,130,150,175,200,50]
#Prix a payer quand un joueur tombe sur une propriété qui n'est pas a lui (avec 2 maison)
twoHouse = [30,60,90,90,100,150,150,180,200,220,250,250,300,330,330,360,390,390,450,500,600,100]
#Prix a payer quand un joueur tombe sur une propriété qui n'est pas a lui (avec 3 maison)
threeHouse = [90,180,270,270,300,450,450,500,550,550,600,700,700,750,800,800,850,900,900,1000,1100,1400,200]
#Prix a payer quand un joueur tombe sur une propriété qui n'est pas a lui (avec 4 maison)
fourHouse = [160,320,400,400,450,625,625,700,750,750,800,875,875,925,975,975,1025,1100,1100,1200,1300,1700]
#Prix a payer quand un joueur tombe sur une propriété qui n'est pas a lui (avec 1 hotel)
hotel = [250,450,550,550,600,750,750,900,950,950,1000,1050,1050,1100,1150,1150,1200,1275,1275,1400,1500,2000]


caseBuy = [0,2,4,7,10,17,20,22,30,33,36,38]   #Case imposible a acheter

nPropPlayer = [0,0]    #Nombre de propriété pour chaque joueur

lapsInPri = [0,0]    #Nombre de tours en prion
cardJailPlayer = [0,0]    #Si le joueur pocede une carte sortie de prison
proprietyplayer=[[],[]]    #Propriété pocédé par les joueurs

#Variables Couleurs
white = 255,255,255 #Couleur Blanc
red = 255,0,0    #Couleur Rouge
black = 0,0,0    #Couleur Noir
blue = 0,255,0    #Couleur Bleu
green = 0,0,255    #Couleur Vert

colour = [red,black]    #Liste de couleur

#Coordonée de depart
xstartplace = 975   #Place en x
ystartplace = 485    #Place en y


size = witdh, height = 1500,700    #Taille de la fenetre

clock = pygame.time.Clock()    #Variable qui prend la valeur du temps
screen = pygame.display.set_mode(size)    #Variable qui facilite l'affichage de la fenetre


#Fenetre de Base Pygame
pygame.init()
pygame.display.set_caption("MonoCity")
img_menu=pygame.image.load("plateau.png")
logo = pygame.image.load("monocity.png")

screen.fill(white)
screen.blit(img_menu, (750-260,0))
screen.blit(logo,(0,0))

#Affichage du pion rouge
pygame.draw.circle(screen,red,(xstartplace,ystartplace),9)

#Affichage Rectangle joueur 1
pygame.draw.rect(screen,black,(20,10,450,245),2)

#Affichage Rectangle joueur 2
pygame.draw.rect(screen,black,(20,265,450,245),2)


#Affichage du 1er rectange large en bas
pygame.draw.rect(screen,black,(20,530,1450,160),2)

#Affichage du texte de bienvenue
myfont = pygame.font.SysFont("arial", 20)
label = myfont.render("Bienvenue dans MonoCity !", 10, (0,0,0))
screen.blit(label, (40, 540))

pygame.display.flip()

#-------------------Nombre de joueur de nom des joueurs -------------------------

nPlayer= 2    #Nombre de joueur

for i in range(0,nPlayer):   #Boucle qui demande a tous les joueurs leurs noms
   	nom[i] = (input("Quel est votre nom du Joueur " + str(i+1) + " ?")) #ajout des noms à une liste

os.system("cls")    #Clear de la console

#--------------------------------------------------------------------------------

#Liste des coordonées des cases
x = [975,919,877,835,793,750,707,665,623,581,525,525,525,525,525,525,525,525,525,525,525,581,623,665,707,750,793,835,877,919,975,975,975,975,975,975,975,975,975,975]
y = [485,485,485,485,485,485,485,485,485,485,485,429,387,345,303,260,217,175,133,91,35,35,35,35,35,35,35,35,35,35,35,91,133,175,217,260,303,345,387,429]


#Fonction qui lance les deux dés
def diceRoll():
    global totalDice
    global dice1
    global dice2
    dice1=randint(1,6)    #le Dés 1 prend une valeur aléatoire entre 1 et 6
    dice2=randint(1,6)    #le Dés 2 prend une valeur aléatoire entre 1 et 6
    totalDice = dice1 + dice2    #Le total des dés prend la valeur des deux deés

#Fonction qui permet de recomancer un tour de plateau
def startTurnAgaine():
    global totalDice
    global playerPosition
    global resttour
    if playerPosition[i-1] > 39 :    #Si le jouer est a une case superieur a 39 alors
        residue = playerPosition[i-1]%39    #Reste de la division euclidienne de la position du joueur par le nombre de case
        playerPosition[i-1] = residue -1   #La Position du joueur est le reste -1 (car les cases commances par 0)
        resttour = 1    #Info : le joueur a passé la case depart

ncardcomu = 0    #Le numero de la carte Comunauté
def cardcomu ():
    global ncardcomu
    global playerPosition
    global lapsInPri
    global playerMoney
    global nPlayer
    global parkMoney
    if ncardcomu == 1 :    #Carte Comunauté 1
        playerMoney[i-1] = playerMoney[i-1]-200    #Le joueur est débité de 200€
        parkMoney = parkMoney + 200    #La cagnotte du parc gratuit esr credité de 200€
    if ncardcomu == 2 :    #Carte Comunauté 2
        playerMoney[i-1] = playerMoney[i-1]+500 #Le joueur est credité de 500€
    if ncardcomu == 3 :    #Carte Comunauté 3
       lapsInPri[i-1] = 0
       lapsPrison()

    if  ncardcomu == 4 :    #Carte Comunauté 4
        playerMoney[i-1] = playerMoney[i-1]-100    #Le joueur est débité de 100€
        parkMoney = parkMoney + 100    #La cagnotte du parc gratuit est credité de 100€

    if  ncardcomu == 5 :    #Carte Comunauté 5
        playerMoney[i-1] = playerMoney[i-1]+50    #Le joueur est credité de 50€

    if  ncardcomu == 6 :    #Carte Comunauté 6
        playerMoney[i-1] = playerMoney[i-1]+100    #Le joueur est credité de 100€

    if  ncardcomu == 7 :    #Carte Comunauté 7
        playerMoney[i-1] = playerMoney[i-1]+100    #Le joueur est credité de 100€

    if  ncardcomu == 8 :    #Carte Comunauté 8
        playerMoney[i-1] = playerMoney[i-1]+100    #Le joueur est credité de 100€

    if  ncardcomu == 9 :    #Carte Comunauté 9
        playerPosition[i-1] = (1+40)-playerPosition[i-1]    #Le joueur est depalacé a une case présise
        startTurnAgaine()    #Le tour de plateau recomance si le joueur passe la case depart

    if  ncardcomu == 10 :    #Carte Comunauté 10
        playerPosition[i-1] = (40+playerPosition[i-1])-playerPosition[i-1]    #Le joueur est depalacé a une case présise
        startTurnAgaine()    #Le tour de plateau recomance si le joueur passe la case depart

    if  ncardcomu == 11 :    #Carte Comunauté 11
        playerMoney[i-1] = playerMoney[i-1] + (50*nPlayer) # le joueur est credité de 50 fois le nombre de joueur

    if  ncardcomu == 12 :   #Carte Comunauté 12
        playerMoney[i-1] = playerMoney[i-1]+200     #Le joueur est credité de 200€

    if  ncardcomu == 13 :    #Carte Comunauté 13
        playerMoney[i-1] = playerMoney[i-1]-100     #Le joueur est débité de 100€
        parkMoney = parkMoney + 100    #La cagnotte du parc gratuit est credité de 100€

    if  ncardcomu == 14 :    #Carte Comunauté 14
        playerMoney[i-1] = playerMoney[i-1]+100    #Le joueur est débité de 100€

    if  ncardcomu == 15 :    #Carte Comunauté 15
        playerMoney[i-1] = playerMoney[i-1]+250    #Le joueur est débité de 100€

    if  ncardcomu == 16 :    #Carte Comunauté 16
        playerMoney[i-1] = playerMoney[i-1]-200    #Le joueur est débité de 200€
        parkMoney = parkMoney + 200     #La cagnotte du parc gratuit est credité de 200€

ncardluck = 0    #Le numero de la carte chance

def cardluck ():
    global ncardluck
    global playerPosition
    global lapsInPri
    global playerMoney
    global lapsInPri
    if ncardluck == 1 :    #Carte Chance 1
        playerPosition[i-1] = (40+playerPosition[i-1])-playerPosition[i-1]   #Le joueur est depalacé a une case présise
        startTurnAgaine()    #Le tour de plateau recomance si le joueur passe la case depart

    if ncardluck == 2 :    #Carte Chance 2
        playerPosition[i-1] = 10    #Le joueur est depalacé a une case présise
        lapsInPri = 3    #Tour restant en prison

    if ncardluck == 3:    #Carte Chance 3
        playerPosition[i-1] = (11+40)-playerPosition[i-1]
        startTurnAgaine()    #Le tour de plateau recomance si le joueur passe la case depart

    if ncardluck == 4:    #Carte Chance 4
        playerMoney[i-1] = playerMoney[i-1]-75

    if  ncardluck == 5:    #Carte Chance 5
        playerMoney[i-1] = playerMoney[i-1]+100    #Le joueur est credité de 100€

    if ncardluck == 6:    #Carte Chance 6
        playerPosition[i-1] = (24+40)-playerPosition[i-1]    #Le joueur est depalacé a une case présise
        startTurnAgaine()    #Le tour de plateau recomance si le joueur passe la case depart

    if ncardluck == 7:    #Carte Chance 7
        playerPosition[i-1] = (15+40)-playerPosition[i-1]    #Le joueur est depalacé a une case présise
        startTurnAgaine()    #Le tour de plateau recomance si le joueur passe la case depart

    if ncardluck == 8:    #Carte Chance 8
        playerMoney[i-1] = playerMoney[i-1]-100    #Le joueur est débité de 100€

    if ncardluck == 9:    #Carte Chance 9
        playerMoney[i-1] = playerMoney[i-1]-150    #Le joueur est débité de 150€

    if ncardluck == 10:    #Carte Chance 10
        playerPosition[i-1] = playerPosition[i-1]-3    #Le joueur est depalacé a une case présise
        startTurnAgaine()    #Le tour de plateau recomance si le joueur passe la case depart

    if ncardluck == 11:    #Carte Chance 11
        global playerPosition

    if ncardluck == 12:    #Carte Chance 12
        playerMoney[i-1] = playerMoney[i-1]+150    #Le joueur est credité de 150€

    if ncardluck == 13:    #Carte Chance 13
        if lapsInPri == 0 :
            cardJailPlayer[i-1] = cardJailPlayer[i-1] + 1 #Le joueur est credité d'une carte sortie de prison
        else :
            lapsInPri = 0    #Le joueur passe 0 tour en prison
            lapsPrison()

    if ncardluck == 14:    #Carte Chance 14
        playerPosition[i-1] = (39+40)-playerPosition[i-1]    #Le joueur est depalacé a une case présise
        startTurnAgaine()    #Le tour de plateau recomance si le joueur passe la case depart

    if ncardluck == 15:    #Carte Chance 15
        global playerMoney

    if ncardluck == 16:    #Carte Chance 16
        playerMoney[i-1] = playerMoney[i-1]+300    #Le joueur est credité de 300€

#Fonction qui genere toute les actions en fonctions des cases
def testCase():
    global playerPosition
    global playerMoney
    global plate
    global plateName
    global buyingPrice
    global caseBuy
    global parkMoney
    global printText

    if (playerPosition[i-1] in caseBuy) == False: #La case sur laquelle est tombé le joueur n'est pas acheté cela lui est donc proposé
        testCase = input("Veux tu acheter la propriété "+ str(plateName[playerPosition[i-1]])+ " qui te couteras "+ str(buyingPrice[playerPosition[i-1]])+ " à l'achat ?(tapes 1 pour acheter)")

        if testCase == "1": #Si le joueur repond 1 alors il achete la propriété

            if playerMoney[i-1] >= buyingPrice[playerPosition[i-1]]:
                playerMoney[i-1] = playerMoney[i-1] - buyingPrice[playerPosition[i-1]]
                caseBuy.append(playerPosition[i-1])
                proprietyplayer[i-1].append(playerPosition[i-1])
                nPropPlayer [i-1] = nPropPlayer [i-1]+1
                printText = 1

            else :
                printText = 2

    else: #Si le joueur tombe sur une case qui n'est pas achetable alors il est sur l'une des suivante alors l'effet ce met en place
        if playerPosition[i-1] == 4:
            printText = 3

        if playerPosition[i-1] == 10:
            printText = 4

        if playerPosition[i-1] == 20:
            if parkMoney > 0:
                printText = 5
            else :
                printText = 6

        if playerPosition[i-1] == 30:
            printText = 7

        if playerPosition[i-1] == 38:
            printText = 8

        if playerPosition[i-1] == 7 or playerPosition[i-1] ==22 or playerPosition[i-1] ==36:
            global ncardluck
            ncardluck=randint(1,16)
            cardluck()

        if playerPosition[i-1] == 2 or playerPosition[i-1] ==17 or playerPosition[i-1] ==33:
            global ncardcomu
            ncardcomu=randint(1,16)
            cardcomu()

#Copie de "testCase" mais uniquement avec le texte
def testCase2():
    global playerPosition
    global playerMoney
    global plate
    global plateName
    global buyingPrice
    global caseBuy
    global parkMoney
    global printText
    if (playerPosition[i-1] in caseBuy) == False:
        if testCase == "1":
            if playerMoney[i-1] >= buyingPrice[playerPosition[i-1]]:
                printText = 1
            else :
                printText = 2
    else:
        if playerPosition[i-1] == 4:
            printText = 3

        if playerPosition[i-1] == 10:
            printText = 4

        if playerPosition[i-1] == 20:
            if parkMoney > 0:
                printText = 5
            else :
                printText = 6

        if playerPosition[i-1] == 30:
            printText = 7

        if playerPosition[i-1] == 38:
            printText = 8


#Fonctions qui defini l'action a faire lorsque qu'un joueur tombe sur une case qui appartient a un autre joueur
def taxeProp():
    global playerPosition
    global playerMoney
    global plate
    #Le joueur qui est chez un autre paye et le proprietaire gagne de l'argent
    if (playerPosition[i-1] in caseBuy) and not (playerPosition[i-1] in proprietyplayer[i-1]) :
        playerMoney[i-1] = playerMoney[i-1] - basePrice[playerPosition[i-1]]

    if (playerPosition[i-1] in proprietyplayer[0]) and not (playerPosition[i-1] in proprietyplayer[i-1]):
        playerMoney[0] = playerMoney[0] + basePrice[playerPosition[i-1]]

    elif (playerPosition[i-1] in proprietyplayer[1]) and not (playerPosition[i-1] in proprietyplayer[i-1]):
        playerMoney[1] = playerMoney[1] + basePrice[playerPosition[i-1]]

#Fonction qui reuni les autres cases spetiales
def speCase():
    global playerPosition
    global playerMoney
    global caseBuy
    #Si un joueur tombe sur une des cases parmis celle non achtable alors il est forcement sur l'une d'entre elle. Alors sur "effet" s'active
    if (playerPosition[i-1] in caseBuy) == True:
        taxCase()
        taxCase2()
        parkCase()
        tribunalCase()

#Le joueur est credité de 200€ si il passe sur la case depart. Et son tour de plateau est remis a 0
def startCase():
    global playerPosition
    global playerMoney
    global parkMoney
    global resttour
    global printText
    if resttour == 1:
        playerMoney[i-1] = playerMoney[i-1] + 200
        printText == 9
        resttour = 0

#Effet de la case Taxe n°1
def taxCase():
    global playerPosition
    global playerMoney
    global parkMoney
    if playerPosition[i-1] == 4:
        playerMoney[i-1] = playerMoney[i-1] - 200
        parkMoney = parkMoney + 200

#Effet de la case Taxe n°2
def taxCase2():
    global playerPosition
    global playerMoney
    global parkMoney
    if playerPosition[i-1] == 38:
        playerMoney[i-1] = playerMoney[i-1] - 100
        parkMoney = parkMoney + 100

#Fonction : Si un joueur tombe sur la case park gratuit il est credité de toute la valeur de la ca
def parkCase():
    global playerPosition
    global playerMoney
    global parkMoney
    if playerPosition[i-1] == 20:
        playerMoney[i-1] = playerMoney[i-1] + parkMoney
        parkMoney = 0

#Case qui envoie le joueur en Prison si le joueur tombe sur la case "Aller en prison"
def tribunalCase():
    global playerPosition
    global lapsInPri
    if playerPosition[i-1] == 30:
        playerPosition[i-1] = 10
        lapsInPri[i-1] = 3

#Effet quand le joueur est en prison
def lapsPrison():
    global lapsInPri
    global tour
    global dice1
    global dice2
    global playerMoney
    global printText
    global i
    if lapsInPri[i-1] > 0: #Si le joueur a encore des tour a passé en prison il y reste le temps que sa sentance ce termine
        tour = 0
        printText == 10
        diceRoll()
        if dice1 == dice2 :
            tour = 1
            lapsInPri[i-1] = 0
            printText == 11
        elif input("Veux tu payer ta caution ?") == str(1):
            lapsInPri[i-1] = 0
            tour = 0
            playerMoney[i-1] = playerMoney[i-1] - 50
            i = i + 1
            printText == 12
        else:
            lapsInPri[i-1] = lapsInPri[i-1] -1
            if lapsInPri[i-1] == 0 :
                playerMoney[i-1] = playerMoney[i-1] - 50
                printText == 13
            i = i + 1

#Variable contennent tout les textes
def printTextFon():
    global printText
    global plateName
    global playerPosition
    global buyingPrice
    global parkCase
    if printText == 1:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Veux tu acheter la propriété "+ str(plateName[playerPosition[i-1]])+ " qui te couteras "+ str(buyingPrice[playerPosition[i-1]])+ " à l'achat ?", 10, (0,0,0))
        screen.blit(label, (40, 540))
        label = myfont.render("Félicitation, Tu as acheté la propriété "+ str(plateName[playerPosition[i-1]])+ " !", 10, (0,0,0))
        screen.blit(label, (40, 570))
        pygame.display.flip()
    elif printText == 2:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Veux tu acheter la propriété "+ str(plateName[playerPosition[i-1]])+ " qui te couteras "+ str(buyingPrice[playerPosition[i-1]])+ " à l'achat ?", 10, (0,0,0))
        screen.blit(label, (40, 540))
        label = myfont.render("Tu n'as pas assez d'argent pour acheter cette propriété", 10, (0,0,0))
        screen.blit(label, (40, 570))
        pygame.display.flip()
    elif printText == 3:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Tu es tombé sur une case taxe tu as été prélever de 200 €", 10, (0,0,0))
        screen.blit(label, (40, 540))
        pygame.display.flip()
    elif printText == 4:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Tu fais une visite à la prison départementale", 10, (0,0,0))
        screen.blit(label, (40, 540))
        pygame.display.flip()
    elif printText == 5:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Tu es un veritable chanceux tu trouve "+ str(parkCase)+ " € au Parc !", 10, (0,0,0))
        screen.blit(label, (40, 540))
        pygame.display.flip()
    elif printText == 6:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Tu te pose sur un banc au parc et tu profite du paysage", 10, (0,0,0))
        screen.blit(label, (40, 540))
        pygame.display.flip()
    elif printText == 7:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Tu es arrivé au tribunal et le juge te condamne à 3 tour de prison !", 10, (0,0,0))
        screen.blit(label, (40, 540))
        pygame.display.flip()
    elif printText == 8:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Tu es tombé sur une case taxe tu as été prélever de 100 €", 10, (0,0,0))
        screen.blit(label, (40, 540))
        pygame.display.flip()
    elif printText == 9:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Tu es passé sur la case départ tu gagnes 200€", 10, (0,0,0))
        screen.blit(label, (40, 540))
        pygame.display.flip()
    elif printText == 10:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Tu ne peux pas jouer ce tour ci car tu es en prison !", 10, (0,0,0))
        screen.blit(label, (40, 540))
        pygame.display.flip()
    elif printText == 11:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Tu as réussi à sortir de prison !", 10, (0,0,0))
        screen.blit(label, (40, 540))
        pygame.display.flip()
    elif printText == 12:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Veux tu payer ta caution ?", 10, (0,0,0))
        screen.blit(label, (40, 540))
        label = myfont.render("Tu as payer ta caution, tu es libre ! Tu pourras jouer le tour prochain", 10, (0,0,0))
        screen.blit(label, (40, 570))
        pygame.display.flip()
    elif printText == 13:
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("Veux tu payer ta caution ?", 10, (0,0,0))
        screen.blit(label, (40, 540))
        label = myfont.render("Tu es enfin sorti de prison aprés avoir purger ta peine et payer ta caution", 10, (0,0,0))
        screen.blit(label, (40, 570))
        pygame.display.flip()

#Affichage du Texte de fin de tour
def questionEnd():
    global printText
    if printText == 1 or printText == 2 or printText == 12 or printText == 13 :
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("C'est la fin du tour de "+ str(nom[i-1])+ ",au prochain joueur de jouer", 10, (0,0,0))
        screen.blit(label, (40, 600))
    else :
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("C'est la fin du tour de "+ str(nom[i-1])+ ",au prochain joueur de jouer", 10, (0,0,0))
        screen.blit(label, (40, 570))

#Fonction du rectangle d'information en bas
def botrect ():
    #Creation du rectangle
    pygame.draw.rect(screen,black,(20,530,1450,160),2)
    #Police d'ecriture et taille d'ecriture
    myfont = pygame.font.SysFont("arial", 20)

#Affichage general
def display ():
    botrect()
    displayPlayer1Rect()
    displayPlayer2Rect()


#Fonction pour le rectangle d'information sur le joueur en haut a gauche (Joueur 1)
def displayPlayer1Rect ():
    pygame.draw.rect(screen,black,(20,10,450,245),2)
    myfont = pygame.font.SysFont("arial", 20)
    #Ligne 1
    label = myfont.render("Joueur 1 (Pion Rouge):"+str(nom[0]), 10, (0,0,0))
    screen.blit(label, (40, 20))
    #Ligne 2
    label2 = myfont.render("Vous avez : "+str(playerMoney[0])+"€", 10, (0,0,0,))
    screen.blit(label2, (40, 50))
    #Ligne 3
    label3 = myfont.render("Place sur le plateau :"+plateName[playerPosition[0]], 10, (0,0,0))
    screen.blit(label3, (40, 80))
    #Ligne 4
    label4 = myfont.render("Nombre de propriété pocédée : "+str(nPropPlayer[0]), 10, (0,0,0))
    screen.blit(label4, (40, 110))
    #Ligne 5
    label5 = myfont.render("Ce joueur possede une carte sortie de prison : "+str(cardJailPlayer[0]), 10, (0,0,0))
    screen.blit(label5, (40, 140))


#Fonction pour le rectangle d'information sur le joueur en bas a gauche (Joueur 2)
def displayPlayer2Rect ():
    pygame.draw.rect(screen,black,(20,265,450,245),2)
    myfont = pygame.font.SysFont("arial", 20)
    #Ligne 1
    label = myfont.render("Joueur 2 (Pion Noir):"+str(nom[1]), 10, (0,0,0))
    screen.blit(label, (40, 275))
    #Ligne 2
    label2 = myfont.render("Vous avez : "+str(playerMoney[1])+"€", 10, (0,0,0,))
    screen.blit(label2, (40, 305))
    #Ligne 3
    label3 = myfont.render("Place sur le plateau :"+plateName[playerPosition[1]], 10, (0,0,0))
    screen.blit(label3, (40, 335))
    #Ligne 4
    label4 = myfont.render("Nombre de propriété pocédée : "+str(nPropPlayer[1]), 10, (0,0,0))
    screen.blit(label4, (40, 365))
    #Ligne 5
    label5 = myfont.render("Ce joueur possede une carte sortie de prison : "+str(cardJailPlayer[1]), 10, (0,0,0))
    screen.blit(label5, (40, 395))

j=0

#Boucle du jeu
#commencement de la boule du jeu
while game :

    gameTour = gameTour + 1     # gain d'une unité par tour

    for event in pygame.event.get():      #lance une liste de tous les évenement

        if event.type == pygame.QUIT :    #si on clique sur la croix de la fenètre

            sys.exit()          #ferme le programme

    if j==0:        # remet le tour a zero (premier joueur)
        i=1
    elif j==1:      # permet de ne plus continuer le jeu
        i=3

    while i < 3:    #sert a recomencer le tour après la fin du deriner quand i etait > 2

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:      #Si clique sur la souris

                    printText = 0       #initialisation de la variable pour ne pas réécrire le meme text que le tour d'avant si aucun texte d'écrit
                    tour = 1            #initialisation de la variable pour lancer le tour après la boucle de pré-lancement

                    lapsPrison()        #fonction qui gère les tours en prison

                    if doubleForPrison == 2:  #si trois double le joueur va en prison
                        doubleForPrison = 0   #reset du nombre de double
                        playerPosition[i-1]=10   #le joueur va en prison
                        lapsInPri[i-1] = 3    #reste 3 tour en prison
                        tour = 0

                        screen.fill(white)      # met un fond blanc
                        screen.blit(img_menu,(750-260,0))   # met l'image du plateau
                        screen.blit(logo,(0,0)) #met l'image du logo Monocity

                        for j in range(0,nPlayer):      # dessine tous les points correspondant aux joueurs
                            pygame.draw.circle(screen,colour[j],(x[playerPosition[j]],y[playerPosition[j]]),9)

                        display() #affiche tous les rectangles
                        pygame.display.flip()       # permet d'afficher sur l'ecran toute les demandes de dessus
                        i=i+1                       # permet de passer au joueur suivant
                        stop = input("c'est la fin de la parti")       # affiche une fenètre pour permettre au joueur suivant de ne pas être bousculé

                    if tour == 1:

                       #Lancement des des + changement de la position du joueur
                        diceRoll()
                        playerPosition[i-1] = playerPosition[i-1] + totalDice
                        print(playerPosition[i-1],"numero",i-1)
                        startTurnAgaine()

                        #Suppression et affichage du nouveau point du joueur
                        screen.fill(white)
                        screen.blit(img_menu,(750-260,0))
                        screen.blit(logo,(0,0))

                        for j in range(0,nPlayer):
                            pygame.draw.circle(screen,colour[j],(x[playerPosition[j]],y[playerPosition[j]]),9)

                        display()
                        pygame.display.flip()

                        # lance toute les fonction correspondant aux cases
                        taxeProp()
                        startCase()
                        testCase()
                        speCase()
                        printTextFon()
                        pygame.display.flip()

                        #Suppression et affichage du nouveau point + affichage du texte dans le rectangle du bas
                        screen.fill(white)
                        screen.blit(img_menu,(750-260,0))
                        screen.blit(logo,(0,0))

                        for j in range(0,nPlayer):
                            pygame.draw.circle(screen,colour[j],(x[playerPosition[j]],y[playerPosition[j]]),9)

                        pygame.display.flip()

                        testCase2()
                        printTextFon()
                        questionEnd()

                        display()
                        pygame.display.flip()

                        #boucle permetant de savoir si on fait un double et de rejouer
                        if dice2 == dice1:
                            i = i
                            doubleForPrison = doubleForPrison + 1
                            stop = input("C'est la fin de ton tour")
                        else:
                            i = i+1
                            doubleForPrison = 0
                            stop = input("C'est la fin de ton tour")

                        #variable pour tester une des fin possible
                        testFin = (gameTour >= 100) or (playerMoney[0] <= 0) or (playerMoney[1] <= 0)
                        j=0
    os.system("cls")
    if (testFin) :

        #Suppression et affichage du nouveau point du joueur
        screen.fill(white)
        screen.blit(img_menu,(750-260,0))
        screen.blit(logo,(0,0))
        pygame.draw.circle(screen,red,(197,1578),3)
        display()

        for j in range(0,nPlayer):
            pygame.draw.circle(screen,colour[j],(x[playerPosition[j]],y[playerPosition[j]]),9)

        pygame.display.flip()
        myfont = pygame.font.SysFont("arial", 20)
        label = myfont.render("La partie est terminée !!", 10, (0,0,0))
        screen.blit(label, (40, 540))

        pygame.display.flip()

        j=1

        stop = input("c'est la fin de la parti")

        sys.exit()

clock.tick(60)