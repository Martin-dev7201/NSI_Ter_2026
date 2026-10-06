class Compte:
    def __init__(self, nom, prenom, num_compte):
        self.solde = 0.0
        self.nom = nom
        self.prenom = prenom
        self.num_compte = num_compte

    def __str__(self):
        return (
            f"Nom : {self.nom}\n"
            f"Prénom : {self.prenom}\n"
            f"Solde : {self.solde}"
        )

    def ajouter(self, montant):
        self.solde += montant

    def debiter(self, montant):
        if self.solde >= montant:
            self.solde -= montant
        else:
            print("Solde insuffisant : retrait impossible.")

    def get_solde(self):
        return self.solde


com1 = Compte("DURAND", "Jacques", 5284323539856531235)
com1.ajouter(500)
com1.debiter(200)
print(com1.get_solde())
