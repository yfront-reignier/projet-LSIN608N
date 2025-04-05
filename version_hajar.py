import tkinter as tk 
import numpy as np
import copy

joueurs={1:'white',0:'black'}



class Othellier:
    def __init__(self):
        self.compteur=0
        self.joueurs={1:'white',0:'black'}
        self.player=0
        self.matrix=np.zeros((8,8),dtype=object)
        self.matrix[3,3]=Pion(0,(3,3))
        self.matrix[3,4]=Pion(1,(3,4))
        self.matrix[3,2]=Pion(0,(3,2))
        self.matrix[5,4]=Pion(0,(5,4))
        self.matrix[4,3]=Pion(1,(4,3))
        self.matrix[4,4]=Pion(0,(4,4))
        
    def line_wise(self,w,y,z,matrix,elem,possibilite):
        k=z
        #si pion opposé est a gauche du pion du joueur
        if y>z:
            while k>=0:
                if matrix[w,k]==0:
                    if (w,k) not in list(possibilite.values()):
                        possibilite[elem].append((w,k))
                    break
                elif matrix[w,k].get_couleur()==self.player:
                    break
                k-=1
        #si pion opposé est a droite du pion du joueur   
        if y<z:
            while k<8:
                if matrix[w,k]==0:
                    if (w,k) not in list(possibilite.values()):
                        possibilite[elem].append((w,k))
                    break
                elif matrix[w,k].get_couleur()==self.player:
                    break
                k+=1 
    
    def column_wise(self,x,w,z,matrix,elem,possibilite):
        #pion oppose en dessous du pion du joueur
        if x>w:
            k=w
            while k>=0:
                if matrix[k,z]==0:
                    if (k,z) not in list(possibilite.values()):
                        possibilite[elem].append((k,z))
                    break
                elif matrix[k,z].get_couleur()==self.player:
                    break
                k-=1
        #pion oppose au dessus du pion du joueur  
        if x<w:
            k=w
            while k<8:
                if matrix[k,z]==0:
                    if (k,z) not in list(possibilite.values()):
                        possibilite[elem].append((k,z) )
                    break
                elif matrix[k,z].get_couleur()==self.player:
                    break
                k+=1
    
    def diagonal_wise_1(self,w,z,matrix,elem,possibilite):
        k=w
        l=z
        while k>=0 and k<8 and l>=0 and l<8:
            if matrix[k,l]==0:
                if (k,l) not in list(possibilite.values()):
                    possibilite[elem].append((k,l))

                break
            elif matrix[k,l].get_couleur()==self.player:
                    break
            
            k-=1
            l-=1
    def diagonal_wise_2(self,w,z,matrix,elem,possibilite):
        k=w
        l=z
        while k>=0 and k<8 and l>=0 and l<8:
            if matrix[k,l]==0:
                if (k,l) not in list(possibilite.values()):
                    possibilite[elem].append((k,l))
                break
            elif matrix[k,l].get_couleur()==self.player:
                    break
            k+=1
            l+=1
    def diagonal_wise_3(self,w,z,matrix,elem,possibilite):
        k=w
        l=z
        while k>=0 and k<8 and l>=0 and l<8:
            if matrix[k,l]==0:
                if (k,l) not in list( possibilite.values()):
                    possibilite[elem].append((k,l))
                break
            elif matrix[k,l].get_couleur()==self.player:
                    break
            k+=1
            l-=1
    def diagonal_wise_4(self,w,z,matrix,elem,possibilite):
        k=w
        l=z
        while k>=0 and k<8 and l>=0 and l<8:
            if matrix[k,l]==0:
                if (k,l) not in list(possibilite.values()):
                    possibilite[elem].append((k,l))

                break
            elif matrix[k,l].get_couleur()==self.player:
                break
        
            k-=1
            l+=1   
    
    def players_pawns(self,matrix):
        pawns=[]
        for i in range(8):
            for j in range(8):
                if matrix[i][j]!=0:
                    if matrix[i][j].get_couleur()==self.player:
                        pawns.append((i,j))
        return pawns
    
    def find_opponants_pawns(self,x,y,matrix):
        pawns=[]
        for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if (i>=0  and i<=7) and ( j>=0 and  j<=7) and matrix[i,j]!=0:
                        if matrix[i][j].get_couleur()==(self.player+1)%2:
                            pawns.append((i,j))
                            
        return pawns
    
    def jeu(self,matrix=None):
        if matrix is None:
            matrix=self.matrix
        pawns_list=self.players_pawns(matrix)
        possibilities={}
        
        for elem in pawns_list:
            possibilities[elem]=[]
            x,y=elem
            opponants_pawns=self.find_opponants_pawns(x,y,matrix)
            for pb in opponants_pawns:
                w,z=pb
                if x==w:
                    self.line_wise(w,y,z,matrix,elem,possibilities)
                if y==z:
                    self.column_wise(x,w,z,matrix,elem,possibilities) 
                if x==w+1 and y==z+1:
                    self.diagonal_wise_1(w,z,matrix,elem,possibilities)       
                if x==w-1 and y==z-1:
                    self.diagonal_wise_2(w,z,matrix,elem,possibilities)
                if x==w-1 and y==z+1:
                    self.diagonal_wise_3(w,z,matrix,elem,possibilities)
                if x==w+1 and y==z-1:
                    self.diagonal_wise_4(w,z,matrix,elem,possibilities)
        return possibilities
    
    
    def calculates_points_by_line_or_column(self,x,y,w,z,counter):
        if (x==w and y!=z) or (x!=w and y==z):
            for i in range(min(x, w), max(x, w)+1):
                for j in range(min(z, y), max(z, y)+1):
                    counter+=1
        return counter
    def calculates_points_by_diagonal_1(self,x,y,w,z,counter):
        i=x
        j=y
        while i>=w and j>=z:
            counter+=1
            j-=1
            i-=1
        return counter
        
    def calculates_points_by_diagonal_2(self,x,y,w,z,counter):
        i=x
        j=y
        while i<=w and j<=z:
            counter+=1
            j+=1
            i+=1
        return counter
    def calculates_points_by_diagonal_3(self,x,y,w,z,counter):
        i=x
        j=y
        while i>=w and j<=z:
            counter+=1
            j+=1
            i-=1
        return counter
    def calculates_points_by_diagonal_4(self,x,y,w,z,counter):
        i=x
        j=y
        while i>0 and i<=w and j>=z:
            counter+=1
            j-=1
            i+=1
        return counter
        
    
    def points_calculation(self,coord1,coord2):
        x,y=coord1
        w,z=coord2 
        counter=-2
        #meme ligne ou meme colonne
        if x==w or y==z:
            counter+=self.calculates_points_by_line_or_column(x,y,w,z,counter)
        #diagonale
        if x!=w and y!=z:
            if w<x and z<y:
                counter+=self.calculates_points_by_diagonal_1(x,y,w,z,counter)
            if w>x and z>y:
                counter+=self.calculates_points_by_diagonal_2(x,y,w,z,counter)
            if w<x and z>y:
                counter+=self.calculates_points_by_diagonal_3(x,y,w,z,counter)
            if w>x and z<y:
                counter+=self.calculates_points_by_diagonal_4(x,y,w,z,counter)
        return ((w,z),counter)
    
    def cost(self,dico):
        dict={}
        for key,value in dico.items():
            for elem in value:
                cle,val=self.points_calculation(key,elem)
                dict[cle]=val
        return dict  
    
    def change_player(self):
        self.player=(self.player+1)%2
    
    def changement_couleur(self,coord1,coord2,plateau):
        x,y=coord1[0],coord1[1]  #coord du pion que l'on vient de placer
        w,z=coord2 #coord du deuxieme point encadrant
        #meme ligne ou meme colonne
        if (x==w and y!=z) or (x!=w and y==z):
            for i in range(min(x, w), max(x, w)+1):
                # print('i: ',i)
                for j in range(min(z, y), max(z, y)+1):
                    self.matrix[i][j]=Pion(self.player,(i,j))
                    self.dessine((i,j),plateau)
        #diagonale
        if x!=w and y!=z:
            if w<x and z<y:
                #diagonale en bas a droite
                i=w
                j=z
                while i>0 and i<x and j<y:
                    self.matrix[i][j]=Pion(self.player,(i,j))
                    self.dessine((i,j),plateau)
                    j+=1
                    i+=1
            # en haut a gauche
            if w>x and z>y:
                i=w
                j=z
                
                while i>x and j>y:
                    self.matrix[i][j]=Pion(self.player,(i,j))
                    self.dessine((i,j),plateau)
                    j-=1
                    i-=1
            # en haut a droite
            if w>x and z<y:
                i=x
                j=y
                while i>0 and i<w and j>z:
                    self.matrix[i][j]=Pion(self.player,(i,j))
                    self.dessine((i,j),plateau)
                    j-=1
                    i+=1
            #en bas a gauche
            if x>w and y<z:
                i=w
                j=z
                while i>0 and i<x and j>y:
                    self.matrix[i][j]=Pion(self.player,(i,j))
                    self.dessine((i,j),plateau)
                    j-=1
                    i+=1
        
    def dessine(self,coord,plateau):
        y,x=coord
        plateau.create_oval(x*100+35,y*100+35,x*100+65,y*100+65,fill=joueurs[self.player])

    def ecriture_matrix(self,msg,ind,compteur=None, matrix=None):
        if matrix is None :
            matrix=self.matrix
        if compteur is None:
            compteur=self.compteur
        nom='matrix'+str(ind)+".txt"
        with open(nom, "w") as f:
            f.write(msg+'\n')
            f.write(str(compteur)+'\n')
            for row in matrix:
                for val in row:
                    if val==0:
                        f.write(str(val))
                    else:
                        f.write(str(joueurs[val.get_couleur()][0].upper()))
                f.write('\n')
    
    def click(self,plateau,couple,yellow_circles):
        if self.player==0:
            self.dessine_pion(plateau,couple,yellow_circles)
        else:
            self.choisir_coup(plateau)
            self.change_player()
            self.drawn_playable_pawns(yellow_circles,plateau)
            
            
    def drawn_playable_pawns(self,yellow_circles,plateau):
        for circle in yellow_circles:
            plateau.delete(circle)
        yellow_circles.clear()
        futur_pawns=self.jeu()
        for list in futur_pawns.values():
            for pawn in list:
                px, py = pawn
                circle = plateau.create_oval(py * 100 + 35, px * 100 + 35, py * 100 + 65, px * 100 + 65, outline='yellow', width=3)
                yellow_circles.append(circle)
                
    def draw_pawn(self,board,couple,yellow_circles):
        x=(couple[0]-couple[0]%100)//100
        y=(couple[1]-couple[1]%100)//100
        possibilities=self.jeu()
        temp=[]
        possible=False
        for key,val in possibilities.items():   
            if (y,x) in val and self.matrix[y,x]==0:
                temp.append(key)
                possible=True
        for elem in temp:
            self.dessine((y,x),board)
            self.matrix[y,x]=Pion(self.player,(y,x))
            self.changement_couleur((y,x),elem,board)
        if possible:
            self.compteur+=1
            self.change_player()
            self.drawn_playable_pawns(yellow_circles,board)
        

    def simulation_recursive(self, mat, joueur, profondeur):
        coups_possibles = self.jeu(mat)
        cout_coups=self.cost(coups_possibles)

        meilleures_cout = {mvt:cout for mvt, cout in cout_coups.items() if cout==max(cout_coups.values())}
        
        if profondeur == 1: # s arrete a un pour avoir un nombre impaire d'iteration donc on finit sur cout de ia
            return meilleures_cout  

        futur_joueur = (joueur + 1)%2  
        
        meilleur_res = {1:float('-inf') , 0: float('inf')}
        for mvt in meilleures_cout.keys():
            temp = copy.deepcopy(mat)
            temp[mvt] = Pion(joueur, mvt)
            score = self.simulation_recursive(temp, futur_joueur, profondeur - 1)
            if joueur == 1 and score:  
                meilleur_res[1] = max(meilleur_res[1], max(score.values()))
            elif joueur==0 and score:  
                meilleur_res[0] = min(meilleur_res[0], min(score.values()))
        return meilleur_res
    
    def simulate_n_moves(self, meilleur_mvt, profondeur):
        results = {}
        for mvt in meilleur_mvt:
            temp = copy.deepcopy(self.matrix)
            temp[mvt] = Pion(self.player, mvt)
            score_final = self.simulation_recursive(temp, self.player, profondeur)
            results[mvt] = score_final
        print('res',results)
        meilleur_coups = max(results, key=lambda k: results[k][1])

        return meilleur_coups
    
    def choisir_coup(self, plateau,profondeur=3):
        print('flag')
        possibilites = self.jeu()
        scores = self.cost(possibilites)

        max_gain = max(scores.values())
        meilleur_coups = [move for move, value in scores.items() if value==max_gain]

        meilleur_coup = self.simulate_n_moves(meilleur_coups, profondeur)
        self.matrix[meilleur_coup]=Pion(1,meilleur_coup)
        self.dessine(meilleur_coup,plateau)
        
        return meilleur_coup


