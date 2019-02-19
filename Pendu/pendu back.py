#---------------- Import ------------------
import tkinter
import os
from tkinter.constants import *
from random import randint
#---------------- Variable non changée ------------------
liste = ["adresse","appartement","ascenseur","balcon","boucherie","boulanger","boulangerie","boutique","bus","caniveau","caravane","carrefour","cave","charcuterie","cinéma","cirque","clin d’oeil","cloche","clocher","clown","coiffeur","colis-route","courrier","croix","église","embouteillage","endroit","enveloppe","essence","facteur","fleuriste","foire","hôpital","hôtel","immeuble","incendie","laisse","magasin","manège","médicament","moineau","monde","monument","ouvrier","palais","panneau","paquet","parc","passage","pharmacie","pharmacien","piscine","place","police","policier","pompier","poste","promenade","quartier","square","timbre","travaux","usine","village","ville","voisin","volet"]
lettre = {"a" : 1, "à" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5 ,"é" : 5,"è" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10, "k" : 11, "m" : 12, "l" : 13, "n" : 14, "o" :15 ,"ô" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20, "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26, "-": 27, "'" : 27, " " : 27}
repo = ["y","n"]
symb = ["'","-"]
rejouer = 1
#---------------- Fonctions ------------------
def nberror(error):
    if error == 0:
        print("Tu n'as encore fait aucune erreur")
    elif error == 1:
        print("Tu as fais une erreur")
    else:
        print("Tu as fais", error ,"erreurs")

def cls():
    os.system("cls")

def retry():
    global choixLettre
    global testV
    try:
        (lettre[choixLettre] not in lettre.values()) or (lettre[choixLettre] in lettreProp)
    except:
        print("Ce qui a été saisie n'est pas une lettre")
        choixLettre = str(input("Choisir une Lettre : "))
        choixLettre.lower()
    else :
        testV = 1
#---------------- Commencement du programme ------------------
while rejouer == 1 :
#---------------- Variable changée ------------------
    error = 0
    lettrepro = 0
    test = 0
    testrep = 0
    tour = 0
    motEpel= []
    valuesMot = []
    motIncomp = []
    lettreProp = []
    lettrePropL = []
    motChoisi =""
    motChEpel =[]
#---------------- Choix du mot random ------------------
    chiffreRand = randint(0,32)

    motRand = liste[chiffreRand]
#---------------- Remplissage de la variable (motImcomp) avec un mot incomplet, avec des espaces vides sauf pour les symboles ------------------
    for i in range(0,len(motRand)):
        motEpel.append(motRand[i])
        if motRand[i] in symb :
            motIncomp.append(motRand[i])
        else :
            motIncomp.append(" ")
#---------------- Remplissage de la variable (valuesMot) avec une suite de valeur correspondant à la valeur des lettres dans le dico (lettre) ------------------
    for i in range(0,len(motRand)):
        valuesMot.append(lettre[motEpel[i]])
#---------------- Test pour rentrer et continuer le jeu ------------------
    while error < 11 and test == 0 :
#---------------- Ajout de tour pour l'affichage ------------------
        tour += 1
        if tour == 1:
            print("Le mot à trouver est un mot de" , len(motRand) , "lettres")
        else :
            print("Mot de :" , len(motRand), "lettres")
            print("Lettre déjà proposée :",lettrePropL)
            print("Le mot ressemble à :", motIncomp)
#---------------- Choix d'une lettre ------------------
        choixLettre = str(input("Choisir une Lettre : "))
#---------------- Suppression des bugs du aux majuscules grâce au .lower() ------------------
        choixLettre = choixLettre.lower()
#---------------- Reset du test pour la validation de la lettre choisie ------------------
        testV = 0
#---------------- Test de debug si la saisie n'est pas une lettre ------------------
        while testV == 0 :
            retry()
#---------------- Reset du test pour la validation de la lettre choisie ------------------
        testT = 0
#---------------- Test de la validation de la lettre choisie ------------------
        while testT == 0 :
#---------------- Test si la lettre n'a jamais été saisie et si c'est bien une lettre pour pouvoir l'ajouter à la liste de lettre proposée (lettreProp) sous forme de nombre ------------------
            if (lettre[choixLettre] not in lettre.values()) or (lettre[choixLettre] in lettreProp) :
                testl = 1
                while testl == 1 :
                    testV = 0
                    while testV == 0:
                        retry()
                    if lettre[choixLettre] in lettreProp :
                        print("La lettre choisie a déjà été saisie aupart avant")
                        choixLettre = str(input("Choisir une Lettre : "))
                        choixLettre = choixLettre.lower()
                    elif lettre[choixLettre] not in lettre.values() :
                        print("La lettre écrite n'éxiste pas")
                        choixLettre = str(input("Choisir une Lettre : "))
                        choixLettre = choixLettre.lower()
                    else :
                        testl = 0
            else :
                lettreProp.append(lettre[choixLettre])
                lettrePropL.append(choixLettre)
                testT = 1
#---------------- Test si la lettre est dans le mot avec la valeur de la lettre ------------------
        if lettre[choixLettre] in valuesMot:
#---------------- Verification du pluriel dans l'affichage ------------------
            if valuesMot.count(lettre[choixLettre]) == 1:
                print("La lettre choisie correspond à une lettre du mot")
            else :
                print("La lettre choisie correspond à" , valuesMot.count(lettre[choixLettre]) , "lettres du mot")
#---------------- Ajout de la lettre trouvée dans le mot incomplet ------------------
            for i in range(0,len(motRand)):
                if valuesMot[i] == lettre[choixLettre] :
                    motIncomp[i] = choixLettre
            print (motIncomp)
#---------------- Ajout d'une erreur si la lettre n'est pas dans le mot ------------------
        else :
            print("La lettre choisie ne correspond à aucune lettre du mot")
            error += 1
#---------------- Demmande de choix d'un mot ------------------
        rep = str(input("Veux-tu choisir un mot ? (y/n) "))
        rep = rep.lower()
#---------------- Test pour voir si la réponse est bien l'une de celles proposée ------------------
        while rep not in repo :
            print ("La réponse n'est pas une réponse valable")
            rep = str(input("Veux-tu choisir un mot ? (y/n) "))
            rep = rep.lower()
#---------------- Si oui ------------------
        if rep == "y":
#---------------- Choix d'un mot, transformation du mot en nombre puis insertion dans un tableau avec test de debug ------------------
            motChEpel = []
            motChoisi = input("Choisir un mot : ")
            motChoisi= motChoisi.lower()
            while motChoisi == "":
                motChoisi = input("Choisir un mot : ")
                motChoisi = motChoisi.lower()
            testI = 0
            while testI == 0:
                try:
                    for i in range(0,len(motRand)):
                        motChEpel.append(lettre[motChoisi[i]])
                except:
                    print("Le mot choisi n'est pas un mot valable")
                    motChoisi = input("Choisir un autre mot : ")
                    motChoisi = motChoisi.lower()
                else:
                    testI = 1
#---------------- Test de concordance entre le mot choisi et le mot random ------------------
            if motChEpel == valuesMot :
                print("Bravo, le bon mot a été touvé")
                test = 1
                cls()
#---------------- ajout d'une erreur si le mot n'est pas le bon et affichage du nombre d'erreur via la fonction (nberror) ------------------
            else :
                print("Ce n'est pas le bon mot")
                error += 1
                cls()
                nberror(error)
#---------------- Si non affichage du nombre d'erreur via la fonction (nberror) ------------------
        else :
            cls()
            nberror(error)
#---------------- Si nombre d'erreur max atteint, fin du jeu et affichage du mot à trouver ------------------
        if error == 11 :
            print("Tu as perdu, le mot étais : ", motRand)
#---------------- Demmande pour rejouer ------------------
    rep2 = str(input("Veux-tu rejouer ? (y/n) "))
    rep2 = rep2.lower()
#---------------- Test pour voir si la réponse est bien l'une de celles proposée ------------------
    while rep2 not in repo :
        print ("La réponse n'est pas une reponse valable")
        rep2 = str(input("Veux-tu rejouer ? (y/n) "))
        rep2 = rep2.lower()
#---------------- Si oui ------------------
    if rep2 == "y":
        print("Le jeu recommence !")
        input("Appuis sur entrer pour rejouer ! ")
        cls()
#---------------- Si non, parammètre de la boucle du jeu passe a false, le jeux s'arrète ------------------
    else :
        print("Vous avez terminer de jouer")
        rejouer= 0

print("Jeu codé par Corentin Fouquet")
