import PIL.Image as Image


class Filtre:
    '''
    On veut changer la couleur de l'image Tigre
    '''

    def __init__(self, img):
        self._img = img
        self._pix = self._img.load()

    def size(self):
        return (self.width(), self.height())

    def width(self):
        return self._img.size[0]

    def height(self):
        return self._img.size[1]

    def weight(self):
        return self.width() * self.height()

    def get_pix(self, col, row):
        return self._pix[col, row]

    def reverse(self):
        """Passe l'image en négatif."""
        for x in range(self.width()):
            for y in range(self.height()):
                r, g, b = self._pix[x, y][:3]
                self._pix[x, y] = (255 - r, 255 - g, 255 - b)

    def red(self):
        """Conserve uniquement la composante rouge."""
        for x in range(self.width()):
            for y in range(self.height()):
                r, g, b = self._pix[x, y][:3]
                self._pix[x, y] = (r, 0, 0)

    def color2grey(self):
        """Transforme l'image couleur en image avec des nuances de gris."""
        for x in range(self.width()):
            for y in range(self.height()):
                r, g, b = self._pix[x, y][:3]
                gris = (r + g + b) // 3
                self._pix[x, y] = (gris, gris, gris)

    def threshold(self):
        """Transforme l'image en noir et blanc selon le seuil limit."""
        limit=128
        self.color2grey()
        for x in range(self.width()):
            for y in range(self.height()):
                gris = self._pix[x, y][0]
                if gris < limit:
                    self._pix[x, y] = (0, 0, 0)
                else:
                    self._pix[x, y] = (255, 255, 255)
    
    def symetrie_verticale(self):
        """Effectue une symétrie verticale (effet miroir gauche/droite)."""
        w = self.width()
        h = self.height()
        for x in range(w // 2):
            for y in range(h):
                pixel_gauche = self._pix[x, y]
                pixel_droite = self._pix[w - 1 - x, y]
                
                self._pix[x,y] = pixel_droite
                self._pix[w - 1 - x,y] = pixel_gauche
    
    def assombrire(self,factor):
        ''' On veut assombrire l'image'''
        for x in range(self.width()):
            for y in range(self.height()):
                r, g, b = self._pix[x, y][:3]
                r_new = max(0, r - factor)
                g_new = max(0, g - factor)
                b_new = max(0, b - factor)
                self._pix[x, y] = (r_new, g_new, b_new)
    
    def éclaircir(self,factor):
        '''On veut éclaircir l'image'''
        for x in range(self.width()):
            for y in range(self.height()):
                r, g, b = self._pix[x, y][:3]
                r_new = min(255, r + factor)
                g_new = min(255, g + factor)
                b_new = min(255, b + factor)
                self._pix[x, y] = (r_new, g_new, b_new)
    
    def show_image(self):
        return self._img.show()

# Accueil du menu
img = Image.open("tigre.jpg")
tigre = Filtre(img)

print("#######################################")
print("#           Menu d'image              #")
print("#######################################")

print("1 : Négatif")
print("2 : Rouge")
print("3 : Nuances de gris")
print("4 : Monochrome")
print("5 : Symetrie_verticale")
print("6 : Assombrire")
print("7 : Eclaircir")

print("#######################################")

choix = input(" Choisissez la transformation de votre image:")

if choix == "1":
    tigre.reverse()
    tigre.show_image()

elif choix == "2":
    tigre.red()
    tigre.show_image()

elif choix == "3":
    tigre.color2grey()
    tigre.show_image()

elif choix == "4":
    tigre.threshold()
    tigre.show_image()

elif choix == "5":
    tigre.symetrie_verticale()
    tigre.show_image()

elif choix == "6":
    factor = int(input("De combien voulez-vous assombrir ?"))
    tigre.assombrire(factor)
    tigre.show_image()

elif choix == "7":
    factor = int(input("De combien voulez-vous éclaircir ?"))
    tigre.éclaircir(factor)
    tigre.show_image()
  
