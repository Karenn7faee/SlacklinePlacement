# Autor : Karen-Fae Laurin


# ----------------------- Devoir 1 -----------------------------------------
# Ce programme implémente un algorithme glouton qui retourne un ensemble 
# d'arrêtes qui représente des positions de slackline dans un parc selon
# l'emplacement des arbres sans croissement afin de maximiser la distance
# sans être optimal.
# --------------------------------------------------------------------------

import sys
import math
import time
startTime = time.time()

# ----------------------------------------------------------
# fonctions additionnelles
# ----------------------------------------------------------

# renvoie la distance entre 2 points
def distance(p1, p2):
    return math.sqrt( (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 )

# 2 prochaines fonctions provenant de : https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
# permet de vérifier si deux segments s'intersecte

# verifie si 3 points sont placé en ordre anti-horaire
def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

# ----------------------------------------------------------
# paramètres de base 
# ----------------------------------------------------------

dictArbre = {}			        # clé: valeur
							    # arbre#id   : [coordX, coordY, DHP]

dictArretes = {}                # arrete_i_j : distance(i,j)

dictSolution = {}				# solution
                                # arrete_i_j : distance(i,j)


# ----------------------------------------------------------
# Ouverture du fichier (command file.txt)
# ----------------------------------------------------------

fileSource = str(sys.argv[1])

#fileSource = str(sys.argv[1])
file = open(fileSource, "r")
line = file.readline()      #skip entête du fichier 

# initialiser dictionnaire source
id = 0
for line in file:
    ligne = line.strip().split(",")
    id += 1

    # Ajoute seulement les arbres avec un troncs de 25cm et plus
    if (float(ligne[14]) >= 25):    
        cle = "arbre" + str(id)                     # id arbre
        valeur = [float(ligne[8]), float(ligne[9])] # info arbre
        dictArbre[cle] = valeur                     # ajout a la dictSource
                                                    # clé : valeur 
                                                    # arbre#id : [coordX, coordY]


print("num of trees in parc :", len(dictArbre))
# ------------------------------------------------------------
# innitialiser le dictionnaire d'arrête valide donc de longueur entre 5 et 30m inclus
# ----------------------------------------------------------

for arbre1 in dictArbre:
    start = False

    for arbre2 in dictArbre:
        # ne pas recalculer les mêmes distances entre deux arbres (i,j) et (j,i) => seulement (i,j)
        if(start == False and arbre1 == arbre2):
            start = True
            continue

        # calcule la distance entre 2 arbres
        if(start == True):
            p1 = dictArbre[arbre1]
            p2 = dictArbre[arbre2]
            

            distance2Arbres = distance(p1, p2)

            # ne considère que les segments qui sont entre 5 et 30m
            if (distance2Arbres >= 5 and distance2Arbres <= 30):
                cle = "arrete_"+arbre1[5:]+"_"+arbre2[5:]
                dictArretes[cle] = distance2Arbres
                                      
print("num of possible slacklines :", len(dictArretes)) 

# ------------------------------------------------------------
# selection des candidats valides
# ----------------------------------------------------------

for arrete in dictArretes:
    ids = arrete.split("_")
    arbre1 = "arbre" + ids[1]
    arbre2 = "arbre" + ids[2]

    
    # verifie si l'arrete cause un intersection avec les arretes dans la solution
    ajout = True
    for arreteSol in dictSolution:
        ids = arreteSol.split("_")
        arbre1Test = "arbre" + ids[1]
        arbre2Test = "arbre" + ids[2]

        # eviter les erreurs flottantes, si le premier arbre est le même sur les deux arretes alors il n'y pas de croissement
        if (arbre1 == arbre1Test or arbre1 == arbre2Test) : continue

        # si intersection ne pas l'ajouter
        estInter = intersect(dictArbre[arbre1], dictArbre[arbre2], dictArbre[arbre1Test], dictArbre[arbre2Test] )
        if (estInter) : 
            ajout = False
            break
    

    if (ajout) : dictSolution[arrete] = dictArretes[arrete]

print("--- execution time  : %s seconds ---" % (time.time() - startTime))

# -------------------------------------------------------------
# Output dans le fichier dans (resultat_file.csv)
# ----------------------------------------------------------

outputFile = open("resultat_"+fileSource, "w")
resultat = ""

distanceMax = 0 
for arrete in dictSolution:
    distanceMax += dictSolution[arrete]
    ids = arrete.split("_")
    resultat += ids[1] + " " + ids[2] + "\n"

outputFile.write(resultat)
outputFile.close()


print("final distance covered :", distanceMax )
print("num of slacklines in solution :", len(dictSolution))