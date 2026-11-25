import numpy as np
from numpy import inf 
from numpy import random
import random
from recherche_locale_permutation import echange
from recherche_locale_insertion import recherche_local_insertion
from score import score
from matrice import charger_instance_lop



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







def ACO(M_original,n_fourmis,n_iterations,alpha,betha,gamma,recherche_locale=None):
    '''recherche_locale = ["None","echange","insertion"]
    '''
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
            
            if recherche_locale == "insertion":
                Pi_voisin= recherche_local_insertion(Pi,M_original)(0)
            elif recherche_locale == "echange":
                Pi_voisin = echange(Pi,M_original)(0)
            else:
                Pi_voisin = Pi
            Pis.append(Pi_voisin)

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


