class Maillon :
    ''' Classe Maillon, element de base d une liste chainee
    attributs publiques : 
            valeur : valeur du maillon
            suivant : maillon suivant (type Maillon)
    '''
    
    def __init__(self, val, suivant) :
        self.valeur = val
        self.suivant = suivant
    
    def __str__(self) :
        rep = '<'+str(self.valeur)+ '>' 
        if self.suivant is not None : rep += str(self.suivant)
        return rep
    
    def __repr__(self) :
        return self.__str__()
    
