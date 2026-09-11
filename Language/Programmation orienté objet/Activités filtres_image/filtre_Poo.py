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
print("#######################################")

choix = input(" Choisissez la transformation de votres image:")

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
  
