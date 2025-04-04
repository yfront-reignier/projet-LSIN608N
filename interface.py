import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class Interface(tk.Tk):
    def __init__(self): 
        super().__init__()

        self.wm_title("Othello")
        self.geometry("1000x1000")
        self.config = self.configure(bg = "#e6dbbe")

        self.mainmenu = MainMenu(self)

class MainMenu(tk.Frame):
    def __init__(self, parent):
        self.parent=parent
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
        
        self.jcj_button = tk.Button(parent, text="Joueur vs Joueur", padx=20, pady=10, font=("Arial", 10), command=self.start_game)
        self.jcj_button.grid(row=1,column=0,columnspan=2)
        
        self.jcia_button = tk.Button(parent,text="Joueur vs IA",padx=20, pady=10, font=("Arial", 10))
        self.jcia_button.grid(row=1,column=1,columnspan=4)
        
        self.button_quit = tk.Button(parent, text = "Quitter", command = parent.quit)
        self.button_quit.grid(row=2, column=0, columnspan=4)

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_rowconfigure(2, weight=1)

        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

    def start_game(self):
        self.cnv.destroy()
        self.label.destroy()
        self.jcj_button.destroy()
        self.jcia_button.destroy()
        self.button_quit.destroy()
        self.game = Game(self.parent)
        

class Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.yellow_circles=[]
        self.canvas_pions={}

        self.plateau=tk.Canvas(parent,width=800,height=800,background='green')

        self.label = tk.Label(parent, text="Nb pions noir:2",font=("Arial", 20))
        self.label.grid(row=1,column=0)

        self.label2 = tk.Label(parent, text="Nb pions blanc:2",font=("Arial", 20))
        self.label2.grid(row=2,column=0)

        self.label3 = tk.Label(parent, text="Tour de:",font=("Arial", 20))
        self.label3.grid(row=1,column=5)

        self.createGrid(8)
        

    def createGrid(self, dim_matrix):
        self.plateau.grid(row=1,column=1,rowspan=2,columnspan=5)
        self.plateau.create_rectangle(0,0,800,800,fill="green")

        for i in range(dim_matrix):
            for j in range(dim_matrix):
                x0 = i*100
                y0 = j*100
                x1 = (i+1)*100
                y1 = (j+1)*100
                self.plateau.create_rectangle(x0,y0,x1,y1,fill="green",outline="black")
    



if __name__ == '__main__': 
    vizualiser = Interface()
    vizualiser.mainloop()