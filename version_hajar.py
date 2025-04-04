import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import copy

joueurs={1:'white',0:'black'}



class Othellier:
    def __init__(self):
        self.compteur=0
        self.joueurs={1:'white',0:'black'}
        self.player=0
        self.matrice=np.zeros((8,8),dtype=object)
        self.matrice[3,3]=Pion(0,(3,3))
        self.matrice[3,4]=Pion(1,(3,4))
        self.matrice[3,2]=Pion(0,(3,2))
        self.matrice[5,4]=Pion(0,(5,4))
        self.matrice[4,3]=Pion(1,(4,3))
        self.matrice[4,4]=Pion(0,(4,4))
        # self.player=player
        
    
    def jeu(self,matrice=None):
        if matrice is None:
            matrice=self.matrice
        pions_atraiter=[]
        possibilite={}
        for i in range(8):
            for j in range(8):
                if matrice[i][j]!=0:
                    if matrice[i][j].get_couleur()==self.player:
                        pions_atraiter.append((i,j))
        for elem in pions_atraiter:
            possibilite[elem]=[]
            x,y=elem
            encercler=[]
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if (i>=0  and i<=7) and ( j>=0 and  j<=7) and matrice[i,j]!=0:
                        if matrice[i][j].get_couleur()==(self.player+1)%2:
                            encercler.append((i,j))
            for pb in encercler:
                w,z=pb
                # sur la meme ligne
                if x==w:
                    k=z
                    #si pion opposé est a gauche du pion du joueur
                    if y>z:
                        while k>=0:
                            if matrice[w,k]==0:
                                if (w,k) not in list(possibilite.values()):
                                    possibilite[elem].append((w,k))
                                break
                            elif matrice[w,k].get_couleur()==self.player:
                                break
                            k-=1
                    #si pion opposé est a droite du pion du joueur   
                    if y<z:
                        while k<8:
                            if matrice[w,k]==0:
                                if (w,k) not in list(possibilite.values()):
                                    possibilite[elem].append((w,k))
                                break
                            elif matrice[w,k].get_couleur()==self.player:
                                break
                            k+=1 
                
                # sur la meme colonne
                if y==z:
                    #pion oppose en dessous du pion du joueur
                    if x>w:
                        k=w
                        while k>=0:
                            if matrice[k,z]==0:
                                if (k,z) not in list(possibilite.values()):
                                    possibilite[elem].append((k,z))
                                break
                            elif matrice[k,z].get_couleur()==self.player:
                                break
                            k-=1
                    #pion oppose au dessus du pion du joueur  
                    if x<w:
                        k=w
                        while k<8:
                            if matrice[k,z]==0:
                                if (k,z) not in list(possibilite.values()):
                                    possibilite[elem].append((k,z) )
                                break
                            elif matrice[k,z].get_couleur()==self.player:
                                break
                            k+=1 
                # sur la diagonale
                #diagonale en haut a gauche  
                if x==w+1 and y==z+1:
                    k=w
                    l=z
                    while k>=0 and k<8 and l>=0 and l<8:
                        if matrice[k,l]==0:
                            if (k,l) not in list(possibilite.values()):
                                possibilite[elem].append((k,l))

                            break
                        elif matrice[k,l].get_couleur()==self.player:
                                break
                        
                        k-=1
                        l-=1
                    
                #digonale en bas a droite
                if x==w-1 and y==z-1:
                    k=w
                    l=z
                    while k>=0 and k<8 and l>=0 and l<8:
                        if matrice[k,l]==0:
                            if (k,l) not in list(possibilite.values()):
                                possibilite[elem].append((k,l))
                            break
                        elif matrice[k,l].get_couleur()==self.player:
                                break
                        k+=1
                        l+=1
                    
                #en bas a gauche
                if x==w-1 and y==z+1:
                    k=w
                    l=z
                    while k>=0 and k<8 and l>=0 and l<8:
                        if matrice[k,l]==0:
                            if (k,l) not in list( possibilite.values()):
                                possibilite[elem].append((k,l))
                            break
                        elif matrice[k,l].get_couleur()==self.player:
                                break
                        k+=1
                        l-=1
                #en haut a droite
                if x==w+1 and y==z-1:
                    k=w
                    l=z
                    while k>=0 and k<8 and l>=0 and l<8:
                        if matrice[k,l]==0:
                            if (k,l) not in list(possibilite.values()):
                                possibilite[elem].append((k,l))

                            break
                        elif matrice[k,l].get_couleur()==self.player:
                            break
                    
                        k-=1
                        l+=1
        return possibilite
    
    
    def calcul_points(self,coord1,coord2):
        x,y=coord1
        w,z=coord2 
        compteur=-2
        #meme ligne ou meme colonne
        if (x==w and y!=z) or (x!=w and y==z):
            for i in range(min(x, w), max(x, w)+1):
                for j in range(min(z, y), max(z, y)+1):
                    compteur+=1
        #diagonale
        if x!=w and y!=z:
            if w<x and z<y:
                #en haut a gauche
                i=x
                j=y
                while i>=w and j>=z:
                    compteur+=1
                    j-=1
                    i-=1
            # en bas a droite
            if w>x and z>y:
                i=x
                j=y
                while i<=w and j<=z:
                    compteur+=1
                    j+=1
                    i+=1
            # en haut a droite
            if w<x and z>y:
                i=x
                j=y
                while i>=w and j<=z:
                    compteur+=1
                    j+=1
                    i-=1
            #en bas a gauche
            if w>x and z<y:
                i=x
                j=y
                while i>0 and i<=w and j>=z:
                    compteur+=1
                    j-=1
                    i+=1
        return ((w,z),compteur)
    
    def cout(self,dico):
        dict={}
        for key,value in dico.items():
            for elem in value:
                cle,val=self.calcul_points(key,elem)
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
                    # print('j: ',j)
                    # print((i,j),'avant: ',self.matrice[i][j].get_couleur())
                    self.matrice[i][j]=Pion(self.player,(i,j))
                    # print((i,j),'apres: ',self.matrice[i][j].get_couleur())
                    self.dessine((i,j),plateau)
        #diagonale
        if x!=w and y!=z:
            if w<x and z<y:
                #diagonale en bas a droite
                i=w
                j=z
                while i>0 and i<x and j<y:
                    self.matrice[i][j]=Pion(self.player,(i,j))
                    self.dessine((i,j),plateau)
                    j+=1
                    i+=1
            # en haut a gauche
            if w>x and z>y:
                i=w
                j=z
                
                while i>x and j>y:
                    self.matrice[i][j]=Pion(self.player,(i,j))
                    self.dessine((i,j),plateau)
                    j-=1
                    i-=1
            # en haut a droite
            if w>x and z<y:
                i=x
                j=y
                while i>0 and i<w and j>z:
                    self.matrice[i][j]=Pion(self.player,(i,j))
                    self.dessine((i,j),plateau)
                    j-=1
                    i+=1
            #en bas a gauche
            if x>w and y<z:
                i=w
                j=z
                while i>0 and i<x and j>y:
                    self.matrice[i][j]=Pion(self.player,(i,j))
                    self.dessine((i,j),plateau)
                    j-=1
                    i+=1
        
    def dessine(self,coord,plateau):
        y,x=coord
        plateau.create_oval(x*100+35,y*100+35,x*100+65,y*100+65,fill=joueurs[self.player])

    def ecriture_matrice(self,msg,ind,compteur=None, matrice=None):
        if matrice is None :
            matrice=self.matrice
        if compteur is None:
            compteur=self.compteur
        nom='matrice'+str(ind)+".txt"
        with open(nom, "w") as f:
            f.write(msg+'\n')
            f.write(str(compteur)+'\n')
            for row in matrice:
                for val in row:
                    if val==0:
                        f.write(str(val))
                    else:
                        f.write(str(joueurs[val.get_couleur()][0].upper()))
                f.write('\n')
    
    def click(self,plateau,couple,yellow_circles):
        print('PLAYER IS',self.player)
        if self.player==0:
            self.dessine_pion(plateau,couple,yellow_circles)
        else:
            self.choisir_coup(plateau)
            self.change_player()
            self.dessin_possibilite(yellow_circles,plateau)
            
            
    def dessin_possibilite(self,yellow_circles,plateau):
        for circle in yellow_circles:
            plateau.delete(circle)
            
        # definir les cercles de possibilites
        yellow_circles.clear()
        futur_poss=self.jeu()
        for liste in futur_poss.values():
            for pion in liste:
                px, py = pion
                circle = plateau.create_oval(py * 100 + 35, px * 100 + 35, py * 100 + 65, px * 100 + 65, outline='yellow', width=3)
                yellow_circles.append(circle)
                
    def dessine_pion(self,plateau,couple,yellow_circles):
        x_non_arrondis,y_non_arrondis=couple
        x=(x_non_arrondis-x_non_arrondis%100)//100
        y=(y_non_arrondis-y_non_arrondis%100)//100
        poss=self.jeu()
        temp=[]
        possible=False
        for key,val in poss.items():   
            if (y,x) in val and self.matrice[y,x]==0:
                temp.append(key)
                possible=True
        for elem in temp:
            self.dessine((y,x),plateau)
            self.matrice[y,x]=Pion(self.player,(y,x))
            self.changement_couleur((y,x),elem,plateau)
        if possible:
            self.compteur+=1
            self.ecriture_matrice('je suis le vrai jeu',str(0))
            self.change_player()
            self.dessin_possibilite(yellow_circles,plateau)
        

    def simulation_recursive(self, mat, joueur, profondeur):
        coups_possibles = self.jeu(mat)
        cout_coups=self.cout(coups_possibles)

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
            temp = copy.deepcopy(self.matrice)
            temp[mvt] = Pion(self.player, mvt)
            score_final = self.simulation_recursive(temp, self.player, profondeur)
            results[mvt] = score_final
        print(results)
        meilleur_coups = max(results, key=lambda k: results[k][1])

        return meilleur_coups
    
    def choisir_coup(self, plateau,profondeur=3):
        print('flag')
        possibilites = self.jeu()
        scores = self.cout(possibilites)

        max_gain = max(scores.values())
        meilleur_coups = [move for move, value in scores.items() if value==max_gain]

        meilleur_coup = self.simulate_n_moves(meilleur_coups, profondeur)
        self.matrice[meilleur_coup]=Pion(1,meilleur_coup)
        self.dessine(meilleur_coup,plateau)
        
        return meilleur_coup
    
    def verif_zero(self):
        for i in self.matrice:
            for j in self.matrice:
                if self.matrice[i][j]==0:
                    return False
        return True
    
    def verif_poss(self):
        if not self.jeu():
            self.change_player()
            if not self.jeu():
                return True
        return False
        

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
    def __init__(self):
        self.root = tk.Tk()
        # self.othellier=othellier
        # self.yellow_circles=[]
        # self.canvas_pions={}
        
