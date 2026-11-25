import numpy as np
M=np.array([[1,2,3],[4,5,6],[7,8,9]])
Pi=[1,2,3]

def score(Pi,M):
    s=0
    n=len(Pi)
    for i in range(n):
        for j in range (i+1,n):
            indice_i=Pi[i]-1
            indice_j=Pi[j]-1
            s+=M[indice_i,indice_j]
    return s


def echange(Pi,M):
    meilleur_score=score(Pi,M)
    meilleure_solution=Pi

    for i in range(len(Pi)):
        for j in range(len(Pi)):
            Pi[i],Pi[j]=Pi[j],Pi[i]
            score_permutation=score(Pi,M)
            if score_permutation>meilleur_score:
                meilleur_score=score_permutation
                meilleure_solution=Pi.copy()
            Pi[i],Pi[j]=Pi[j],Pi[i]
    
    return meilleure_solution,meilleur_score

print(echange(Pi,M))