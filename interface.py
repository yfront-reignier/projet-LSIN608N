import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class Interface(tk.Tk):
    def __init__(self): 
        super().__init__()

        self.wm_title("Othello")
        self.geometry("720x640")
        self.config = self.configure(bg = "#e6dbbe")

        self.mainmenu = MainMenu(self)
        self.mainmenu.grid()


class MainMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        

        self.label = tk.Label(parent,text = "Othello", justify=tk.CENTER)
        self.label.grid(row =0, column=0, columnspan=4)
        self.label.config(font=("Arial", 20))

        self.fond = Image.open("othello.png")
        self.fond = self.fond.resize((500,500))
        self.fond_tk = ImageTk.PhotoImage(self.fond)
        
        self.cnv = tk.Canvas(parent, width=500, height=500)
        self.cnv.grid(row=0, column=0, rowspan=4, columnspan=3)
        self.cnv.create_image(0, 0, image=self.fond_tk, anchor="nw")
        
        self.jcj_button = tk.Button(parent, text="Joueur vs Joueur", padx=20, pady=10, font=("Arial", 10))
        self.jcj_button.grid(row=1,column=0,columnspan=2)
        
        self.jcia_button = tk.Button(parent,text="Joueur vs IA",padx=20, pady=10, font=("Arial", 10))
        self.jcia_button.grid(row=1,column=1,columnspan=4)
        
        self.button_quit = tk.Button(parent, text = "Quitter", command = self.quit())
        self.button_quit.grid(row=2, column=0, columnspan=4)

    def start_game(self):
        self.game = Game(self)

class Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


if __name__ == '__main__': 
    vizualiser = Interface()
    vizualiser.mainloop()
    v2 = MainMenu()
    v2.mainloop()