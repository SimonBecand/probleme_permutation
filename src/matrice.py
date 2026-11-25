import os
import numpy as np

def charger_instance_lop(nom_fichier, dossier="src/instances/groupe_A"):
    """
    Lit un fichier d'instance LOP (taille n sur la 1ère ligne, suivie de la matrice n x n)
    et renvoie la matrice NumPy avec une diagonale nulle.
    """
    chemin = os.path.join(dossier, nom_fichier)
    
    # skiprows=1 permet d'ignorer la première ligne (qui contient la taille '50')
    M = np.loadtxt(chemin, skiprows=1, dtype=int)
    
    # IMPORTANT : On remet la diagonale à 0 car dans ces instances IO,
    # la diagonale contient des flux internes qui fausseraient votre glouton
    np.fill_diagonal(M, 0)
    
    return M

M = charger_instance_lop("instance_001.txt")
print(M)