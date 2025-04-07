from othellier import Othellier

class Computer(Othellier):
    def __init__(self):
        super().__init__()
    
    def startRecursive(self, n):
        dico = {}
        if n == 0:
            return dico
        if n % 2 == 0:
            pass

    def cost(self):
        playable = self._playablePoints()