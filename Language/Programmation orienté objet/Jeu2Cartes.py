import random
from carte import Carte  # Import de la classe Carte

class Jeu2Cartes:
    def __init__(self):
        self.jeu = self._construire_jeu()
        self.nbre_cartes = len(self.jeu)

    def _construire_jeu(self):
        """Construit une liste de 52 cartes ordonnées puis mélangées."""
        couleurs = ["carreau", "cœur", "pique", "trèfle"]
        cartes = []
        for val in range(2, 15):
            for coul in couleurs:
                cartes.append(Carte(val, coul))
        random.shuffle(cartes)
        return cartes

    def melanger_cartes(self):
        """Mélange l'ordre des éléments de la liste jeu."""
        random.shuffle(self.jeu)

    def rassembler_cartes(self):
        """Reconstitue un jeu complet de 52 cartes mélangées."""
        self.jeu = self._construire_jeu()
        self.nbre_cartes = len(self.jeu)

    def distribuer_carte(self):
        """Renvoie la première carte de la liste jeu et la retire."""
        if self.nbre_cartes > 0:
            self.nbre_cartes -= 1
            return self.jeu.pop(0)
        else:
            return("Le paquet de cartes est vide !")
