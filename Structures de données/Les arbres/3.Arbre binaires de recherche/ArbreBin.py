class ArbreBin :
    def __init__(self,d, gauche=None, droit=None) :
        '''Construit un arbre binaire, constituite d'un noeud d'étiquette d, d'un
        sous arbre gauche et un sous arbre droit.
        gauche = None et droit = None par defaut -> construction d'une feuille)'''
        self.__data = d
        self.__sag = gauche
        self.__sad = droit
    
    def est_feuille(self) :
        '''Retourne vrai si le noeud est une feuille'''
        return self.__sag==None and self.__sad==None
    
    def sag(self) :
        '''retourne le sous arbre gauche'''
        return self.__sag
    
    def sad(self) :
        '''retourne le sous arbre droit'''
        return self.__sad

    def set_sag(self, noeud) :
        '''Insere un noeud dans le sous arbre gauche'''
        self.__sag = noeud
     
    def set_sad(self, noeud) :
        '''Insere un noeud dans le sous arbre droit'''
        self.__sad = noeud
        
    def noeud(self) :
        '''retorune l'etiquette du noeud'''
        return self.__data
    
    def nbre_feuilles(self) :
        ''' retourne le nombre de feuilles de l'arbre'''
        if self.est_feuille() :
            return 1
        elif self.sad() == None :
            return self.sag().nbre_feuilles()
        elif self.sag() == None :
            return self.sad().nbre_feuilles()        
        else :
            return self.sag().nbre_feuilles() + self.sad().nbre_feuilles()
        
    def nbre_noeuds(self, debug = False) :
        ''' retourne le nombre de noeuds de l'arbre'''
        if self.est_feuille() : return 0
        elif self.sad() == None :
            return self.sag().nbre_noeuds() + 1
        elif self.sag() == None :
            return self.sad().nbre_noeuds()  + 1 
        else :
            return 1 + self.sag().nbre_noeuds() + self.sad().nbre_noeuds()      

        
    def hauteur(self) :
        '''Renvoie la hauteur de l'arbre'''
        if self.est_feuille() :
            return 0
        elif self.sad() == None :
            return self.sag().hauteur() + 1
        elif self.sag() == None :
            return self.sad().hauteur()  + 1         
        else :
            return 1+ max(self.sag().hauteur(), self.sad().hauteur())
     
     
     

