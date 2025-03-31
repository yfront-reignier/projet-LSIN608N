import tkinter as tk
import numpy as np

class Interface(tk.Tk):
    def __init__(self): 
        super().__init__()

        self.wm_title("Othello")
        self.geometry("720x640")
        self.config = self.configure(bg = "#e6dbbe")

        self.mainmenu = MainMenu(self)


class MainMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.pack()

        self.button_start = tk.Button(self, text = "Jouer", command = self.start_game())
        self.button_start.pack()

        self.button_quit = tk.Button(self, text = "Quitter", command = self.quit())
        self.button_quit.pack()

    def start_game(self):
        self.game = Game(self)

class Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


if __name__ == '__main__': 
    vizualiser = Interface()
    vizualiser.mainloop()