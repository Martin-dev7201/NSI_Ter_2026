class Graphe_oriente_ls :
    '''Graphe decrit par un dictionnaire d'adjacence'''
    
    def __init__(self) :
        self.__adj = {}
    
    def __repr__(self) :
        out = ''
        for cle in self.__adj.keys() :
            out += cle + ' -> ' + str(self.__adj[cle])[1:-1] + '\n'
        return out            
    
    def ajouter_sommet(self,s) :
        if s not in self.__adj : self.__adj[s]=[]
        
    def ajouter_arc(self, s1, s2) :
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.__adj[s1].append(s2)
        
    def sommets(self) :
        return list(self.__adj.keys())
    
    def voisins(self, s) :
        return self.__adj[s]
    
    def predecesseurs(self):
        pred ={}
        for s in self.sommets():
            pred[s] = []
        for s in self.sommets():
            for v in self.voisins(s):
                pred[v].append(s)
        return pred
    
    def arc_existe(self, s1, s2):
        return s2 in self.voisin(s1)
    
def charge_arcs(graphe, arcs):
    for arc in arcs:
        graphe.ajouter_arc(arc[0], arc[1])
        
def amis_d_amis(graphe, pers):
    resultat = []
    for ami in graphe.voisins(pers):
        for ami_ami in graphe.voisins(ami):
            if ami_ami != pers and ami_ami not in resultat:
                resultat.append(ami_ami)

    return resultat

graphe = Graphe_oriente_ls()
arcs= [('Ana','Bob'),('Bob','Ana'),('Carl','Bob'),('Bob','Erol'),('Erol','Bob'),('Erol','Dora'),('Erol','Filo'),('Erol','Gab'),('Gab','Erol'),('Dora','Gab'),('Filo','Gab')]


