class Cercle:
    ''' Classe Cercle:
    Caractéristiques d'un cercle par rapport à son centre, son rayon et sa couleur
    '''
    def __init__(self, centre_x, centre_y, rayon, couleur):
        self.__x = centre_x
        self.__y = centre_y
        self.__rayon = rayon
        self.__couleur = couleur
        
    def __repr__(self):
        return f"Cercle(centre=({self.__x}, {self.__y}), rayon={self.__rayon}, couleur='{self.__couleur}')"
    
    def deplacer(self, dx, dy):
        self.__x += dx
        self.__y += dy
    
    def obt_centre(self):
        return (self.__x, self.__y)
        
    def change_couleur(self, nouvelle_couleur):
        self.__couleur = nouvelle_couleur
        
    def obt_couleur(self):
        return self.__couleur
    
#Q2 à Q8
>>> cercle_1 = Cercle(3,7,1,"rouge")
>>> cercle_1.deplacer(4,2)
>>> cercle_1.obt_centre()
(7, 9)
>>> cercle_1.change_couleur("green")
>>> cercle_1.obt_couleur()
'green'
