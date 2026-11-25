import numpy as np
from numpy import inf 
from numpy import random
import random





INSTANCES = {
    "D1_n9": {
        "C": np.array([
            [0, 47, 35, 35, 52, 14, 0, 43, 50],
            [47, 0, 14, 13, 98, 44, 71, 43, 30],
            [21, 80, 0, 5, 0, 83, 60, 63, 81],
            [19, 86, 39, 0, 11, 16, 53, 89, 45],
            [30, 70, 70, 51, 0, 22, 56, 86, 60],
            [4, 94, 52, 12, 22, 0, 29, 30, 88],
            [3, 14, 14, 84, 10, 79, 0, 57, 51],
            [34, 31, 61, 99, 15, 63, 83, 0, 25],
            [52, 0, 91, 48, 35, 8, 26, 65, 0],
        ], dtype=int),
        "optimal_permutation": [0, 4, 3, 2, 1, 7, 6, 5, 8],
        "optimal_value": 1963,
        "static_greedy_permutation": [np.int64(4), np.int64(0), np.int64(2), np.int64(3), np.int64(5), np.int64(1), np.int64(7), np.int64(6), np.int64(8)],
        "static_greedy_value": 1874,
        "dynamic_greedy_permutation": [4, 2, 5, 1, 6, 8, 0, 7, 3],
        "dynamic_greedy_value": 1836,
    },
    "D2_n9": {
        "C": np.array([
            [0, 28, 33, 59, 43, 66, 38, 58, 32],
            [62, 0, 23, 68, 80, 34, 60, 11, 96],
            [98, 49, 0, 40, 20, 69, 29, 90, 38],
            [87, 44, 70, 0, 40, 22, 28, 93, 90],
            [19, 70, 38, 21, 0, 62, 97, 81, 74],
            [74, 40, 28, 4, 50, 0, 81, 11, 99],
            [6, 65, 30, 55, 55, 42, 0, 16, 6],
            [38, 13, 39, 71, 64, 2, 18, 0, 56],
            [19, 74, 12, 72, 35, 81, 20, 69, 0],
        ], dtype=int),
        "optimal_permutation": [3, 2, 5, 1, 0, 4, 8, 7, 6],
        "optimal_value": 2061,
        "static_greedy_permutation": [np.int64(2), np.int64(3), np.int64(4), np.int64(1), np.int64(5), np.int64(0), np.int64(6), np.int64(8), np.int64(7)],
        "static_greedy_value": 1987,
        "dynamic_greedy_permutation": [2, 1, 3, 4, 5, 0, 8, 7, 6],
        "dynamic_greedy_value": 2037,
    },
    "D3_n10": {
        "C": np.array([
            [0, 40, 2, 85, 90, 18, 8, 17, 88, 84],
            [75, 0, 35, 91, 56, 61, 51, 88, 2, 45],
            [87, 14, 0, 44, 7, 27, 18, 74, 31, 67],
            [40, 22, 10, 0, 96, 63, 7, 93, 25, 21],
            [0, 76, 97, 46, 0, 70, 53, 25, 8, 95],
            [90, 4, 14, 38, 29, 0, 68, 43, 16, 65],
            [57, 75, 32, 19, 32, 56, 0, 22, 45, 89],
            [89, 30, 14, 8, 32, 90, 79, 0, 59, 74],
            [81, 89, 93, 95, 47, 68, 87, 78, 0, 96],
            [5, 47, 80, 40, 52, 59, 31, 13, 6, 0],
        ], dtype=int),
        "optimal_permutation": [8, 4, 1, 2, 3, 7, 5, 6, 0, 9],
        "optimal_value": 2968,
        "static_greedy_permutation": [np.int64(8), np.int64(1), np.int64(4), np.int64(6), np.int64(7), np.int64(2), np.int64(3), np.int64(0), np.int64(5), np.int64(9)],
        "static_greedy_value": 2688,
        "dynamic_greedy_permutation": [8, 1, 7, 6, 0, 4, 2, 9, 3, 5],
        "dynamic_greedy_value": 2794,
    },
    "D4_n10": {
        "C": np.array([
            [0, 63, 13, 58, 77, 51, 62, 58, 31, 91],
            [67, 0, 65, 99, 41, 69, 16, 28, 30, 2],
            [30, 95, 0, 0, 98, 7, 79, 14, 56, 25],
            [55, 85, 31, 0, 27, 87, 25, 42, 54, 29],
            [4, 16, 87, 93, 0, 12, 12, 79, 52, 83],
            [93, 92, 52, 4, 3, 0, 72, 36, 69, 17],
            [1, 90, 41, 68, 54, 60, 0, 98, 2, 62],
            [86, 1, 42, 47, 55, 62, 33, 0, 69, 5],
            [57, 93, 21, 88, 94, 80, 11, 11, 0, 71],
            [16, 96, 39, 53, 9, 75, 55, 96, 57, 0],
        ], dtype=int),
        "optimal_permutation": [2, 8, 0, 6, 4, 9, 1, 7, 3, 5],
        "optimal_value": 2796,
        "static_greedy_permutation": [np.int64(6), np.int64(9), np.int64(8), np.int64(0), np.int64(2), np.int64(4), np.int64(7), np.int64(5), np.int64(3), np.int64(1)],
        "static_greedy_value": 2386,
        "dynamic_greedy_permutation": [6, 9, 7, 8, 3, 5, 2, 0, 1, 4],
        "dynamic_greedy_value": 2641,
    },
    "D5_n11": {
        "C": np.array([
            [0, 40, 72, 40, 48, 48, 11, 78, 73, 54, 16],
            [61, 0, 66, 1, 77, 51, 99, 24, 32, 1, 90],
            [22, 79, 0, 37, 44, 64, 53, 44, 40, 57, 58],
            [96, 20, 19, 0, 62, 60, 1, 79, 85, 79, 42],
            [43, 64, 92, 50, 0, 88, 16, 77, 58, 96, 21],
            [84, 29, 4, 45, 15, 0, 74, 33, 34, 84, 18],
            [73, 30, 37, 71, 55, 69, 0, 38, 22, 57, 33],
            [92, 99, 43, 33, 96, 65, 35, 0, 62, 29, 23],
            [81, 73, 64, 83, 55, 90, 22, 98, 0, 36, 57],
            [59, 91, 8, 99, 53, 49, 96, 80, 35, 0, 21],
            [87, 44, 31, 80, 69, 39, 43, 67, 82, 60, 0],
        ], dtype=int),
        "optimal_permutation": [10, 4, 8, 2, 9, 3, 7, 1, 5, 6, 0],
        "optimal_value": 3552,
        "static_greedy_permutation": [np.int64(10), np.int64(8), np.int64(2), np.int64(9), np.int64(6), np.int64(4), np.int64(3), np.int64(7), np.int64(1), np.int64(5), np.int64(0)],
        "static_greedy_value": 3496,
        "dynamic_greedy_permutation": [10, 8, 9, 7, 1, 6, 4, 3, 0, 2, 5],
        "dynamic_greedy_value": 3494,
    },
    "D6_n11": {
        "C": np.array([
            [0, 8, 91, 75, 19, 79, 68, 73, 97, 26, 35],
            [65, 0, 68, 28, 91, 46, 79, 33, 55, 64, 3],
            [15, 98, 0, 69, 14, 99, 55, 49, 57, 15, 18],
            [45, 39, 51, 0, 40, 97, 17, 97, 43, 66, 80],
            [6, 18, 6, 71, 0, 88, 8, 18, 74, 10, 93],
            [65, 63, 24, 71, 74, 0, 46, 3, 16, 17, 37],
            [22, 3, 68, 91, 64, 83, 0, 68, 77, 86, 78],
            [69, 81, 1, 10, 66, 17, 80, 0, 33, 10, 89],
            [27, 57, 53, 42, 11, 12, 78, 58, 0, 49, 9],
            [6, 68, 14, 61, 81, 55, 62, 88, 75, 0, 57],
            [62, 75, 64, 32, 43, 59, 17, 20, 53, 32, 0],
        ], dtype=int),
        "optimal_permutation": [1, 0, 6, 2, 3, 9, 7, 4, 10, 5, 8],
        "optimal_value": 3398,
        "static_greedy_permutation": [np.int64(9), np.int64(0), np.int64(6), np.int64(2), np.int64(3), np.int64(1), np.int64(10), np.int64(7), np.int64(4), np.int64(8), np.int64(5)],
        "static_greedy_value": 3137,
        "dynamic_greedy_permutation": [9, 0, 6, 2, 3, 7, 10, 1, 4, 5, 8],
        "dynamic_greedy_value": 3330,
    },
    "D7_n12": {
        "C": np.array([
            [0, 73, 25, 7, 0, 50, 23, 83, 78, 97, 76, 41],
            [72, 0, 89, 26, 19, 71, 92, 36, 21, 59, 76, 5],
            [54, 96, 0, 90, 89, 30, 81, 63, 61, 97, 42, 35],
            [13, 95, 18, 0, 29, 26, 66, 66, 48, 34, 58, 73],
            [18, 28, 27, 0, 0, 60, 12, 69, 61, 22, 84, 52],
            [77, 92, 15, 31, 57, 0, 18, 47, 54, 11, 30, 78],
            [78, 96, 51, 68, 49, 4, 0, 51, 1, 62, 26, 94],
            [38, 78, 62, 20, 53, 93, 37, 0, 59, 16, 5, 76],
            [7, 11, 82, 50, 21, 96, 28, 24, 0, 23, 30, 66],
            [49, 7, 93, 8, 6, 69, 91, 84, 75, 0, 9, 75],
            [97, 11, 51, 47, 12, 68, 21, 91, 28, 71, 0, 17],
            [40, 65, 62, 16, 37, 6, 52, 4, 75, 57, 80, 0],
        ], dtype=int),
        "optimal_permutation": [2, 6, 3, 4, 1, 10, 0, 9, 7, 8, 5, 11],
        "optimal_value": 3935,
        "static_greedy_permutation": [np.int64(3), np.int64(2), np.int64(4), np.int64(6), np.int64(9), np.int64(0), np.int64(10), np.int64(5), np.int64(7), np.int64(1), np.int64(11), np.int64(8)],
        "static_greedy_value": 3561,
        "dynamic_greedy_permutation": [2, 3, 4, 10, 9, 7, 5, 6, 0, 11, 1, 8],
        "dynamic_greedy_value": 3828,
    },
    "D8_n12": {
        "C": np.array([
            [0, 99, 38, 65, 89, 48, 87, 75, 50, 35, 86, 36],
            [29, 0, 35, 38, 95, 74, 42, 16, 10, 46, 73, 46],
            [0, 55, 0, 2, 70, 8, 2, 91, 76, 97, 61, 44],
            [43, 7, 14, 0, 92, 67, 81, 21, 3, 35, 66, 33],
            [34, 75, 13, 59, 0, 70, 27, 64, 34, 39, 71, 52],
            [86, 99, 23, 35, 48, 0, 84, 15, 73, 87, 13, 87],
            [98, 35, 59, 71, 21, 96, 0, 21, 87, 11, 55, 41],
            [4, 23, 92, 91, 86, 6, 49, 0, 42, 36, 72, 12],
            [48, 75, 12, 11, 18, 81, 43, 71, 0, 38, 56, 39],
            [38, 82, 65, 4, 8, 59, 80, 42, 66, 0, 66, 6],
            [54, 77, 0, 25, 86, 95, 81, 66, 28, 98, 0, 9],
            [6, 29, 83, 19, 45, 55, 94, 74, 65, 8, 93, 0],
        ], dtype=int),
        "optimal_permutation": [0, 11, 7, 3, 2, 10, 4, 5, 9, 6, 8, 1],
        "optimal_value": 3982,
        "static_greedy_permutation": [np.int64(0), np.int64(11), np.int64(2), np.int64(3), np.int64(5), np.int64(9), np.int64(8), np.int64(7), np.int64(6), np.int64(10), np.int64(4), np.int64(1)],
        "static_greedy_value": 3712,
        "dynamic_greedy_permutation": [0, 11, 2, 7, 3, 10, 9, 6, 8, 5, 1, 4],
        "dynamic_greedy_value": 3906,
    },
}

