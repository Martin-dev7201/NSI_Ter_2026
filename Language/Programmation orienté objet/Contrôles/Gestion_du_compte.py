class Compte:
    
    def __init__(self, nom, prenom, solde, num_compte):
        self.nom = nom
        self.prenom = prenom 
        self.solde = solde 
        self.num_compte = num_compte
        
    def __repr__(self):
        return(f"Le compte {self.num_compte} au de nom {self.nom} {self.prenom} à pour solde : {self.solde} euros.")
        
    def ajouter(self,a_solde):
        '''
        On veut verser de l'argent sur notre solde avec:
        a_solde = ajouter à la solde
        '''
        self.solde += a_solde
        return self.solde
    
    
    def débiter (self,d_solde):
        '''
        On veut verser de l'argent sur notre solde avec:
        d_solde = débiter à la solde
        Contrainte: la solde doit etre positive ou égale à 0 donc interdit qu'elle soit négative
        '''
        if self.solde >=0 :
            self.solde -= d_solde
            return self.solde
        else:
            print("Votre compte est dans le négatif, alors nous ne pouvons pas débiter")
            
    def get_solde (self):
        return (f"Votre solde est de {self.solde} euros")
    
    
com1 = Compte("DURAND", "Jacques", 300, 5284323539856531235)
print(com1)
print(com1.ajouter(700))
print(com1.débiter(200))
print(com1.get_solde())