class Pion():
    def __init__(self,couleur,coord):
        self.couleur=couleur
        self.coordonnee=coord
    def get_couleur(self):
        return self.couleur
    def change_couleur(self,nv_couleur):
        self.couleur=nv_couleur
    def get_coordonnee(self):
        return self.coordonnee



class Interface():
    def __init__(self,othellier, joueurs):
        self.root = tk.Tk()
        self.root.title("Othello")
        self.othellier=othellier
        self.yellow_circles=[]
        self.canvas_pions={}
        
        self.plateau = tk.Canvas(self.root, width=800, height=800, background='green')
        self.plateau.grid(row=1, column=1)
        self.plateau.bind("<Button-3>",self.click_to_draw)
        # self.plateau.bind("<Button-1>", lambda event: othellier.dessine_pion(self.plateau, (event.x, event.y), self.yellow_circles))
        # self.plateau.bind("<Button-1>", lambda event: othellier.dessine_pion(event, self.plateau, (event.x, event.y), self.yellow_circles))


        
        self.matrix = othellier.matrix
        self.joueurs = joueurs
        self.dessiner_plateau()
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        
        self.root.mainloop()
    
    def click_to_draw(self,event):
        othellier.click(self.plateau,(event.x,event.y),self.yellow_circles)
    def dessiner_plateau(self):
        for i in range(1, 8):
            self.plateau.create_line(i * 100, 0, i * 100, 800, width=3, fill='black')
            self.plateau.create_line(0, i * 100, 800, i * 100, width=3, fill='black')
        
        for ligne in self.matrix:
            for elem in ligne:
                if elem != 0:
                    y, x = elem.get_coordonnee()
                    self.plateau.create_oval(x * 100 + 35, y * 100 + 35, x * 100 + 65, y * 100 + 65, fill=self.joueurs[elem.get_couleur()])
                    
        possib=othellier.jeu()
        for liste in possib.values():
            for pion in liste:
                px, py = pion
                circle = self.plateau.create_oval(py * 100 + 35, px * 100 + 35, py * 100 + 65, px * 100 + 65, outline='yellow', width=3)
                self.yellow_circles.append(circle)


othellier=Othellier()
plateau_jeu=Interface(othellier,joueurs)
# print(othellier.jeu(othellier.player))
# othellier.choisir_coup()

