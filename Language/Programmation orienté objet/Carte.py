class Carte :
    ''' Carte d'un jeu de 52 cartes
    '''
    
    def __init__(self, val, coul) :
        self.__valeur = val
        self.__couleur = coul
        self.__definir_figure()        
            
    def __repr__(self) :
        return self.__figure + ' de ' + self.__couleur
        
    def obtenir_couleur(self) :
        return self.__couleur
    
    def obtenir_valeur(self) :
        return self.__valeur
    
    def obtenir_figure(self) :
        return self.__figure
    
    def attribuer_couleur(self, coul) :
        self.__couleur = coul
        
    def attribuer_valeur(self, val) :
        self.__valeur = val
        self.__definir_figure()
        
    def __definir_figure(self) :
        if 1 < self.__valeur <= 10 : self.__figure = str(self.__valeur)
        elif self.__valeur == 11 : self.__figure = 'valet'
        elif self.__valeur == 12 : self.__figure = 'dame'
        elif self.__valeur == 13 : self.__figure = 'roi'
        elif self.__valeur == 14 : self.__figure = 'as'
        else : self.__figure = 'erreur'

#Q6:
carte1 = Carte(11,"trèfles")

#Q7:
carte1.obtenir_figure()

#Q8:
jeu_vide = [0]*52

#Q9:
couleurs = ["carreau", "cœur", "pique", "trèfle"]
jeu = []

for val in range(2, 15):
    for coul in couleurs:
        jeu.append(Carte(val, coul))
