import numpy as np
import random
from recherche_locale_insertion import recherche_local_insertion
from recherche_locale_permutation import echange



def grasp(M_original,nb_iterations,recherche_locale=None):
    N=len(M_original)#taille de la matrice
    meilleur_score=-np.inf
    meilleur_pi=[np.nan for _ in range(N)]
    for loop in range(nb_iterations):
        pi=random.sample(range(1, N+1), N)
        if recherche_locale=="insertion":
            pi,score=recherche_local_insertion(pi,M_original)
        elif recherche_locale == "echange":
            pi,score=echange(pi,M_original)
         
        if meilleur_score<score:
            meilleur_score=score
            meilleur_pi=pi
        
    return meilleur_pi,meilleur_score
        
        
