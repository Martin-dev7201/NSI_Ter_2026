class GrapheM :
    '''Graphe represente par sa matrice d'adjacence,
    où les sommets sont les entiers o, 1, ..., n-1'''

    def __init__(self, n) :
        self.__n = n
        self.__adj = [[False] * n for _ in range(n)]
        
    def afficher(self):
        for s in range(self.__n):
            print(s, "->", end=" ")
            for v in self.voisins(s):
                print(v, end=" ")
            print()
    
    def ajouter_arete(self, s1, s2) :
        '''Ajoute un arc entre les sommets s1 et S2'''
        self.__adj[s1][s2] = True
        self.__adj[s2][s1] = True

    def supprimer_arete(self, s1, s2) :
        '''Supprimer un arc entre les sommets s1 et S2'''
        self.__adj[s1][s2] = False
        self.__adj[s2][s1] = False
        
    def degre(self,s):
        return len(self.voisins(s))
        
    def arete(self, s1, s2) :
        '''Indique la presence d'un arc ou non
        entre s1 et s2'''
        return self.__adj[s1][s2]
    
    def nb_aretes(self):
        nb = 0
        for s in range(self.__n):
            nb = nb + self.degre(s)
        return nb // 2

    def voisins(self, s) :
        '''Renvoie la liste des voisins de s'''
        v =[]
        for i in range(self.__n) :
            if self.arete(i, s) :
                v.append(i)
        return v
    
    def matrix_to_list(self,p):
        d = {}
        for nom, i in p.items():
            d[nom] = []
            for voisin in self.voisins(i):
                for nom_voisin, numero in p.items():
                    if numero == voisin:
                        d[nom].append(nom_voisin)
        return d
            

# Le dictionnaire des individus
p = {'Alban': 0,'Béatrice': 1,'Charles' : 2,'Déborah' : 3,'Eric':4,'Fatima':5,'Gérald':6,'Hélène':7}

g = GrapheM(8)
#Q3
g.ajouter_arete(p['Alban'],p['Béatrice'])
g.ajouter_arete(p['Alban'],p['Déborah'])
g.ajouter_arete(p['Alban'],p['Eric'])
g.ajouter_arete(p['Alban'],p['Fatima'])

g.ajouter_arete(p['Béatrice'],p['Charles'])
g.ajouter_arete(p['Béatrice'],p['Déborah'])
g.ajouter_arete(p['Béatrice'],p['Eric'])
g.ajouter_arete(p['Béatrice'],p['Gérald'])

g.ajouter_arete(p['Charles'],p['Déborah'])
g.ajouter_arete(p['Charles'],p['Hélène'])

g.ajouter_arete(p['Déborah'],p['Gérald'])

g.ajouter_arete(p['Fatima'],p['Gérald'])
g.ajouter_arete(p['Fatima'],p['Hélène'])

g.ajouter_arete(p['Gérald'],p['Hélène'])

#Q4

g.afficher
g.supprimer_arete(p['Alban'],p['Béatrice'])
g.degre(p['Alban'])
g.nb_aretes()
g.matrix_to_list()
