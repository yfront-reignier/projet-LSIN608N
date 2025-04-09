import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from othellier import Othellier
from computer import Computer
import time


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
        
        self.label = tk.Label(parent,text = "Othello \n⚫VS⚪ ",bg="#e6dbbe", justify=tk.CENTER)
        self.label.grid(row =0, column=0,rowspan=1, columnspan=4)
        self.label.config(font=("ArcadeClassic",100 ))

        # self.fond = Image.open("othello.png")
        # self.fond = self.fond.resize((500,500))
        # self.fond_tk = ImageTk.PhotoImage(self.fond)
        
        # self.cnv = tk.Canvas(parent, width=500, height=500)
        # self.cnv.grid(row=0, column=0, rowspan=4, columnspan=3)
        # self.cnv.create_image(0, 0, image=self.fond_tk, anchor="nw")
        
        self.jcj_button = tk.Button(parent, text="Joueur vs Joueur", padx=20, pady=10, bd=5, font=("Arial", 14,"bold"),
                                    bg="#228B22",fg="white",activebackground="#008000",activeforeground="white",
                                    relief="raised",  command=lambda: self.start_game('jvsj'))
        self.jcj_button.grid(row=1,column=0,columnspan=2)
        
        self.jcia_button = tk.Button(parent,text="Joueur vs IA",padx=20, pady=10, bd=5, font=("Arial", 14,"bold"),
                                    bg="#228B22",fg="white",activebackground="#008000",activeforeground="white",
                                    relief="raised",command=lambda: self.start_game('jvsia'))
        self.jcia_button.grid(row=1,column=1,columnspan=4)

        self.button_regle = tk.Button(parent, text = "Règle du Jeu", padx=20, pady=10, bd=5, font=("Arial", 14,"bold"),
                                    bg="#696969",fg="white",activebackground="#000000",activeforeground="white",
                                    relief="raised", command = self.regle)
        self.button_regle.grid(row=2,column=1,columnspan=4)
        
        self.button_quit = tk.Button(parent, text = "Quitter", padx=20, pady=10, bd=5, font=("Arial", 14,"bold"),
                                    bg="#696969",fg="white",activebackground="#000000",activeforeground="white",
                                    relief="raised", command = parent.quit)
        self.button_quit.grid(row=2, column=0, columnspan=2)

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_rowconfigure(2, weight=1)

        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

    def regle(self):
        self.label.destroy()
        self.jcj_button.destroy()
        self.jcia_button.destroy()
        self.button_quit.destroy()
        self.button_regle.destroy()
        self.game = RegleDuJeu(self.parent)

    def start_game(self,mode):
        self.label.destroy()
        self.jcj_button.destroy()
        self.jcia_button.destroy()
        self.button_quit.destroy()
        self.button_regle.destroy()
        self.game = Game(self.parent,mode)
        
class RegleDuJeu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent

        self.label = tk.Label(parent, text="Règle du Jeu",font=("ArcadeClassic",20),bg="#e6dbbe", justify=tk.CENTER)
        self.label.grid(row=0,column=0)

        texte = """blavblabblablalblblblblbl """
        
        self.ecrit=tk.Label(parent, text=texte,
          font=("Helvetica", 12),
          bg="#f0e6d6",
          justify=LEFT,
          padx=20,
          pady=20)
        self.ecrit.grid(row=0,column=1)

        self.replay_button = tk.Button(parent, text="Retourner au Menu",padx=20, pady=10, bd=5, font=("Arial", 14,"bold"),
                                    bg="#696969",fg="white",activebackground="#000000",activeforeground="white",
                                    relief="raised",  command = self.replay_game)
        self.replay_button.grid(row=1, column=1)

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_rowconfigure(2, weight=1)

        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

    def replay_game(self):
        self.label.destroy()
        self.ecrit.destroy()
        self.replay_button.destroy()
        MainMenu(self.parent)

