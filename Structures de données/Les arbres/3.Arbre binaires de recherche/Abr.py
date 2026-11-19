from ArbreBin import *

class Abr(ArbreBin) :
    '''Classe arbre binaire de recherche
    -> herite des methodes de ArbreBin'''
    
    def __init__(self,d, gauche=None, droit=None) :
        ArbreBin.__init__(self,d, gauche, droit)
    
    def __repr__(self):
        return (f"{self.noeud()}, {self.sag()}, {self.sad()}")
        
    def rechercher(self, n : int) :
        '''Recherche la presence de n dans l'arbre'''
        print('entree dans : ',self.noeud())
        if self.noeud() == n :
            return True
        elif self.noeud() > n :
            if self.sag() == None :
                return False
            else :
                return self.sag().rechercher(n)
        else :
            if self.sad() == None :
                return False
            else :
                return self.sad().rechercher(n)

    def inserer(self, n: int):
        '''Insere n dans l'arbre de recherche'''
        if n < self.noeud():
            if self.sag() is None:
                self.set_sag(Abr(n))
            else:
                self.sag().inserer(n)
        else:
            if self.sad() is None:
                self.set_sad(Abr(n))
            else:
                self.sad().inserer(n)
            
            
def test_rechercher_Abr(abr, list_tests, list_resultats) :
    ''' Test automatique de la méthode Abr.rechercher()
    abr : arbre de recherche
    list_tests : liste des valeurs (int) à rechercher
    list_resulats : lsite des resultats (booleens) attendus
    Retour : Pas de retour attendu -> Levée d'erreur par assertion si test faux'''
    for i in range(len(list_tests)):
        assert abr.rechercher(list_tests[i]) == list_resultats[i], "Erreur de recherche"
      
abr = Abr(35,Abr(20,Abr(10),Abr(25)),Abr(50,Abr(45),Abr(60)))

list_tests = [22,35,100]
list_resultats = [True, True, False]

abr.inserer(22)
test_rechercher_Abr(abr, list_tests, list_resultats)