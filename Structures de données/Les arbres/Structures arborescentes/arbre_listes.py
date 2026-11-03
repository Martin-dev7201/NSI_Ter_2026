
def creation_arbre(r,profondeur):
    ''' r : racine de l'arbre (str ou int)
    profondeur : profondeur de l’arbre (int)'''
    arbre = [r]+[None for i in range(2**(profondeur+1)-2)]
    return arbre

def insertion_noeud(arbre,n,fg,fd):
    '''Insére les noeuds et leurs enfants dans l’arbre.'''
    indice = arbre.index(n)
    arbre[2*indice+1] = fg
    arbre[2*indice+2] = fd

def parent(arbre,p):
    '''Retourne le parent du noeud p de l'arbre.'''
    if est_racine(arbre,p) :
        return None
    if p in arbre:
        indice = arbre.index(p)
        if indice%2 == 0:
            return arbre[(indice-2)//2]
        else:
            return arbre[(indice-1)//2]

def est_vide(arbre):
    '''Retourne True si l'arbre est vide.'''
    return arbre[0] is None

def enfants(arbre, n):
    '''Retourne les enfants du noeud n.'''
    indice = arbre.index(n)
    fg = 2*indice + 1
    fd = 2*indice + 2
    
    enfants_noeud =[]
    
    if fg < len(arbre) and arbre[fg] is not None:
        enfants_noeud.append(arbre[fg])
    if fd < len(arbre) and arbre[fd] is not None:
        enfants_noeud.append(arbre[fd])

    return enfants_noeud

def fils_gauche(arbre, n):
    '''Retourne le fils gauche du noeud n s'il existe.'''
    indice = arbre.index(n)
    fg = 2*indice + 1
    
    if fg < len(arbre):
        return arbre[fg]
    return None
    
def fils_droit(arbre, n):
    '''Retourne le fils droit du noeud n s'il existe.'''
    indice = arbre.index(n)
    fd = 2*indice + 2
    
    if fd < len(arbre):
        return arbre[fd]
    return None

def est_racine(arbre, n):
    '''Retourne True si n est la racine.'''
    if est_vide(arbre):
        return False
    return arbre[0] == n
    
def est_feuille(arbre,n):
    '''Retourne True si n est une feuille.'''
    return fils_gauche(arbre, n) is None and fils_droit(arbre, n) is None

def a_un_frere(arbre,n):
    '''Retourne True si n a un frère gauche ou droit'''
    indice = arbre.index(n)
    if indice == 0:
        return False
    
    if indice % 2 == 1:
        indice_frere = indice + 1
    else:
        indice_frere = indice -1
    
    return indice_frere < len(arbre) and arbre[indice_frere] is not None

# création de l’arbre
arbre = creation_arbre("r",3)

# ajout des noeuds par niveau de gauche à droite
insertion_noeud(arbre,"r","a","b")
insertion_noeud(arbre,"a","c","d")
insertion_noeud(arbre,"b","e","f")
insertion_noeud(arbre,"c",None,"h")
insertion_noeud(arbre,"d","i","j")
insertion_noeud(arbre,"e","k",None)
insertion_noeud(arbre,"f",None,None)

# Teste Q4 page 4/4
print(f"Liste est vide : {est_vide(arbre)}")
# Réponse = False
print(f"Le noeud r a pour enfants : {enfants(arbre, 'r')}")
# Réponse = ['a', 'b']
print(f"Le fils gauche du noeud r : {fils_gauche(arbre, 'r')}")
# Réponse = 'a'
print(f"Le fils droit du noeud r : {fils_droit(arbre, 'r')}")
# Réponse = 'b'
print(f"Est-ce que 'r' est la racine de l'arbre : {est_racine(arbre, 'r')}")
# Réponse = True
print(f"Est-ce que le noeud 'h' est une feuille : {est_feuille(arbre, 'h')}")
# Réponse = True
print(f"Est-ce que le noeud 'a' a un frère gauche ou droit : {a_un_frere(arbre, 'a')}")
# Réponse = True
