class Pion():
    def __init__(self, color, pos):
        self.color = color
        self.position = pos
    
    def __repr__(self):
        if self.color == 0:
            return f'N'
        if self.color == 1:
            return f'B'
    
    def GetColor(self):
        return self.color
    
    def ChangeColor(self,new_color):
        self.color = new_color

    def GetPosition(self):
        return self.position