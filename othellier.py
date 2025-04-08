import numpy as np
from paw import Paw

class Othellier:
    def __init__(self):
        self.player = 0  # 0 : Noir, 1 : Blanc
        self.running_state = True
        self.othellier_matrix = np.zeros((8, 8), dtype=object)
        self.__initializeGame()

    ### Public methods ###
    def changePlayer(self):
        self.player = (self.player + 1) % 2

    def placePaw(self, position):
        possibilities = self.calculatePossibilities()
        if not self.__isValidPosition(position) or position not in possibilities.keys():
            print("Invalid position")
            return False

        if self.othellier_matrix[position[0], position[1]] == 0:
            self.othellier_matrix[position[0], position[1]] = Paw(self.player, position)
            self._takePaws(possibilities[position])
            self.changePlayer()
            return True
        else:
            print("There is already a paw here.")
            return False

    def winner(self):
        nb_black, nb_white = self.__countPaws()

        if nb_black == nb_white:
            print("Draw")
            return None
        elif nb_black > nb_white:
            print("Black wins")
            return 0
        else:
            print("White wins")
            return 1

    def showGrid(self):
        print(self.othellier_matrix)

    def calculatePossibilities(self):
        possibilities = {}

        # Récupère tous les pions du joueur actuel
        player_paws = self.__getPlayerPaws()

        # Directions : (dx, dy) pour les mouvements horizontaux, verticaux et diagonaux
        directions = [
            (0, 1), (1, 0), (1, 1), (-1, -1),  # Droite, Bas, Diagonale bas-droite, Diagonale haut-gauche
            (0, -1), (-1, 0), (-1, 1), (1, -1)  # Gauche, Haut, Diagonale haut-droite, Diagonale bas-gauche
        ]

        for paw in player_paws:
            x, y = paw
            for dx, dy in directions:
                self.__checkDirection(x, y, dx, dy, possibilities, paw)

        return possibilities

    ### Protected methods ###
    def _takePaws(self, paws_list):
        for paw in paws_list:
            paw.changeColor()

    def _isEmpty(self):
        return not np.any(self.othellier_matrix)

    def _isFull(self):
        return not np.any(self.othellier_matrix == 0)

    ### Private methods ###
    def __initializeGame(self):
        self.othellier_matrix[3, 3] = Paw(0, (3, 3))
        self.othellier_matrix[3, 4] = Paw(1, (3, 4))
        self.othellier_matrix[4, 3] = Paw(1, (4, 3))
        self.othellier_matrix[4, 4] = Paw(0, (4, 4))

    def __countPaws(self):
        nb_black = sum(
            1 for row in self.othellier_matrix for paw in row if paw != 0 and paw.getColor() == 0
        )
        nb_white = sum(
            1 for row in self.othellier_matrix for paw in row if paw != 0 and paw.getColor() == 1
        )
        return nb_black, nb_white

    def __isValidPosition(self, pos):
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8

    def __getPlayerPaws(self):
        paws = []
        for i in range(8):
            for j in range(8):
                paw = self.othellier_matrix[i, j]
                if paw != 0 and paw.getColor() == self.player:
                    paws.append((i, j))
        return paws

    def __findOpponentPaws(self, x, y):
        opponent_paws = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.__isValidPosition((i, j)) and (i != x or j != y):
                    paw = self.othellier_matrix[i, j]
                    if paw != 0 and paw.getColor() != self.player:
                        opponent_paws.append((i, j))
        return opponent_paws

    def __checkDirection(self, x, y, dx, dy, possibilities, paw):
        i, j = x + dx, y + dy
        found_opponent = False

        while self.__isValidPosition((i, j)):
            current_paw = self.othellier_matrix[i, j]
            if current_paw == 0:
                if found_opponent:
                    possibilities.setdefault(paw, []).append((i, j))
                break
            elif current_paw.getColor() != self.player:
                found_opponent = True
            else:
                break
            i += dx
            j += dy
