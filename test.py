import unittest
import numpy as np
from othellier import Othellier
from pion import Pion
from computer import Computer

class TestOthellier(unittest.TestCase):
    def testGridSize(self):
        othellier = Othellier()
        self.assertEqual(othellier.othellier_matrix.shape, (8, 8))

    def testStartPosition(self):
        othellier = Othellier()
        self.assertIsInstance(othellier.othellier_matrix[3, 3], Pion)
        self.assertIsInstance(othellier.othellier_matrix[3, 4], Pion)
        self.assertIsInstance(othellier.othellier_matrix[4, 3], Pion)
        self.assertIsInstance(othellier.othellier_matrix[4, 4], Pion)

    def testChangePlayer(self):
        othellier = Othellier()
        self.assertEqual(othellier.player, 0)
        othellier.changePlayer()
        self.assertEqual(othellier.player, 1)
        othellier.changePlayer()
        self.assertEqual(othellier.player, 0)

    def testPlaceChecker(self):
        othellier = Othellier()
        othellier.placeChecker((0, 0))
        self.assertIsInstance(othellier.othellier_matrix[0, 0], Pion)
        self.assertEqual(othellier.othellier_matrix[0, 0].getColor(), 0)

    def testWinner(self):
        othellier = Othellier()
        self.assertEqual(othellier.winner(), None)
        othellier.placeChecker((7, 7))
        self.assertEqual(othellier.winner(), 1)

class TestPion(unittest.TestCase):
    def testPionInitialization(self):
        pion = Pion(0, (4, 4))
        self.assertEqual(pion.getColor(), 0)
        self.assertEqual(pion.getPosition(), (4, 4))

    def testChangeColor(self):
        pion = Pion(0, (4, 4))
        pion.changeColor()
        self.assertEqual(pion.getColor(), 1)
        pion.changeColor()
        self.assertEqual(pion.getColor(), 0)

class TestComputer(unittest.TestCase):
    def testAlphaBetaPruning(self):
        computer = Computer()
        computer.othellier_matrix[3, 3] = Pion(0, (4, 4))
        computer.othellier_matrix[3, 4] = Pion(1, (4, 5))
        computer.othellier_matrix[4, 3] = Pion(1, (5, 4))
        computer.othellier_matrix[4, 4] = Pion(0, (5, 5))
        result = computer.startRecursive(3)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()