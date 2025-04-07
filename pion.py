class Pion():
    def __init__(self, color, pos):
        self.color = color
        self.position = pos
    
    def __repr__(self):
        if self.color == 0:
            return f'N'
        if self.color == 1:
            return f'B'
    
    def getColor(self):
        return self.color
    
    def changeColor(self):
        self.color = 2 % (self.color + 1)

    def getPosition(self):
        return self.position