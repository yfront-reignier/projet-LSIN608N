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
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.config = self.configure(bg = "#e6dbbe")
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.mainmenu = MainMenu(self)

class MainMenu(tk.Frame):
    def __init__(self, parent):
        self.parent=parent
        super().__init__(parent)

        self.label = tk.Label(parent,text = "Othello \n⚫VS⚪ ",bg="#e6dbbe", justify=tk.CENTER)
        self.label.grid(row =0, column=0,rowspan=1, columnspan=4)
        self.label.config(font=("ArcadeClassic",100 ))
        
        self.jcj_button = tk.Button(parent, text="Joueur vs Joueur", padx=20, pady=10, bd=5, font=("Arial", 14,"bold"),
                                    bg="#228B22",fg="white",
                                    relief="raised",  command=lambda: self.start_game('jvsj'))
        self.jcj_button.grid(row=1,column=0,columnspan=2)
        
        self.jcia_button = tk.Button(parent,text="Joueur vs IA",padx=20, pady=10, bd=5, font=("Arial", 14,"bold"),
                                    bg="#228B22",fg="white",
                                    relief="raised",command=lambda: self.start_game('jvsia'))
        self.jcia_button.grid(row=1,column=1,columnspan=4)

        self.button_regle = tk.Button(parent, text = "Règle du Jeu", padx=20, pady=10, bd=5, font=("Arial", 14,"bold"),
                                    bg="#696969",fg="white",
                                    relief="raised", command = self.regles)
        self.button_regle.grid(row=2,column=1,columnspan=4)
        
        self.button_quit = tk.Button(parent, text = "Quitter", padx=20, pady=10, bd=5, font=("Arial", 14,"bold"),
                                    bg="#696969",fg="white",
                                    relief="raised", command = parent.quit)
        self.button_quit.grid(row=2, column=0, columnspan=2)

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_rowconfigure(2, weight=1)

        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

    def regles(self):
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

        self.label = tk.Label(parent, text="Regle du Jeu",font=("ArcadeClassic",20),bg="#e6dbbe", justify=tk.CENTER)
        self.label.grid(row=0,column=0)

        texte = """        
        Chaque joueur se voit attribué une couleur et reçoit des pions.
        Chacun étant noir d'un côté et blanc de l'autre.
        Noir commence la partie en plaçant le premier pion à un endroit qui enferme un pion de l'adversaire.

        <Enfermer> un disque signifie entourer un ou plusieurs pion de votre adversaire avec deuax de vos propres pions.

        Tous les pions noirs situés entre les deux pions blancs sont ensuite retournés (captués) et affichent ainsi leur côté blanc.
        Un pion peut capturer n'importe quel nombre de pions de l'adversaire
        (en diagonale, à l'horizontale ou à verticale)

        Si un joueur ne peut pas enfermer au moin un pion de l'adversaire, il est forcé de passer son tour.
        Quand aucun des joueurs ne peut plus déplacer de pions, alors la partie s'arrête.
        Le gagnant en fin de partie est celui qui possède le plus de pions sur le plateau. 
        
        Les indice dans le jeu:
        - Indices-Un tour: vous donne les indices pour le tour en cours.
        - Indices-Toute la partie: vous donne les indices pour toute la partie.
        """
        
        self.ecrit=tk.Label(parent, text=texte,
          font=("Helvetica", 12),
          bg="#f0e6d6",
          justify=LEFT,
          padx=20,
          pady=20)
        self.ecrit.grid(row=0,column=1)

        self.replay_button = tk.Button(parent, text="Retourner au Menu",padx=20, pady=10, bd=5, font=("Arial", 14,"bold"),
                                    bg="#696969",fg="white",
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
        
        self.bg=tk.Canvas(parent,width=250,height=750,bg="#fdfbf9")
        self.bg.place(x=20,y=25)

        self.bg2=tk.Canvas(parent,width=250,height=750,bg="#c8ad7f")
        self.bg2.place(x=1250, y=25)

        self.label3 = tk.Label(parent, text="Tour du joueur: Noir",font=("Helvetica", 16, "bold"), fg="black", bg="#c8ad7f")
        self.label3.place(x=1260,y=550)

        self.label2 = tk.Label(parent, text="⚪Pions blanc: ", font=("Helvetica", 16, "bold"), fg="black", bg="white")
        self.label2.place(x=65,y=28)

        self.score_white = tk.Label(parent, text= str(self.othellier._countPaws()[1]), font=("Helvetica", 36, "bold"), fg="black", bg="#fdfbf9")
        self.score_white.place(x=100,y=300)

        self.label = tk.Label(parent, text="⚫Pions noir: ",font=("Helvetica", 16, "bold"), fg="black", bg="#c8ad7f")
        self.label.place(x=1295,y=28)

        self.score_black = tk.Label(parent, text= str(self.othellier._countPaws()[0]), font=("Helvetica", 36, "bold"), fg="black", bg="#c8ad7f")
        self.score_black.place(x=1340,y=300)
        
        self.hint=tk.Button(parent,text='Indices-Un tour',padx=20, pady=10, bd=5, font=("Helvetica", 14,"bold"),
                                    bg="#f0e6d6",fg="black",relief="raised", command=self.show_hints)
        
        self.hint.place(x=35,y=600)

        self.all_hints=tk.Button(parent,text='Indices-Toute \n la partie',padx=20, pady=10, bd=5, font=("Helvetica", 14,"bold"),
                                    bg="#f0e6d6",fg="black",relief="raised", command=self.show_hints_all_game)
        self.all_hints.place(x=1295,y=600)

        

        self.createGrid(self.othellier.getMatrix())
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
        self.plateau.place(x=350,y=0)
        self.plateau.create_rectangle(0,0,800,800,fill="green")

        for i in range(dim_matrix):
            for j in range(dim_matrix):
                x0 = i*100
                y0 = j*100
                x1 = (i+1)*100
                y1 = (j+1)*100
                self.plateau.create_rectangle(x0,y0,x1,y1,fill="green",outline="black")

    def createCircle(self):
        for x in range(len(self.othellier.getMatrix())):
            for y in range(len(self.othellier.getMatrix())):
                if self.othellier.getMatrix()[x][y] != 0:
                    x0 = y*100+5
                    y0 = x*100+5
                    x1 = x0 + 90
                    y1 = y0 + 90
                    if self.othellier.getMatrix()[x][y].getColor() == 0:
                        self.plateau.create_oval(x0+2, y0+2, x1+2, y1+2, fill='grey30', outline='')
                        self.plateau.create_oval(x0, y0, x1, y1, fill='black')
                    else:
                        self.plateau.create_oval(x0+2, y0+2, x1+2, y1+2, fill='grey30', outline='')
                        self.plateau.create_oval(x0, y0, x1, y1, fill='white')

          
    def maj_score(self):
        self.score_black.config(text=str(self.othellier._countPaws()[0]))
        self.score_white.config(text=str(self.othellier._countPaws()[1]))
        self.label3.config(text="Tour du joueur: "+self.color[self.othellier.getPlayer()])

    def win_lose(self,parent):
            if self.othellier.winner() == 0:
                self.bg.destroy()
                self.bg2.destroy()
                self.score_black.destroy()
                self.score_white.destroy()
                self.label.destroy()
                self.label2.destroy()
                self.label3.destroy()
                self.plateau.destroy()
                self.hint.destroy()
                self.all_hints.destroy()
                text="Le joueur noir a gagne!  \n Voulez vous rejouer?"
            elif self.othellier.winner() == 1:
                self.bg.destroy()
                self.bg2.destroy()
                self.score_black.destroy()
                self.score_white.destroy()
                self.label.destroy()
                self.label2.destroy()
                self.label3.destroy()
                self.plateau.destroy()
                self.hint.destroy()
                self.all_hints.destroy()
                text="Le joueur blanc a gagne! \n Voulez vous rejouez?"
            elif self.othellier.winner() == None:
                self.bg.destroy()
                self.bg2.destroy()
                self.score_black.destroy()
                self.score_white.destroy()
                self.label.destroy()
                self.label2.destroy()
                self.label3.destroy()
                self.plateau.destroy()
                self.hint.destroy()
                self.hint.destroy()
                text="C'est un match nul!  \n Voulez vous rejouez?"
            GameOver(self.parent,text)

    def play_move(self,couple):
        move=((couple[1]-couple[1]%100)//100,(couple[0]-couple[0]%100)//100)
        success,pawns=self.othellier.placePaw(move)
        if success:
            for pawn in pawns:
                self.draw(pawn)
            self.othellier.changePlayer()
        
    def draw(self,position):
        color='white' if self.othellier.player==1 else 'black'
        self.plateau.create_oval(position[1]*100+5,position[0]*100+5,position[1]*100+95,position[0]*100+95,fill=color)
    
    def ai_vs_player(self,couple):
        self.play_move(couple) 
        self.maj_score()
        self.update()
        time.sleep(0.1) 
        if self.othellier.player==1:
            ai= Computer(self.othellier)
            move=(ai.minimax(self.othellier,9))[1]
            if move:
                self.play_move((move[1]*100,move[0]*100))
        
    def click(self,event):
        self.delete_hints() 
        if self.mode=='jvsj':
            self.play_move((event.x,event.y))
        else:
            self.ai_vs_player((event.x,event.y))
        self.maj_score()
        if self.hint_all_game:
            self.show_hints()
        time.sleep(0.5)  
        if self.othellier.game_over():
            self.win_lose(self.parent)


class GameOver(tk.Frame):
    def __init__(self, parent,text):
        super().__init__(parent)
        self.parent=parent

        self.label = tk.Label(parent, text="Game Over" ,font=("Tiny5", 120),bg="#e6dbbe", justify=tk.CENTER)
        self.label.grid(row=0,column=0,columnspan=4)

        self.label2 = tk.Label(parent, text=text,font=("DM Serif Display", 40),bg="#e6dbbe", justify=tk.CENTER)
        self.label2.grid(row=1,column=0,columnspan=4)


        self.button_quit = tk.Button(parent, text = "Quitter", padx=20, pady=10, bd=5, font=("Helvetica", 14,"bold"),
                                    bg="#f0e6d6",fg="black",relief="raised",command = parent.quit)
        self.button_quit.grid(row=2, column=0, columnspan=2) 

        self.replay_button = tk.Button(parent, text="Rejouer",padx=20, pady=10, bd=5, font=("Helvetica", 14,"bold"),
                                    bg="#f0e6d6",fg="black",relief="raised",command = self.replay_game)
        self.replay_button.grid(row=2, column=1, columnspan=4)

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_rowconfigure(2, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_columnconfigure(2, weight=1)

    def replay_game(self):
        self.label.destroy()
        self.label2.destroy()
        self.button_quit.destroy()
        self.replay_button.destroy()
        MainMenu(self.parent)

    

if __name__ == '__main__': 
    vizualiser = Interface()
    vizualiser.mainloop()