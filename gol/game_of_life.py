import os
import time
import random

def clear_screen_windows():
    os.system("cls")

def clear_screen_unix():
    os.system("clear")

def random_boolean():
    return bool(random.getrandbits(1))

class GameOfLife:
    def __init__(self, width=50, height=50):
        self.height = height
        self.width = width

        # Liste dont chaque élément est une cellule de la grille
        self.grid = []

    # Méthode affichant la grille du jeu de la vie
    def display(self):
        s = "┌" + ("─" * (self.width * 2)) + "┐\n"
        for idx in range(len(self.grid)):
            if idx % self.width == 0:
                s += "│"
            if self.grid[idx]:
                s += "▓▓"
            else:
                s += "  "
            if idx % self.width == self.width-1:
                s += "│\n"
        s += "└" + ("─" * (self.width * 2)) + "┘\n"
        print(s)

    # Récupère l'état d'une cellule en fonction de ses coordonnées x et y
    # Si la cellule est hors de la grille, retourne un état "mort"
    def get_cell(self, x, y):
        if x >= self.width or x < 0:
            return False
        elif y >= self.height or y < 0:
            return False
        else:
            ind = (y * self.width) + x
            return self.grid[ind]
