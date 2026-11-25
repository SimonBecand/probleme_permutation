def score(Pi,M):
    s=0
    n=len(Pi)
    for i in range(n):
        for j in range (i+1,n):
            indice_i=Pi[i]-1
            indice_j=Pi[j]-1
            s+=M[indice_i,indice_j]
    return s