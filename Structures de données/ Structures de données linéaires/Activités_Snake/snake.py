from maillon import Maillon


class Snake:

    def __init__(self):
        self._position = Maillon((50, 30), None)
        self._orientation = "bas"

    def modifier_orientation(self, o: str):
        self._orientation = o

    def lire_orientation(self) -> str:
        return self._orientation

    def lire_positions(self) -> Maillon:
        return self._position

    def lire_tete(self) -> tuple:
        return self._position.valeur

    def _longueur(self, m: Maillon) -> int:
        if m is None:
            return 0
        if m.suivant is None:
            return 1
        return 1 + self._longueur(m.suivant)

    def taille(self) -> int:
        return self._longueur(self._position)

    def _in(self, val: tuple, m: Maillon) -> bool:
        if m is None:
            return False
        if m.valeur == val:
            return True
        return self._in(val, m.suivant)

    def est_mort(self) -> bool:
        if self._position is None or self._position.suivant is None:
            return False
        return self._in(self.lire_tete(), self._position.suivant)

    def ajout_tete(self):
        x, y = self.lire_tete()
        if self._orientation == "haut":
            nouvelle_tete = (x, y - 1)
        elif self._orientation == "bas":
            nouvelle_tete = (x, y + 1)
        elif self._orientation == "gauche":
            nouvelle_tete = (x - 1, y)
        elif self._orientation == "droite":
            nouvelle_tete = (x + 1, y)

        self._position = Maillon(nouvelle_tete, self._position)

    def _retirer_dernier(self, m: Maillon):
        if m is None or m.suivant is None:
            return
        if m.suivant.suivant is None:
            m.suivant = None
        else:
            self._retirer_dernier(m.suivant)

    def couper_queue(self):
        self._retirer_dernier(self._position)