#         self.plateau = tk.Canvas(self.root, width=800, height=800, background='green')
#         self.plateau.grid(row=1, column=1)
#         self.plateau.bind("<Button-3>",self.click_to_draw)
#         # self.plateau.bind("<Button-1>", lambda event: othellier.dessine_pion(self.plateau, (event.x, event.y), self.yellow_circles))
#         # self.plateau.bind("<Button-1>", lambda event: othellier.dessine_pion(event, self.plateau, (event.x, event.y), self.yellow_circles))


        
#         self.matrice = othellier.matrice
#         self.joueurs = joueurs
#         self.dessiner_plateau()
        
#         self.root.grid_rowconfigure(0, weight=1)
#         self.root.grid_rowconfigure(1, weight=1)
#         self.root.grid_rowconfigure(2, weight=1)
#         self.root.grid_columnconfigure(0, weight=1)
#         self.root.grid_columnconfigure(1, weight=1)
#         self.root.grid_columnconfigure(2, weight=1)
        
#         self.root.mainloop()
    
#     def click_to_draw(self,event):
#         othellier.click(self.plateau,(event.x,event.y),self.yellow_circles)

#     def dessiner_plateau(self):
#         for i in range(1, 8):
#             self.plateau.create_line(i * 100, 0, i * 100, 800, width=3, fill='black')
#             self.plateau.create_line(0, i * 100, 800, i * 100, width=3, fill='black')
        
