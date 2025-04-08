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
        self.assertIsInstance(othellier.othellier_matrix[0, 0], Paw)
        self.assertEqual(othellier.othellier_matrix[0, 0].getColor(), 0)

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