from maillon import Maillon
from random import randint

# Construction de la liste aléatoire fournie par le sujet
maListe = Maillon(10, None)
for i in range(10):
    maListe = Maillon(randint(0, 100), maListe)


# --- Q7 : longueur_liste ---
def longueur_liste(m):
    if m.suivant is None:
        return 1
    else:
        return 1 + longueur_liste(m.suivant)


# --- Q9 : test_valeur ---
def test_valeur(val, m):
    if m is None:
        return False
    if m.valeur == val:
        return True
    return test_valeur(val, m.suivant)


# --- Q11 : supprime_queue ---
def supprime_queue(m):
    if m is None or m.suivant is None:
        return None
    if m.suivant.suivant is None:
        m.suivant = None
    else:
        supprime_queue(m.suivant)


# --- Bloc de tests ---
m1 = Maillon(30, None)
m2 = Maillon(20, m1)
test_liste = Maillon(10, m2)

print("Liste de départ :", test_liste)
print("Longueur :", longueur_liste(test_liste))
print("Présence de 20 :", test_valeur(20, test_liste))
print("Présence de 99 :", test_valeur(99, test_liste))

supprime_queue(test_liste)
print("Après suppression queue :", test_liste)
print("Nouvelle longueur :", longueur_liste(test_liste))
