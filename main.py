from othellier import Othellier
from paw import Paw
from computer import Computer

if __name__ == '__main__':
    othellier = Othellier()
    computer = Computer()
    poss = othellier.calculatePossibilities()
    print(poss.keys())
    othellier.placePaw((3,5))

    # computer.start_recursive()
    othellier.showGrid()

