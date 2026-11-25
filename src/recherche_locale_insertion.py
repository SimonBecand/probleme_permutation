from score import score
import numpy as np
from numpy import inf 
from numpy import random
import random

def recherche_local_insertion(Pi_original,M):
    best=score(Pi_original,M)
    best_Pi=Pi_original
    for i in range(len(Pi_original)):
        for j in range(len(Pi_original)):
            Pi= Pi_original.copy()
            if i<j:
                numero_insere= Pi[i]
                for l in range (i,j):
                    Pi[l]=Pi[l+1]
                Pi[j]=numero_insere
            
            elif i>j:
                numero_insere =Pi[i]
                for l in range(i,j,-1):
                    Pi[l]=Pi[l-1]
                Pi[j]=numero_insere

            score_Pi=score(Pi,M)
            if score_Pi>best:
                best=score_Pi
                best_Pi=Pi

    return best_Pi,best




    
    
    
    
    
    
    
    
    
    