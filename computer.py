# COMPUTER

from othellier import Othellier
import copy
import numpy as np

class Computer(Othellier):
    def __init__(self,othellier:Othellier):
        super().__init__()
        self.othellier=othellier
        #Matrice de poids 
        self.points = np.array([
            [100, -20, 10, 5, 5, 10, -20, 100],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [10, -2, 0, 0, 0, 0, -2, 10],
            [5, -2, 1, 1, 1, 1, -2, 5],
            [5, -2, 1, 1, 1, 1, -2, 5],
            [10, -2, 1, 1, 1, 1, -2, 10],
            [-20, -50, -2, -2, -2, -2, -50, -20],
            [100, -20, 10, 5, 5, 10, -20, 100]])
    
    def evaluation(self,othellier:Othellier):
        #Parité des pions
        players_pawn=othellier._countPaws()[othellier.player]
        opp_pawns=othellier._countPaws()[(othellier.player+1)%2]
        diff=players_pawn-opp_pawns
        #Capture des coins
        corners = [(0,0), (0,7), (7,0), (7,7)]
        players_corners = sum(1 for x, y in corners if othellier.othellier_matrix[x,y] == othellier.player)
        opp_corners = sum(1 for x, y in corners if othellier.othellier_matrix[x,y] == (othellier.player+1)%2)
        corners_score = players_corners - opp_corners
        #Calcule à l'aide de la matrice de poids
        position_score = 0
        for i in range(8):
            for j in range(8):
                if othellier.othellier_matrix[i,j] == othellier.player:
                    position_score += self.points[i,j]
                elif othellier.othellier_matrix[i,j] ==(othellier.player+1)%2:
                    position_score -= self.points[i,j]
        #Multiplication en fonction de l'importance de chaque aspect
        score=(0.3*corners_score+0.4*position_score+0.3*diff)
        return score
    
    #algo negamax avec elagage alpha beta
    def minimax(self,othellier:Othellier,profondeur,alpha=float('-inf'),beta=float('inf')):
        # on s'arrete a 1 ( on donne en entree un nombre impaire) donc on veut s'arreter au tour du joueur 1 qui est l'ia
        if othellier.game_over() or profondeur==1:
            return self.evaluation(othellier),None

        meilleur_score=float('-inf') if othellier.player==1 else float('inf')
        meilleur_coup=None
        playable = [pos for positions in othellier.calculatePossibilities().values() for pos in positions]
        if playable:
            for move in playable:
                #creation d'une copy pour pouvoir rapeller la fonction avec cette nouvelle matrice
                new_othellier = copy.deepcopy(othellier)
                #place le pion et change de joueur avant l'appel de la fonction
                new_othellier.placePaw(move)
                new_othellier.changePlayer() 
                score, _ = self.minimax(new_othellier, profondeur - 1,-alpha,-beta)
                # on inverse le signe car on applique negamax donc ce que gagne le joueur adeversaire represente une perte pour le joueur actuelle
                score=-score
                if othellier.player == 1:
                    if score > meilleur_score:
                        meilleur_score = score
                        meilleur_coup = move
                    alpha=max(alpha,score)
                    
                if othellier.player == 0 :
                    if score < meilleur_score:
                        meilleur_score = score
                        meilleur_coup = move
                    beta=min(beta,score)
                #elagage alphabeta
                if beta <= alpha:
                    break
            return  meilleur_score,meilleur_coup
    
