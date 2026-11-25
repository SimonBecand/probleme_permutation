from ACO import ACO


liste_instance=[]





numero_matrice=[]
ACO_liste=[]
Grasp_insertion=[]
Grasp_permutation=[]
i=0
for matrice in liste_instance:
    numero_matrice.append(0)
    ACO_liste.append(ACO(M_original=matrice,n_fourmis=100,n_iterations=50,alpha=0.5,betha=0.5,gamma=0.5,recherche_locale=None)(1))
    





