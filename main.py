from othellier import Othellier
from pion import Pion
from computer import Computer

if __name__ == '__main__':
    othellier = Othellier()
    computer = Computer()
    computer.start_recursive()
    othellier.showGrid()

