from score import score

def recherche_local_insertion(M,Pi):
    for i in range(len(Pi)):
        for j in range(len(Pi)):
            if i<j:
                numero_insere= Pi[i]
                for l in range (i,j):
                    Pi[l]=Pi[l+1]
                Pi[j]=numero_insere
            
            elif j>i:
                numero_insere =Pi[i]
                for l in range(i,j,-1):
                    Pi[l]=Pi[l-1]
                Pi[j]=numero_insere
            

    return meilleur_voisin

Pi=[2,4,3,1,6,7,8]
i=5
j=1
numero_insere =Pi[i]
for l in range(i,j,-1):
    Pi[l]=Pi[l-1]
Pi[j]=numero_insere


print(Pi)
    
    
    
    
    
    
    
    
    
    