def objective(C, permutation):
    n = len(permutation)
    return sum(int(C[permutation[i], permutation[j]]) for i in range(n) for j in range(i+1,n))



M_original2=np.array([[1,2,3,],
   [4,5,6],
   [7,8,9]])

M_original=np.array([[1,2,3,4,5],
                     [6,7,8,9,10],
                     [11,12,13,14,15],
                     [16,17,18,19,20],
                     [21,22,23,24,25]])








def score(Pi,M):
    s=0
    n=len(Pi)
    for i in range(n):
        for j in range (i+1,n):
            indice_i=Pi[i]-1
            indice_j=Pi[j]-1
            s+=M[indice_i,indice_j]
    return s


def glouton(M):
    dictionnaire_score = {}
    for i in range (len(M)):
        numero_colonne = M[i,i]
        ligne = M[i,:]
        colonne = M[:,i]
        dictionnaire_score[numero_colonne]=0
        for j in range (len(M)):
            if j != i:
                dictionnaire_score[numero_colonne] += ligne[j] - colonne[j]
    for cle in dictionnaire_score:
        min= dictionnaire_score[cle]
        max= dictionnaire_score[cle]
        break
    for cle in dictionnaire_score:
        if dictionnaire_score[cle] < min:
            min = dictionnaire_score[cle]
        if dictionnaire_score[cle] > max:
            max = dictionnaire_score[cle]
    
    if max == min:
        for cle in dictionnaire_score:
            dictionnaire_score[cle] = 1

    else:
        for cle in dictionnaire_score:
            dictionnaire_score[cle] = (
                dictionnaire_score[cle] - min
            ) / (max - min)

    return dictionnaire_score 

