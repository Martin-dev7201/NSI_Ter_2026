
class ArbreBin :
    def __init__(self,d, gauche=None, droit=None) :
        '''Construit un arbre constituite d'un noeud d'étiquette d, d'un
        sous arbre gauche et un sous arbre droit.
        gauche = None et droit = None par defaut -> construction d'une feuille)'''
        self.__data = d
        self.__sag = gauche
        self.__sad = droit

    def __str__(self) :
        return '{'+str(self.__sag) +'_'+ '('+self.__data +')'+'_'+str(self.__sad)+'}'

    def __repr__(self) :
        return self.__str__()

    def est_feuille(self) :
        '''Retourne vrai si le noeud est une feuille'''
        return self.__sag == None and self.__sad==None

    def sag(self) :
        '''retourne le sous arbre gauche'''
        return self.__sag

    def sad(self) :
        '''retourne le sous arbre droit'''
        return self.__sad

    def noeud(self) :
        '''retourne l'etiquette du noeud'''
        return self.__data

    def nbr_noeuds(self):
        '''Renvoie le nombre de noeuds internes (sans feuille) d'un arbre binaire équilibré.
        '''
        if self.est_feuille():
            return 0
        n = 1
        if self.sag():
            n += self.sag().nbr_noeuds()
        if self.sad():
            n += self.sad().nbr_noeuds()

        return n

    def nbre_feuilles(self):
        '''Renvoie le nombre de feuilles d'un arbre binaire.'''
        if self.est_feuille():
            return 1

        n = 0
        if self.sag():
            n += self.sag().nbre_feuilles()
        if self.sad():
            n += self.sad().nbre_feuilles()

        return n

    def hauteur(self):
        '''Renvoie la hauteur de l'arbre binaire.'''
        if self.est_feuille():
            return 0

        hg = -1
        hd = -1

        if self.sag():
            hg = self.sag().hauteur()
        if self.sad():
            hd = self.sad().hauteur()

        return 1 + max(hg, hd)

    def feuilles(self):
        '''Renvoie la liste des étiquettes des feuilles de l'arbre.'''
        if self.est_feuille():
            return [self.noeud()]

        liste = []
        if self.sag():
            liste += self.sag().feuilles()
        if self.sad():
            liste += self.sad().feuilles()

        return liste


def creer_noeud(abr_lst,indice) :
    '''Convertir d'un arbre defini par une liste en un arbre de type AbreBin
    parametres : abr_lst -> Liste d'etiquettes des noeuds d'un arbre binaire
                 indice : indice dans la liste du noeud à creer
    sortie :     Arbre de type ArbreBin
    '''
    fg = abr_lst[2*indice+1]
    fd = abr_lst[2*indice+2]
    if fg is None and fd is None :
        return ArbreBin(abr_lst[indice])
    elif fg is None and fd is not None :
        return ArbreBin(abr_lst[indice], None, creer_noeud(abr_lst, 2*indice+2))
    elif fg is not None and fd is None :
        return ArbreBin(abr_lst[indice], creer_noeud(abr_lst, 2*indice+1), None)
    else :
        return ArbreBin(abr_lst[indice], creer_noeud(abr_lst, 2*indice+1), creer_noeud(abr_lst, 2*indice+2))


abr = creer_noeud(['N','Y', 'O', 'D', 'V', 'T', 'H', 'C','O', None,None,None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],0)

# Tests des méthodes de la classe ArbreBin

# Question 5 : Nombre de noeuds internes
print("Nombre de noeuds internes :", abr.nbr_noeuds())

# Question 6 : Nombre de feuilles
print("Nombre de feuilles :", abr.nbre_feuilles())

# Question 7 : Hauteur de l'arbre
print("Hauteur de l'arbre :", abr.hauteur())

# Question 8 : Liste des feuilles
print("Liste des feuilles :", abr.feuilles())
