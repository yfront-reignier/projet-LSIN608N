import numpy as np
from pion import Pion

class Othellier:
    def __init__(self):
        self.player = 0
        self.running_state = True
        self.othellier_matrix = np.zeros((8,8), dtype=object)
        self.__newGame()
       
    ### Public methods ###
    def verif(self):
        pass

    def changePlayer(self):
        self.player = (self.player + 1) % 2

    def placeChecker(self, pos):
        if self.othellier_matrix[pos[0], pos[1]] == 0:
            self.othellier_matrix[pos[0], pos[1]] = Pion(self.player, pos + (1,1))
            self.changePlayer()
        else:
            print("Already a checker here.")

    def winner(self):
        all_checkers = self.__countChecker()

        if all_checkers[0] == all_checkers[1]:
            print("Egalité")
            return None
        if all_checkers[0] < all_checkers[1]:
            print("Blanc gagne")
            return 1
        if all_checkers[0] > all_checkers[1]:
            print("Noir gagne")
            return 0

    ### Protected methods ###
    def _takeCheckers(self, l_pion):
        for pion in l_pion:
            pion.changeColor()

    def _isEmpty(self):
        for ligne in self.othellier_matrix:
            for elm in ligne:
                if elm != 0:
                    return False
        return True

    def _isFull(self):
        for ligne in self.othellier_matrix:
            for elm in ligne:
                if elm == 0:
                    return False
        return True

    def _playablePoints(self):
        playable = []


    ### Private methods ###
    def __fillCenter(self):
        self.othellier_matrix[3,3] = Pion(0,(4,4))
        self.othellier_matrix[3,4] = Pion(1,(4,5))
        self.othellier_matrix[4,3] = Pion(1,(5,4))
        self.othellier_matrix[4,4] = Pion(0,(5,5))

    def __countChecker(self):
        nb_checker_white = 0
        nb_checker_black = 0
        
        for liste in self.othellier_matrix:
            for elm in liste:
                if elm != 0:
                    if elm.getColor() == 0:
                        nb_checker_white += 1
                    if elm.getColor() == 1:
                        nb_checker_black += 1

        return (nb_checker_black, nb_checker_white)

    def __newGame(self):
        self.othellier_matrix = np.zeros((8, 8), object)
        self.__fillCenter()

    ### Getter ###
    def getMatrix(self):
        return self.othellier_matrix

    ### Debug methods ###
    def showGrid(self):
        print(self.othellier_matrix)
