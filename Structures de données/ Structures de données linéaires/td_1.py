class Pile:
    def __init__(self):
        self.__n = 20
        self.__p = [None] * self.__n
        self.__p[0] = 1
             
    def __repr__(self):
        liste = ''
        for i in range(self.__n):
            liste += str(self.__p[i])
        return liste
    
    def empiler(self, e):       
        self.__p[self.__p[0]] = e       
        self.__p[0] += 1      
    
    def depiler(self):
        self.__p[0] -=1
        valeur = self.__p[self.__p[0]]
        self.__p[self.__p[0]] = None
        return valeur
    
    def est_vide(self):
        return self.__p[0] == 1


class File:
    def __init__(self):
        self.__pile_entree = Pile()
        self.__pile_sortie = Pile()

    def est_vide(self):
        return (self.__pile_entree.est_vide()
                and self.__pile_sortie.est_vide())
    
    def file_empiler(self, x):
        self.__pile_entree.empiler(x)
    
    def file_depiler(self):
        if self.__pile_sortie.est_vide():
            while not self.__pile_entree.est_vide():
                self.__pile_sortie.empiler(self.__pile_entree.depiler())

        return self.__pile_sortie.depiler()
    
    def __repr__(self):
        return f"File({self.__pile_entree}, {self.__pile_sortie})"
