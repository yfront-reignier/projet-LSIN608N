import tkinter as tk
import numpy as np



class Interface(tk.Tk):
    def __init__(self): 
        tk.Tk.__init__(self)
        self.create_config()

    def create_config(self):
        self.geometry('720x720')
        self.config = self.configure(bg = "#e6dbbe")
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton.pack()


    
    def show_grid(matrix):
        matrix = np.array()



if __name__ == '__main__': 
    vizualiser = Interface()
    vizualiser.mainloop()