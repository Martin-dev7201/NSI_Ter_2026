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

def dechiffre_message(m, clef):
    """Déchiffre une liste d'entiers (ou un entier) avec la clé privée et renvoie une chaîne de caractères."""
    d, n = clef
    if isinstance(m, int):
        m = [m]
    resultat = ""
    for nombre in m:
        resultat += chr((d * nombre) % n)
    return resultat

assert dechiffre_message([325], (73, 537)) == 'a', "Erreur pour le déchiffrement du message"
assert dechiffre_message(325,(73, 537)) == 'a' , "Erreur pour le déchiffrement du message"
assert dechiffre_message(224766,(14557, 1004889)) + dechiffre_message(368006,(14557, 1004889)) + dechiffre_message(81526,(14557, 1004889)) == 'NSI', " Erreur de déchiffrement des 3 lettres"

def bruteForceKidRSA(e, n):
    """Renvoie le premier inverse de e modulo n, ou None s’il n’existe pas."""
    for d in range(1, n):
        if (e * d - 1) % n == 0:
            return d
    return None

e, n = 53447, 5185112
message1 = [3580949, 2084433, 3687843, 4436101, 4489548,
            1710304, 4329207, 4542995, 3901631, 1710304,
            4061972, 3687843, 1710304, 3527502, 4222313,
            4436101, 4436101, 1710304, 3687843, 4168866,
            1710304, 4168866, 4436101, 3901631, 1710304, 3367161]
d = bruteForceKidRSA(e, n)
assert d == 323639, "bruteForceKidRSA : clé privée incorrecte"
assert dechiffre_message(message1, (d, n)) == "C'EST QUI LE BOSS EN NSI ?", "dechiffre_message : premier message secret incorrect"


def pgcd(a, b):
    """Renvoie (g, x, y) tels que g = PGCD(a, b) et a*x + b*y = g."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = pgcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(e, n):
    """Renvoie l’inverse de e modulo n, ou False si aucun inverse n’existe."""
    g, x, y = pgcd(e, n)
    if g != 1:
        return False
    else:
        return x % n

e, n = 230884490440319, 194326240259798261076
message2 = [16623683311702968, 19625181687427115, 16392798821262649,
            16392798821262649, 20548719649188391, 7388303694090208,
            17547221273464244, 15931029840382011, 19163412706546477,
            7388303694090208, 15238376369061054, 18239874744785201,
            18008990254344882, 19163412706546477, 7388303694090208,
            19394297196986796, 19625181687427115, 20548719649188391,
            15007491878620735, 19625181687427115, 20317835158748072,
            7388303694090208, 7619188184530527]
d = modinv(e, n)
assert d == 158674832848565541575, "modinv : clé privée incorrecte"
assert dechiffre_message(message2, (d, n)) == "HUGGY LES BONS TUYAUX !", "dechiffre_message : deuxième message secret incorrect"

