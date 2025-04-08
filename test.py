import unittest
import numpy as np
from othellier import Othellier
from paw import Paw
from computer import Computer

class TestOthellier(unittest.TestCase):
    def testGridSize(self):
        othellier = Othellier()
        self.assertEqual(othellier.othellier_matrix.shape, (8, 8))

    def testStartPosition(self):
        othellier = Othellier()
        self.assertIsInstance(othellier.othellier_matrix[3, 3], Paw)
        self.assertIsInstance(othellier.othellier_matrix[3, 4], Paw)
        self.assertIsInstance(othellier.othellier_matrix[4, 3], Paw)
        self.assertIsInstance(othellier.othellier_matrix[4, 4], Paw)

    def testChangePlayer(self):
        othellier = Othellier()
        self.assertEqual(othellier.player, 0)
        othellier.changePlayer()
        self.assertEqual(othellier.player, 1)
        othellier.changePlayer()
        self.assertEqual(othellier.player, 0)

    def testPlacePaw(self):
        othellier = Othellier()
        othellier.placePaw((0, 0))
        self.assertEqual(othellier.othellier_matrix[0, 0], 0)
        othellier.placePaw((3, 5))
        self.assertIsInstance(othellier.othellier_matrix[3, 5], Paw)
        self.assertEqual(othellier.othellier_matrix[3, 5].getColor(), 0)

    def testWinner(self):
        othellier = Othellier()
        self.assertEqual(othellier.winner(), None)
        othellier.placePaw((3, 5))
        self.assertEqual(othellier.winner(), 0)

    def testCalculatePossibilities(self):
        othellier = Othellier()
        othellier.changePlayer()
        # Initial state of the board
        possibilities = othellier.calculatePossibilities()

        # Expected possibilities for the initial state
        expected_possibilities = {
            (3, 4): [(5, 4), (3, 2)],
            (4, 3): [(4, 5), (2, 3)],
        }

        # Check if the calculated possibilities match the expected ones
        self.assertEqual(possibilities, expected_possibilities)

    def testFindOpponentPaws(self):
        # Initialisation de l'othellier
        othellier = Othellier()

        # Placement des pions pour le test
        othellier.othellier_matrix[3, 3] = Paw(0, (3, 3))  # Pion du joueur
        othellier.othellier_matrix[3, 4] = Paw(1, (3, 4))  # Pion adverse
        othellier.othellier_matrix[3, 5] = Paw(1, (3, 5))  # Pion adverse
        othellier.othellier_matrix[3, 6] = Paw(0, (3, 6))  # Pion du joueur

        # Appel de la méthode pour trouver les pions adverses
        opponent_paws = othellier._findOpponentPaws(3, 3)

        # Vérification des résultats
        expected_opponents = [
            othellier.othellier_matrix[3, 4],
            othellier.othellier_matrix[3, 5],
        ]
        self.assertEqual(opponent_paws, expected_opponents)

    def testFindOpponentPawsEmpty(self):
        # Initialisation de l'othellier
        othellier = Othellier()

        # Placement des pions pour le test
        othellier.othellier_matrix[3, 3] = Paw(0, (3, 3))  # Pion du joueur
        othellier.othellier_matrix[3, 4] = 0  # Case vide
        othellier.othellier_matrix[3, 5] = Paw(1, (3, 5))  # Pion adverse
        othellier.othellier_matrix[3, 6] = Paw(0, (3, 6))  # Pion du joueur

        # Appel de la méthode pour trouver les pions adverses
        opponent_paws = othellier._findOpponentPaws(3, 3)

        # Vérification des résultats (aucun pion adverse entre les pions du joueur)
        self.assertEqual(opponent_paws, [])

    def testFindOpponentPawsDiagonal(self):
        # Initialisation de l'othellier
        othellier = Othellier()

        # Placement des pions pour le test
        othellier.othellier_matrix[3, 3] = Paw(0, (3, 3))  # Pion du joueur
        othellier.othellier_matrix[4, 4] = Paw(1, (4, 4))  # Pion adverse
        othellier.othellier_matrix[5, 5] = Paw(1, (5, 5))  # Pion adverse
        othellier.othellier_matrix[6, 6] = Paw(0, (6, 6))  # Pion du joueur

        # Appel de la méthode pour trouver les pions adverses
        opponent_paws = othellier._findOpponentPaws(3, 3)

        # Vérification des résultats
        expected_opponents = [
            othellier.othellier_matrix[4, 4],
            othellier.othellier_matrix[5, 5],
        ]
        self.assertEqual(opponent_paws, expected_opponents)

class TestPaw(unittest.TestCase):
    def testPawInitialization(self):
        paw = Paw(0, (4, 4))
        self.assertEqual(paw.getColor(), 0)
        self.assertEqual(paw.getPosition(), (4, 4))

    def testChangeColor(self):
        paw = Paw(0, (4, 4))
        paw.changeColor()
        self.assertEqual(paw.getColor(), 1)
        paw.changeColor()
        self.assertEqual(paw.getColor(), 0)

if __name__ == '__main__':
    unittest.main()