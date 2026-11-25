import numpy as np
import random
from recherche_locale_insertion import recherche_local_insertion
from recherche_locale_permutation import echange



def grasp(M_original,nb_iterations):
    N=len(M_original)#taille de la matrice
    meilleur_score=-np.inf
    meilleur_pi=[np.nan for _ in range(N)]
    for i in range(nb_iterations):
        pi=random.sample(range(1, N+1), N)
        s=+np.inf
        
        while score(pi,M_original)<s:
            if recherche_local_insertion(pi,M_original)[1]>echange(pi,M_original)[1]:
                pi,s=recherche_local_insertion(pi,M_original)
            else:
                pi,s=echange(pi,M_original)           
            
        if meilleur_score<s:
            meilleur_score=s
            meilleur_pi=pi
            
    return meilleur_pi,meilleur_score
        
        