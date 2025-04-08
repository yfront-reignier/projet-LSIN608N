from othellier import Othellier
from paw import Paw
from computer import Computer

if __name__ == '__main__':
    othellier = Othellier()
    computer = Computer()
    poss = othellier.calculatePossibilities()
    
    othellier.placePaw((5,3))

    othellier.showGrid()

    othellier.placePaw((5,4))

    # computer.start_recursive()
    othellier.showGrid()

