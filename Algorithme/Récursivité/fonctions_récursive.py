def somme_positifs(tab):
    if tab == []:
        return 0
    
    premier = tab[0]
    reste = tab[1:]
    
    if premier > 0:
        return premier + somme_positifs(reste)
    else:
        return somme_positifs(reste)
    
def somme_chiffres(chaine):
    if chaine == "":
        return 0
    return int(chaine[0]) + somme_chiffres(chaine[1:])

def inverse_caractères(chaine):
    chaine_inverse = ""
    if len(chaine) == 1:
        return chaine
    else:
        chaine_inverse +=chaine[::-1]
    return chaine_inverse 
