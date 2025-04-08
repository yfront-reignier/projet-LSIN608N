import tkinter as tk 
import numpy as np
import copy
from pion import Pion


class Othellier:
    def __init__(self):
        self.joueurs={1:'White',0:'Black'}
        self.player=0
        self.matrix=np.zeros((8,8),dtype=object)    
        self.matrix[3,3]=Pion(0,(3,3))
        self.matrix[3,4]=Pion(1,(3,4))
        self.matrix[4,3]=Pion(1,(4,3))
        self.matrix[4,4]=Pion(0,(4,4))
   
    def line_wise(self,w,y,z,matrix,elem,possibilite):
        k=z
        if y>z:
            while k>=0:
                if matrix[w,k]==0:
                    if (w,k) not in list(possibilite.values()):
                        possibilite[elem].append((w,k))
                    break
                elif matrix[w,k].GetColor()==self.player:
                    break
                k-=1
        #si pion opposé est a droite du pion du joueur   
        if y<z:
            while k<8:
                if matrix[w,k]==0:
                    if (w,k) not in list(possibilite.values()):
                        possibilite[elem].append((w,k))
                    break
                elif matrix[w,k].GetColor()==self.player:
                    break
                k+=1 
    
    def column_wise(self,x,w,z,matrix,elem,possibilite):
        if x>w:
            k=w
            while k>=0:
                if matrix[k,z]==0:
                    if (k,z) not in list(possibilite.values()):
                        possibilite[elem].append((k,z))
                    break
                elif matrix[k,z].GetColor()==self.player:
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
                elif matrix[k,z].GetColor()==self.player:
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
            elif matrix[k,l].GetColor()==self.player:
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
            elif matrix[k,l].GetColor()==self.player:
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
            elif matrix[k,l].GetColor()==self.player:
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
            elif matrix[k,l].GetColor()==self.player:
                break
        
            k-=1
            l+=1   
    
    def players_pawns(self,matrix,player):
        pawns=[]
        for i in range(8):
            for j in range(8):
                if matrix[i][j]!=0:
                    if matrix[i][j].GetColor()==player:
                        pawns.append((i,j))
        return pawns
    
    def opponent_neighbors(self,x,y,matrix):
        pawns=[]
        for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if (i>=0  and i<=7) and ( j>=0 and  j<=7) and matrix[i,j]!=0:
                        if matrix[i][j].GetColor()==(self.player+1)%2:
                            pawns.append((i,j))                  
        return pawns
    
    def jeu(self,matrix=None):
        if matrix is None:
            matrix=self.matrix
        pawns_list=self.players_pawns(matrix,self.player)
        possibilities={}
        
        for elem in pawns_list:
            possibilities[elem]=[]
            x,y=elem
            opponants_pawns=self.opponent_neighbors(x,y,matrix)
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
    def calculates_points_by_diagonal_1(self,x,y,w,z,counter):
        i=x
        j=y
        while i>=w and j>=z:
            counter+=1
            j-=1
            i-=1
        
    def calculates_points_by_diagonal_2(self,x,y,w,z,counter):
        i=x
        j=y
        while i<=w and j<=z:
            counter+=1
            j+=1
            i+=1
    def calculates_points_by_diagonal_3(self,x,y,w,z,counter):
        i=x
        j=y
        while i>=w and j<=z:
            counter+=1
            j+=1
            i-=1
    def calculates_points_by_diagonal_4(self,x,y,w,z,counter):
        i=x
        j=y
        while i>0 and i<=w and j>=z:
            counter+=1
            j-=1
            i+=1
        
    
    def points_calculation(self,coord1,coord2):
        x,y=coord1
        w,z=coord2 
        counter=-2
        self.calculates_points_by_line_or_column(x,y,w,z,counter)
        if x!=w and y!=z:
            if w<x and z<y:
                self.calculates_points_by_diagonal_1(x,y,w,z,counter)
            if w>x and z>y:
                self.calculates_points_by_diagonal_2(x,y,w,z,counter)
            if w<x and z>y:
                self.calculates_points_by_diagonal_3(x,y,w,z,counter)
            if w>x and z<y:
                self.calculates_points_by_diagonal_4(x,y,w,z,counter)
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
        
    def change_color_line(self,x,y,w,z,board):
        for i in range(min(x, w), max(x, w)+1):
            for j in range(min(z, y), max(z, y)+1):
                self.matrix[i][j].ChangeColor(self.player)
                self.draw_on_board((i,j),board)
        
    def change_color_diagonal_1(self,x,y,w,z,board):
        i=w
        j=z
        while i>0 and i<x and j<y:
            self.matrix[i][j].ChangeColor(self.player)
            self.draw_on_board((i,j),board)
            j+=1
            i+=1
    
    def change_color_diagonal_2(self,x,y,w,z,board):
        i=w
        j=z
        while i>x and j>y:
            self.matrix[i][j].ChangeColor(self.player)
            self.draw_on_board((i,j),board)
            j-=1
            i-=1
        
    
    def change_color_diagonal_3(self,x,y,w,z,board):
        i=x
        j=y
        while i>0 and i<w and j>z:
            self.matrix[i][j].ChangeColor(self.player)
            self.draw_on_board((i,j),board)
            j-=1
            i+=1

    def change_color_diagonal_4(self,x,y,w,z,board):
        i=w
        j=z
        while i>0 and i<x and j>y:
            self.matrix[i][j].ChangeColor(self.player)
            self.draw_on_board((i,j),board)
            j-=1
            i+=1


    def color_change(self,pos1,pos2,board):
        x,y=pos1 #coord du pion que l'on vient de placer
        w,z=pos2 #coord du deuxieme point encadrant
        if (x==w and y!=z) or (x!=w and y==z):
            self.change_color_line(x,y,w,z,board)
        if x!=w and y!=z:
            if w<x and z<y:
                self.change_color_diagonal_1(x,y,w,z,board)
            if w>x and z>y:
                self.change_color_diagonal_2(x,y,w,z,board)
            if w>x and z<y:
                self.change_color_diagonal_3(x,y,w,z,board)
            if x>w and y<z:
                self.change_color_diagonal_4(x,y,w,z,board)

    def draw_on_board(self,coord,board):
        y,x=coord
        board.create_oval(x*100,y*100,x*100+100,y*100+100,fill=self.joueurs[self.player])
    
    
    def click(self,board,couple,yellow_circles,mode):
        if self.player==0:
            self.draw_pawn(board,couple,yellow_circles,mode)
        else:
            if mode=='jvsj':
                self.draw_pawn(board,couple,yellow_circles,mode)
            else:
                x,y=self.choisir_coup(board)
                self.draw_pawn(board,(x,y),yellow_circles,mode)
            
    def draw_playable_pawns(self,yellow_circles,board,mode):
        for circle in yellow_circles:
            board.delete(circle)
        yellow_circles.clear()
        if self.player!=1 or mode!='jvsia':
            futur_pawns=self.jeu()
            for list in futur_pawns.values():
                for pawn in list:
                    px, py = pawn
                    circle = board.create_oval(py * 100 , px * 100 , py * 100 + 80, px * 100 + 80, outline='blue', width=3)
                    yellow_circles.append(circle)
      
    def draw_pawn(self,board,couple,yellow_circles,mode):
        if self.player==1 and mode=='jvsia':
            y,x=couple
        else:
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
            self.draw_on_board((y,x),board)
            self.matrix[y,x]=Pion(self.player,(y,x))
            self.color_change((y,x),elem,board)
        if possible:
            self.change_player()
            self.draw_playable_pawns(yellow_circles,board,mode)
        

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
        meilleur_coups = max(results, key=lambda k: results[k][1])

        return meilleur_coups
    
    def choisir_coup(self, board,profondeur=3):
        possibilites = self.jeu()
        scores = self.cost(possibilites)

        max_gain = max(scores.values())
        meilleur_coups = [move for move, value in scores.items() if value==max_gain]

        meilleur_coup = self.simulate_n_moves(meilleur_coups, profondeur)
        return meilleur_coup
        
        return meilleur_coup
    def verif_zero(self):
        for row in self.matrix:
            for elem in row:
                if elem==0:
                    return False
        return True
    
    def verif_poss(self):
        if not self.jeu():
            self.change_player()
            if not self.jeu():
                return True
        return False
    def getMatrix(self):
        return self.matrix

