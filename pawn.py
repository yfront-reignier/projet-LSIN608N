class Paw():
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
    
    def changeColor(self,new_color):
        self.color = new_color

    def getPosition(self):
        return self.position