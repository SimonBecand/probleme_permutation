from score import score


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