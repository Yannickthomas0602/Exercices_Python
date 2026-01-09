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
class Polygone : 
    #Associer à cette classe 4 objets  Ligne  correspondant aux lignes entre chacuns de ces points.
    def __init__(self, a, b, c, d) : 
        self.ligne_ab = Ligne(a, b)
        self.ligne_bc = Ligne(b, c)
        self.ligne_cd = Ligne(c, d)
        self.ligne_da = Ligne(d, a)
    def perimetre(self) : 
        return self.ligne_ab.get_length() + self.ligne_bc.get_length() + self.ligne_cd.get_length() + self.ligne_da.get_length()
    #Créer une méthode  draw  qui appelle la méthode  draw  de chacune des lignes
    def draw(self, paint) :
        self.ligne_ab.draw(paint)
        self.ligne_bc.draw(paint)
        self.ligne_cd.draw(paint)
        self.ligne_da.draw(paint)

# p = Polygone(Point(50,  300), Point(100,  50), Point(200, 150), Point(150, 250))
# p.draw(paint)

class Parallelogramme(Polygone) : 
    def __init__(self, a, b, c) :
        self.d = Point((c.x + (a.x - b.x)),(c.y + (a.y - b.y)))
        self.a = a
        self.b = b
        self.c = c
        Polygone.__init__(self, self.a, self.b, self.c, self.d)

# para = Parallelogramme(Point(50,  300), Point(100,  50), Point(200, 150))
# para.draw(paint)

class Rectangle(Parallelogramme) :
    def __init__(self, a, b, bc) :
        self.c = Point(((b.x + bc * ((a.y - b.y)/a.dist(b)))), (b.y - bc * ((a.x - b.x)/a.dist(b))))
        Parallelogramme.__init__(self, a, b, self.c)

# r = Rectangle(Point(50, 350), Point(80,  25), 800)
# r.draw(paint)

class Carre(Rectangle) : 
    def __init__(self, a, b) : 
         self.bc = a.dist(b)
         Rectangle.__init__(self, a, b, self.bc)

# c = Carre(Point(50, 350), Point(80,  25))
# c.draw(paint)

class Triangle :
        def __init__(self, a, b, c) : 
            self.ligne_ab = Ligne(a, b)
            self.ligne_bc = Ligne(b, c)
            self.ligne_ca = Ligne(c, a)
        def perimetre(self) : 
            return self.ligne_ab.get_length() + self.ligne_bc.get_length() + self.ligne_ca.get_length()
        def draw(self, paint) :
            self.ligne_ab.draw(paint)
            self.ligne_bc.draw(paint)
            self.ligne_ca.draw(paint)

# t = Triangle(Point(50,  300), Point(100,  50), Point(200, 150))
# t.draw(paint)

class Triangle_Rectangle(Triangle) : 
    def __init__(self, a, b, angle) :
        self.angle_rad = math.pi * angle / 180
        self.bc = a.dist(b) / math.cos(self.angle_rad)
        self.ac = self.bc * math.sin(self.angle_rad)
        self.c_x = a.x + self.ac * ((b.y - a.y ) / a.dist(b))
        self.c_y = a.y - self.ac * ((b.x - a.x ) / a.dist(b))
        self.c = Point(self.c_x, self.c_y)
        Triangle.__init__(self, a, b, self.c)

# tr = Triangle_Rectangle(Point(500,  500), Point(100,  50), 30)
# tr.draw(paint)

class Triangle_isocele(Triangle) : 
    def __init__(self, a, b, angle) : 
        self.m_x = (a.x + b.x) / 2
        self.m_y = (a.y + b.y) / 2
        self.m = Point(self.m_x, self.m_y)
        Triangle_Rectangle.__init__(self, self.m, b, angle)
        Triangle.__init__(self, a, b, self.c)

# iso = Triangle_isocele(Point(500,  500), Point(100,  50), 50)
# iso.draw(paint)

class Triangle_rect_iso(Triangle_isocele) :
    def __init__(self, a, b):
        Triangle_isocele.__init__(self, a, b, 45)

# rect_iso = Triangle_rect_iso(Point(400,  500), Point(100,  50))
# rect_iso.draw(paint)

class Triangle_equi(Triangle_isocele) : 
    def __init__(self, a, b) : 
        Triangle_isocele.__init__(self, a, b, 60)

# tr_equi = Triangle_equi(Point(800,  500), Point(100,  50))
# tr_equi.draw(paint)
# print(tr_equi.perimetre())



paint.show()


