import sys
import math
import matplotlib.pyplot as plt

DRAW_NSTEPS = 10240

# Canvas de pixel sur lequel vous pouvez dessiner
class Paint:
    def __init__(self, width=1000, height=1000):
        self.canvas = []
        for line in range(height):
            line_data = list()
            for col in range(width):
                line_data.append([255, 255, 255])
            self.canvas.append(line_data)

    # Modifie la valeur d'un pixel sur le canvas
    def set_pixel(self, x, y, r=0, g=0, b=0):
        if x < 0 or y < 0:
            return
        if y >= len(self.canvas):
            return
        if x >= len(self.canvas[y]):
            return

        self.canvas[y][x] = [r, g, b]

    # Affiche le résultat du canvas dans une fenêtre
    def show(self):
        plt.gca().invert_yaxis()
        plt.imshow(self.canvas)
        plt.show()
        sys.exit(0)

# Point sur le canvas
class Point:

    # Définit par ses coordonnées carthésiennes
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Calcule la distance avec un autre point
    def dist(self, autre):
        s =  (autre.x - self.x) ** 2
        s += (autre.y  - self.y) ** 2
        return math.sqrt(s)

# Classe représentant une ligne entre 2 points
class Ligne:
    # Chaque paramètre est un objet de la classe Point
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Longueur de cette ligne
    def get_length(self):
        return self.a.dist(self.b)

    # Dessiner l'objet sur le canvas de pixel
    # Méthode prenant en paramètre le canvas de pixels à afficher
    def draw(self, paint):
        dx = (self.b.x - self.a.x) / DRAW_NSTEPS
        dy = (self.b.y - self.a.y) / DRAW_NSTEPS

        x = float(self.a.x)
        y = float(self.a.y)
        for step in range(DRAW_NSTEPS):
            paint.set_pixel(int(round(x, 0)), int(round(y, 0)))
            x += dx
            y += dy

paint = Paint()

#### Début du sujet
### Définition de classes ici
class Polygone:
    def __init__(self, a, b, c, d):
        self.lab = Ligne(a, b)
        self.lbc = Ligne(b, c)
        self.lcd = Ligne(c, d)
        self.lda = Ligne(d, a)

    def draw(self, paint):
        self.lab.draw(paint)
        self.lbc.draw(paint)
        self.lcd.draw(paint)
        self.lda.draw(paint)

    def perimeter(self):
        return self.lab.get_length() + self.lbc.get_length() + self.lcd.get_length() + self.lda.get_length()

class Parallelogramme(Polygone):
    def __init__(self, a, b, c):
        dx = c.x + (a.x - b.x)
        dy = c.y + (a.y - b.y)
        print(dx, dy)
        d = Point(dx, dy)
        Polygone.__init__(self, a, b, c, d)

    def area(self):
        t = Triangle(self.lab.a, self.lab.b, self.lbc.b)
        return t.area() * 2

class Rectangle(Parallelogramme):
    def __init__(self, a, b, bc):
        ab = a.dist(b)
        cx = b.x + bc*((a.y - b.y) / ab)
        cy = b.y - bc*((a.x - b.x) / ab)
        c = Point(cx, cy)
        Parallelogramme.__init__(self, a, b, c)

class Carre(Rectangle):
    def __init__(self, a, b):
        bc = a.dist(b)
        Rectangle.__init__(self, a, b, bc)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = Ligne(a, b)
        self.bc = Ligne(b, c)
        self.ca = Ligne(c, a)

    def draw(self, paint):
        self.ab.draw(paint)
        self.bc.draw(paint)
        self.ca.draw(paint)

    def area(self):
        s = (self.ab.get_length() + self.bc.get_length() + self.ca.get_length()) / 2
        return math.sqrt(s * (s - self.ab.get_length()) * (s - self.bc.get_length()) * (s - self.ca.get_length()))

    def perimeter(self):
        return self.ab.get_length() + self.bc.get_length() + self.ca.get_length()

class TriangleRectangle(Triangle):
    def __init__(self, a, b, angle_deg):
        assert angle_deg < 90
        theta = (angle_deg * math.pi) / 180

        cb = a.dist(b) / math.cos(theta)
        ac = cb * math.sin(theta)

        dx = ((b.y - a.y) / a.dist(b)) * ac
        c_x = a.x + dx

        dy = ((b.x - a.x) / a.dist(b)) * ac
        c_y = a.y - dy

        Triangle.__init__(self, a, b, Point(c_x, c_y))

class TriangleIsocele(Triangle):
    def __init__(self, a, b, angle_deg):
        mid_point = Point(a.x + ((b.x - a.x) // 2), a.y + ((b.y - a.y) // 2))
        tri_rect = TriangleRectangle(mid_point, b, angle_deg)
        Triangle.__init__(self, a, b, tri_rect.c)

class TriangleRectangleIsocele(TriangleIsocele):
    def __init__(self, a, b):
        TriangleIsocele.__init__(self, a, b, 45)

class TriangleEquilateral(TriangleIsocele):
    def __init__(self, a, b):
        TriangleIsocele.__init__(self, a, b, 60)
### Instanciation d'objets géométriques ici
###

ti = TriangleIsocele(Point(300, 300), Point(500, 300), 45)
ti.draw(paint)

paint.show()