class Game(tk.Frame):
    def __init__(self, parent,mode):
        super().__init__(parent)
        self.mode=mode
        self.parent=parent
        self.color={0:'Noir',1:'Blanc'}
        self.plateau=tk.Canvas(parent,width=800,height=800,background='green')
        self.hints=[]
        self.hint_all_game=False
        self.canvas_pions={}
        self.othellier=Othellier()

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_rowconfigure(2, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

        self.hint=tk.Button(parent,text='Indices-Toute la partie',font=("Helvetica", 16, "bold"), fg="black", bg="#f0e6d6",command=self.show_hints_all_game)
        self.hint.grid(row=4,column=0)
        
        self.hint=tk.Button(parent,text='Indices-Un tour',font=("Helvetica", 16, "bold"), fg="black", bg="#f0e6d6",command=self.show_hints)
        self.hint.grid(row=3,column=0)

        self.label = tk.Label(parent, text="⚫Pions noir: "+str(self.othellier._countPaws()[0]),font=("Helvetica", 16, "bold"), fg="black", bg="#f0e6d6")
        self.label.grid(row=2,column=0)

        self.label2 = tk.Label(parent, text="⚪Pions blanc: "+str(self.othellier._countPaws()[0]),font=("Helvetica", 16, "bold"), fg="black", bg="#f0e6d6")
        self.label2.grid(row=1,column=0)

        self.label3 = tk.Label(parent, text="Tour du joueur: Noir",font=("Helvetica", 16, "bold"), fg="black", bg="#f0e6d6")
        self.label3.grid(row=0,column=0)
        
        

        self.createGrid(self.othellier.GetMatrix())
        self.createCircle()
        parent.bind("<Button-3>",self.click)

        
    def show_hints_all_game(self):
        self.show_hints()  
        self.hint_all_game=True  
    def show_hints(self):
        playable = [pos for positions in self.othellier.calculatePossibilities().values() for pos in positions]      
        for elem in playable:
            x,y=elem
            x0 = y*100+5
            y0 = x*100+5
            x1 = x0 + 95
            y1 = y0 + 95  
            self.hints.append(self.plateau.create_oval(x0, y0, x1, y1,outline='#17b669', fill='',width=2) )
    def delete_hints(self):
        if self.hints:
            for elem in self.hints:
                self.plateau.delete(elem)
            self.hints.clear()

    def createGrid(self, matrix):
        dim_matrix = matrix.shape[0]
        self.plateau.grid(row=0,column=1,rowspan=6,columnspan=6)
        self.plateau.create_rectangle(0,0,800,800,fill="green")

        for i in range(dim_matrix):
            for j in range(dim_matrix):
                x0 = i*100
                y0 = j*100
                x1 = (i+1)*100
                y1 = (j+1)*100
                self.plateau.create_rectangle(x0,y0,x1,y1,fill="green",outline="black")

    def createCircle(self):
        for x in range(len(self.othellier.GetMatrix())):
            for y in range(len(self.othellier.GetMatrix())):
                if self.othellier.GetMatrix()[x][y] != 0:
                    x0 = y*100+5
                    y0 = x*100+5
                    x1 = x0 + 90
                    y1 = y0 + 90
                    if self.othellier.GetMatrix()[x][y].getColor() == 0:
                        self.plateau.create_oval(x0+2, y0+2, x1+2, y1+2, fill='grey30', outline='')
                        self.plateau.create_oval(x0, y0, x1, y1, fill='black')
                    else:
                        self.plateau.create_oval(x0+2, y0+2, x1+2, y1+2, fill='grey30', outline='')
                        self.plateau.create_oval(x0, y0, x1, y1, fill='white')

          
    def maj_score(self):
        self.label.config(text="Pions noir: "+str(self.othellier._countPaws()[0]))
        self.label2.config(text="Pions blanc: "+str(self.othellier._countPaws()[1]))
        self.label3.config(text="Tour du joueur: "+self.color[self.othellier.GetPlayer()])

    def win_lose(self,parent):
            if self.othellier.winner() == 0:
                self.label.destroy()
                self.label2.destroy()
                self.label3.destroy()
                self.plateau.destroy()
                self.label = tk.Label(parent, text="Blanc gagne",font=("Arial", 20))
                self.label.grid(row=1,column=0,columnspan=4)
            elif self.othellier.winner() == 1:
                self.label.destroy()
                self.label2.destroy()
                self.label3.destroy()
                self.plateau.destroy()
                self.label = tk.Label(parent, text="Noir gagne",font=("Arial", 20))
                self.label.grid(row=1,column=0,columnspan=4)
            elif self.othellier.winner() == None:
                self.label.destroy()
                self.label2.destroy()
                self.label3.destroy()
                self.plateau.destroy()
                self.label = tk.Label(parent, text="Egalité",font=("Arial", 20))
                self.label.grid(row=1,column=0,columnspan=4)

            GameOver(self.parent)

    def click(self,event):
        self.delete_hints() 
        self.othellier.click(self.plateau,(event.x,event.y)) 
        self.maj_score()
        if self.hint_all_game:
            self.show_hints()
        time.sleep(0.5)  
        if self.othellier.game_over():
            self.win_lose(self.parent)
        
            

class GameOver(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent

        self.label = tk.Label(parent, text="Game Over",font=("Arial", 20))
        self.label.grid(row=1,column=0,columnspan=4)


        self.button_quit = tk.Button(parent, text = "Quitter", padx=20, pady=10, command = parent.quit)
        self.button_quit.grid(row=2, column=0, columnspan=2) 

        self.replay_button = tk.Button(parent, text="Rejouer",padx=20, pady=10, command = self.replay_game)
        self.replay_button.grid(row=2, column=1, columnspan=4)

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_rowconfigure(2, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

    def replay_game(self):
        self.label.destroy()
        self.button_quit.destroy()
        self.replay_button.destroy()
        MainMenu(self.parent)

    

if __name__ == '__main__': 
    vizualiser = Interface()
    vizualiser.mainloop()