def modification_apres_choix(M,copyP,c):

    for i in range (len(M)):
        if M[i,i] == c:
            colonne = i
            break

    M[[0, colonne], :] = M[[colonne, 0], :]
    M[:, [0, colonne]] = M[:, [colonne, 0]]
    M = np.delete(M, 0, axis=0)
    M = np.delete(M, 0, axis=1)

    for i in range (len(copyP)):
        if copyP[i,i] == c:
            colonne = i
            break

    copyP = np.delete(copyP, colonne, axis=0)
    copyP = np.delete(copyP, colonne, axis=1)

    return M,copyP


def choix_prochaine_colonne(M,P,alpha,beta):
    score1=glouton(M)
    score2=score_pheromones(P)

    candidat = list(score1.keys())

    if len(candidat) == 1:
        return candidat[0]

    poids = []

    for c in candidat :
        poids.append((score1[c]**beta)*(score2[c]**alpha))

    colonne = random.choices(candidat, weights=poids, k=1)[0]
    return colonne





def ajout_pheromones(liste_pi,P,gamma,M):
    """
    Pi: Matrice numpi de solutions
    P: Matrice numpi de phéromone
    gamma: float entre 0 et 1, taux d'evaporation
    Return: 
    meilleur_score:float, valeur du meilleur score
    meilleur_pi: tableau numpi, meilleur permutation de la génération
    Modifie la matrice de phéromone en fonction des résultat de la génération de fourmis
    """
    #Evaporation
    P=gamma*P



    #Ajout des nouvelles phéromones
    meilleur_score=score(liste_pi[0],M)
    meilleur_pi=liste_pi[0]

    for pi in liste_pi:
        score_pi=score(pi,M)
        for i in range(len(pi)):
            for j in range(i+1,(len(pi))):
                P[pi[i]-1,pi[j]-1]+=score_pi
        if score_pi > meilleur_score:
            meilleur_score=score_pi
            meilleur_pi=pi
        #Renumerotation des lignes et colonnes
    for i in range(len(P)):
        P[i][i]=int(i+1)
    return P,meilleur_score,meilleur_pi