#         for ligne in self.matrice:
#             for elem in ligne:
#                 if elem != 0:
#                     y, x = elem.get_coordonnee()
#                     self.plateau.create_oval(x * 100 + 35, y * 100 + 35, x * 100 + 65, y * 100 + 65, fill=self.joueurs[elem.get_couleur()])
                    
#         possib=othellier.jeu()
#         for liste in possib.values():
#             for pion in liste:
#                 px, py = pion
#                 circle = self.plateau.create_oval(py * 100 + 35, px * 100 + 35, py * 100 + 65, px * 100 + 65, outline='yellow', width=3)
#                 self.yellow_circles.append(circle)
    def page_debut(self):
        self.root.title('Debut Othello')
        self.root.geometry("500x500")

        label = tk.Label(self.root, text="Othello",justify=tk.CENTER)
        label.grid(row=0,column=0, columnspan=4)
        label.config(font=("Arial", 20))
        
        image_fond = Image.open("othello.png")
        image_fond = image_fond.resize((500, 500))
        image_fond_tk = ImageTk.PhotoImage(image_fond)
        canvas = tk.Canvas(self.root, width=500, height=500)
        canvas.grid(row=0, column=0, rowspan=4, columnspan=3)
        canvas.create_image(0, 0, image=image_fond_tk, anchor="nw")
        canvas.image = image_fond_tk


        jvj_button = tk.Button(self.root,text="Joueur vs Joueur", command=start_jvj, padx=20, pady=10, font=("Arial", 10))
        jvj_button.grid(row=1,column=0,columnspan=2)

        jvc_button = tk.Button(self.root,text="Joueur vs IA",padx=20, pady=10, font=("Arial", 10))
        jvc_button.grid(row=1,column=1,columnspan=4)

        quitter_button = tk.Button(self.root,text="Quitter",command=self.root.quit, padx=20, pady=10, font=("Arial", 10))
        quitter_button.grid(row=2,column=0,columnspan=4)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.mainloop()



othellier=Othellier()
plateau_jeu=Interface(othellier,joueurs)
# print(othellier.jeu(othellier.player))
# othellier.choisir_coup()

