# Programmation du chiffrement symétrique XOR
def chiffrement_XOR(message : str, cle : str):
    '''
    Chiffre le message avec cle par un chiffrement symétrique XOR
    cle doit être de taillle inférieure ou égale au message
    exemple:
    >>> chiffrement_XOR('NSI', 'CLE')
    '\r\x1f\x0c'
    '''
    resultat = ""

    for i in range(len(message)):
        a = ord(message[i])
        b = ord(cle[i % len(cle)])

        resultat += chr(a ^ b)

    return resultat

assert chiffrement_XOR('NSI', 'CLE') == '\r\x1f\x0c', "Erreur sur l'exemple NSI / CLE"

msg = "SPECIALITE NSI"
cle = "TERM"
assert chiffrement_XOR (msg, cle) == '\x07\x15\x17\x0e\x1d\x04\x1e\x04\x00\x00r\x03\x07\x0c', "Erreur sur l'exemple SPECIALITE NSI /TERM"
msg_chiffre = chiffrement_XOR(msg, cle)
assert chiffrement_XOR(msg_chiffre, cle) == msg, "Le déchiffrement ne redonne pas le message initial"

# Programmation du chiffrement asymétrique kidRSA

def genere_clefs_publique_et_privee (a1,b1,a2,b2):
    '''
    Génère et retourne la cle publique (e,n) et la clef secrète(d,n)
    à paritr des 4 entiers passés en paramètre a1,b1,a2,b2
    '''
    M = a1 * b1 - 1
    e = a2 * M + a1
    d = b2 * M + b1
    n = (e * d - 1) // M
    
    return (e,n) , (d,n)

assert genere_clefs_publique_et_privee (5,3,7,5) == ((103, 537), (73, 537)) , "Erreur pour obtenir les clefs publique et privee"

def chiffre_message(m,clef):
    '''
    Chiffre un message m qui est une chaîne de caractères avec la clef 'clef'
    en remplaçant chaque caractères par son code ASCII en décimal
    '''
    c = clef[0] * m % clef[1]
    return c

assert chiffre_message(ord('a'),(103,537)) == 325 , "Erreur pour le chiffrement du message"
assert chiffre_message(ord('N'), (28648, 1004889)) == 224766, "Erreur pour le chiffrement de la lettre 'N' "
assert chiffre_message(ord('S'), (28648, 1004889)) == 368006, "Erreur pour le chiffrement de la lettre 's' "
assert chiffre_message(ord('I'), (28648, 1004889)) == 81526, "Erreur pour le chiffrement de la lettre 'I' "

def dechiffre_message(m,clef):
    '''
    Déchiffre un message m qui est une liste de nombres
    et renvoie le message déchiffré sous la forme d'une chaîne de caractères 
    '''
    d = clef[0] * m % clef[1]
    return chr(d)

assert dechiffre_message(325,(73, 537)) == 'a' , "Erreur pour le déchiffrement du message"
assert dechiffre_message(224766,(14557, 1004889)) + dechiffre_message(368006,(14557, 1004889)) + dechiffre_message(81526,(14557, 1004889)) == 'NSI', " Erreur de déchiffrement des 3 lettres"
