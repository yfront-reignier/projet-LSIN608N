# COMPUTER

from othellier import Othellier

class Computer(Othellier):
    def __init__(self,othellier:Othellier):
        super().__init__()
        self.othellier=othellier
    
    def evaluation(self,possibilities:dict,pos2):
        liste_pos1=[]
        counter=0
        for key,liste in possibilities.items():
            if pos2 in liste:
                liste_pos1.append(key)
        for pos1 in liste_pos1:
            counter+=self._takePaws(pos1,pos2,False)
        return counter
            

    def minimax(self,profondeur,move=None):
        if self.othellier.game_over() or profondeur==0:
            return self.evaluation(self.calculatePossibilities(),move)
        playable=[]
        for positions in self.othellier.calculatePossibilities().values():
            for pos in positions:
                if pos not in playable:
                    playable.append(pos)
        if self.othellier.player==0:
            meilleure_score=float('-inf')
            for move in playable:
                if self.othellier.placePaw(move,False):
                    score=self.minimax(profondeur-1,move)
                    self.othellier_matrix[move]=0
                    if score>meilleure_score:
                        meilleure_score=score
                        meilleure_coup=move            
        else:
            meilleure_score=float('inf')
            for move in playable:
                if self.othellier.placePaw(move,False):
                    score=self.minimax(profondeur-1)
                    self.othellier_matrix[move]=0
                    if score>meilleure_score:
                        meilleure_score=score
                        meilleure_coup=move 
        
        
        return(meilleure_score,meilleure_coup)
    
com=Computer(Othellier())
com.showGrid()
print(com.minimax(3)  
)    
