from math import *

class Point :
    '''Classe de definition d'un point en coordonnees
    polaires et cartesiennes
    '''
    def __init__(self, x, y) :
        self.__x = x
        self.__y = y
        self.__convertir_cart_polaire() 
        
    def __repr__(self):
        return f"Point(x={self.__x}, y={self.__y})"
    
    def lire_coord_cartesiennes(self) :
        return (self.__x, self.__y)
    
    def lire_coord_polaires(self) :
        return (self.__r, self.__theta)
    
    def __convertir_cart_polaire(self) :
        #Calcul de theta
        if self.__x > 0 : self.__theta = atan(self.__y/self.__x)
        elif self.__x < 0 and self.__y >=0 : self.__theta = atan(self.__y/self.__x) + pi
        elif self.__x < 0 and self.__y < 0 : self.__theta = atan(self.__y/self.__x) - pi
        elif self.__x == 0 and self.__y > 0 : self.__theta = pi/2
        elif self.__x == 0 and self.__y < 0 : self.__theta = -pi/2
        else : self.__theta = 0
        
        # Calcul de r
        self.__r = sqrt(self.__x**2 + self.__y**2)
            
...
A = Point(-2,5)
B = Point(5,5) 
C = Point(-2,-2)
D = Point(5,-2)

A.lire_coord_polaires()
B.lire_coord_polaires()
C.lire_coord_polaires()
D.lire_coord_polaires()
