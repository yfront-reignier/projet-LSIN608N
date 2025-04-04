import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class othellier:
    def __init__(self):
        self.matrice = np.zeros((8,8),dtype=object)
        self.joueurs = {0:"black", 1:"white"}

    def __countChecker(self):
        nb_checker_white = 0
        nb_checker_black = 0
        return (nb_checker_black, nb_checker_white)

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
        # self.othellier=othellier
        # self.matrice = othellier.matrice
        # self.jouers = othellier.joueurs

        self.plateau=tk.Canvas(parent,width=800,height=800,background='green')
        #self.plateau.bind("<Button-1>",self.click_to_draw)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_rowconfigure(2, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

        self.label = tk.Label(parent, text="Nb pions noir:2",font=("Arial", 20))
        self.label.grid(row=1,column=0)

        self.label2 = tk.Label(parent, text="Nb pions blanc:2",font=("Arial", 20))
        self.label2.grid(row=2,column=0)

        self.label3 = tk.Label(parent, text="Tour de: noir",font=("Arial", 20))
        self.label3.grid(row=1,column=5)

        matrix = np.zeros((8,8))
        self.createGrid(matrix)
        

    def createGrid(self, matrix):
        dim_matrix = matrix.shape[0]
        self.plateau.grid(row=1,column=1,rowspan=2,columnspan=5)
        self.plateau.create_rectangle(0,0,800,800,fill="green")

        for i in range(dim_matrix):
            for j in range(dim_matrix):
                x0 = i*100
                y0 = j*100
                x1 = (i+1)*100
                y1 = (j+1)*100
                self.plateau.create_rectangle(x0,y0,x1,y1,fill="green",outline="black")

    # def draw_pion(self):
    #     for ligne in self.matrice:
    #         for elem in ligne:
    #             if elem != 0:
    #                 y, x = elem.getPosition()
    #                 self.plateau.create_oval(x * 100 + 35, y * 100 + 35, x * 100 + 65, y * 100 + 65, fill=self.joueurs[elem.getColor()])

    #     possib=othellier.jeu()
    #     for liste in possib.values():
    #         for pion in liste:
    #             px, py = pion
    #             circle = self.plateau.create_oval(py * 100 + 35, px * 100 + 35, py * 100 + 65, px * 100 + 65, outline='yellow', width=3)
    #             self.yellow_circles.append(circle)
    
    # def click_to_draw(self, event):
    #     othellier.click(self.plateau,(event.x,event.y),self.yellow_circles)



    # def maj_label(self, othellier):
    #     nb_noir = othellier.__countChecker()[0]
    #     nb_blanc = othellier.__countChecker()[1]
    #     self.label.config(text=f"Nb pions noir: {nb_noir}")
    #     self.label2.config(text=f"Nb pions blanc: {nb_blanc}")
    #     self.label3.config(text=f"Tour de: noir")



if __name__ == '__main__': 
    vizualiser = Interface()
    vizualiser.mainloop()