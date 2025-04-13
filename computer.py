# COMPUTER

from othellier import Othellier
import copy

class Computer(Othellier):
    def __init__(self,othellier:Othellier):
        super().__init__()
        self.othellier=othellier
    
    def evaluation(self,plateau:Othellier):

        if plateau.player==0:
            return plateau._countPaws()[1]-plateau._countPaws()[0]
        else:
            return plateau._countPaws()[0]-plateau._countPaws()[1]
        
    def minimax(self,plateau:Othellier,profondeur):
        if plateau.game_over() or profondeur==1:
            return self.evaluation(plateau),None

        meilleur_score=float('-inf') if plateau.player==1 else float('inf')
        meilleur_coup=None
        playable = [pos for positions in plateau.calculatePossibilities().values() for pos in positions]
        if playable:
            for move in playable:
                new_plateau = copy.deepcopy(plateau)
                new_plateau.placePaw(move)
                score, _ = self.minimax(new_plateau, profondeur - 1)

                if plateau.player == 1 and score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = move
                elif plateau.player == 0 and score < meilleur_score:
                    meilleur_score = score
                    meilleur_coup = move

            return  meilleur_coup
    
