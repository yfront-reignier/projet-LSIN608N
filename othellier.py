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
        playable = [pos for positions in possibilities.values() for pos in positions]
        if not self.__isValidPosition(position) or position not in playable:
            print("Invalid position")
            return False

        if self.othellier_matrix[position[0], position[1]] == 0:
            self.othellier_matrix[position[0], position[1]] = Paw(self.player, position)
            self._takePaws(self._findOpponentPaws(position[0], position[1]))
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
        # Calcule tous les coups possibles pour le joueur actuel
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
                valid_positions = self.__checkDirection(x, y, dx, dy, paw)
                if valid_positions:
                    possibilities.setdefault(paw, []).extend(valid_positions)

        return possibilities

    ### Protected methods ###
    def _takePaws(self, paws_list):
        for paw in paws_list:
            paw.changeColor()

    def _findOpponentPaws(self, x, y):
        opponent_paws = []
        directions = [
            (0, 1), (1, 0), (1, 1), (-1, -1),  
            (0, -1), (-1, 0), (-1, 1), (1, -1)
        ]

        for dx, dy in directions:
            i, j = x + dx, y + dy
            temp_opponents = []  # Liste temporaire pour stocker les pions adverses dans cette direction
            while self.__isValidPosition((i, j)):
                current_paw = self.othellier_matrix[i, j]
                if current_paw == 0:  # Case vide
                    break
                elif current_paw.getColor() != self.player:  # Pion adverse
                    temp_opponents.append(current_paw)  # Ajoute le pion adverse à la liste temporaire
                else:  # Pion du joueur
                    # Si un pion du joueur est rencontré, ajoute les pions adverses entre les deux
                    opponent_paws.extend(temp_opponents)
                    break
                i += dx
                j += dy

        return opponent_paws

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

    def __isValidPosition(self, position):
        return 0 <= position[0] < 8 and 0 <= position[1] < 8

    def __getPlayerPaws(self):
        paws = []
        for i in range(8):
            for j in range(8):
                paw = self.othellier_matrix[i, j]
                if paw != 0 and paw.getColor() == self.player:
                    paws.append((i, j))
        return paws

    def __checkDirection(self, x, y, dx, dy, paw, collect_opponents=False):
        i, j = x + dx, y + dy
        found_opponent = False
        opponents = []  # Liste pour collecter les pions adverses

        while self.__isValidPosition((i, j)):
            current_paw = self.othellier_matrix[i, j]
            if current_paw == 0:  # Case vide
                if found_opponent and not collect_opponents:
                    return [(i, j)]  # Retourne la position valide
                break
            elif current_paw.getColor() != self.player:  # Pion adverse
                found_opponent = True
                if collect_opponents:
                    opponents.append((i, j))  # Collecte les pions adverses
            else:  # Pion du joueur
                break
            i += dx
            j += dy

        return opponents if collect_opponents else []
