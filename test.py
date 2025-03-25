import unittest
import numpy as np
import unittest.test
import othello as oth

class TestOthellier(unittest.TestCase):
    def testGridSize(self):
        othellier = oth.Othellier()
        self.assertEqual(othellier.othellier_matrix.shape, (8, 8))  

    def testStartPosition(self):
        othellier = oth.Othellier()

        test_othellier = np.zeros((8,8), object)

        test_othellier[3,4], test_othellier[4,3] = oth.Pion(0, (4,5)), oth.Pion(0, (5,4))
        test_othellier[3,3], test_othellier[4,4] = oth.Pion(1, (4,4)), oth.Pion(1, (5,5))

    def testChangePlayer(self):
        othellier = oth.Othellier()
        self.assertEqual(othellier.player, 0)

        othellier.changePlayer()
        self.assertEqual(othellier.player,  1)

        othellier.changePlayer()
        self.assertEqual(othellier.player, 0)

    def testPlaceChecker(self):
        othellier = oth.Othellier()

        test_othellier = np.zeros((8,8), object)
        test_othellier[3,4], test_othellier[4,3] = oth.Pion(0, (4,5)), oth.Pion(0, (5,4))
        test_othellier[3,3], test_othellier[4,4] = oth.Pion(1, (4,4)), oth.Pion(1, (5,5))

        othellier.placeChecker((0,0))
        test_othellier[0,0] = oth.Pion(0, (1,1))
        self.assertEqual(test_othellier.all(), othellier.getMatrix().all())

        othellier.placeChecker((7,7))
        test_othellier[7,7] = oth.Pion(0, (8,8))
        self.assertEqual(test_othellier.all(), othellier.getMatrix().all())

        othellier.placeChecker((0,0))
        self.assertEqual(test_othellier.all(), othellier.getMatrix().all())

    def testWinner(self):
        othellier = oth.Othellier()

        self.assertEqual(othellier.winner(), None)

        othellier.placeChecker((7,7))
        self.assertEqual(othellier.winner(), 1)

        othellier.placeChecker((6,6))
        othellier.changePlayer()
        othellier.placeChecker((5,5))
        self.assertEqual(othellier.winner(), 0)

if __name__ == '__main__':
    unittest.main()