def score_pheromones(Copie_P):
    """
    Copie_P: matrice de pheromone partielle
    Return: 
    dico_score_pheromone: un dictionnaire avec les numéros de colonne liés avec leur score respectif
    """
    score_tot=0
    dico_score_pheromone={}
    #Ajout du score
    for i in range(len(Copie_P)):
        score_partiel=0
        indice=0
        for j in range(len(Copie_P)):
            if i==j:
                indice=Copie_P[i][j]
            else:
                score_partiel+=Copie_P[i][j]
                score_tot+=Copie_P[i][j]
        dico_score_pheromone[indice]=score_partiel
    #Normalisation du score
    for indice in dico_score_pheromone.keys():
        if score_tot == 0:
            for indice in dico_score_pheromone:
                dico_score_pheromone[indice] = 1 / len(Copie_P)

        else:
            for indice in dico_score_pheromone:
                dico_score_pheromone[indice] /= score_tot
    return dico_score_pheromone

"""     
liste_pi=np.array([[1,2,3],[1,2,3],[2,3,1]])
P=np.array([[1,1,1],[1,2,1],[1,1,3]])

P,meilleur_score,meilleur_pi=ajout_pheromones(liste_pi,P,gamma=0.5)
print(P)
print(meilleur_pi)
print(meilleur_score)
print(score_pheromones(P))
""" 







def ACO(M_original,n_fourmis,n_iterations,alpha,betha,gamma):

    M_avec_coeff=np.copy(M_original)
    score_max = 0
    best_Pi = []

    for i in range (len(M_avec_coeff)):
        M_avec_coeff[i,i] = i+1

    P = np.ones((len(M_avec_coeff), len(M_avec_coeff)))
    np.fill_diagonal(P, np.arange(1, len(M_avec_coeff)+1))


    for i in range (n_iterations):
        
        Pis=[]

        for f in range (n_fourmis):
            Pi = []
            copyP = np.copy(P)
            M=np.copy(M_avec_coeff)
            while len(Pi) < len(M_original):
                choix_colonne = choix_prochaine_colonne(M,copyP,alpha,betha)
                Pi.append(choix_colonne)
                M,copyP=modification_apres_choix(M,copyP,choix_colonne)
            Pis.append(Pi)

        P,score_fourmis, meilleur_fourmi = ajout_pheromones(Pis,P,gamma,M_original)
        if score_fourmis > score_max:
            score_max = score_fourmis
            best_Pi = meilleur_fourmi


    return best_Pi,score_max



gamma= 0.8
beta=0.6
alpha=0.7
n_fourmis = 1000
n_itération = 100

C = INSTANCES["D8_n12"]["C"]
optimum = INSTANCES["D8_n12"]["optimal_value"]
solution = INSTANCES["D8_n12"]["optimal_permutation"]
PI_np,score_max = ACO(C,n_fourmis,n_itération,alpha,beta,gamma)
PI=liste = [int(x)-1 for x in PI_np]
print("Meilleure permutation trouvée :", PI)
print("Score de la meilleure permutation :", score_max)
print("score théorique optimum :", optimum)

