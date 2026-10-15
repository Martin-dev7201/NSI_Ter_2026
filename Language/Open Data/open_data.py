import csv

file = open("bor_sigparkpub.csv")
table = list(csv.DictReader(file, delimiter=";"))
table = [dict(elem) for elem in table]
file.close()

total = 0
gratuit = 0
payant = 0

for elem in table:
    places = elem.get("nombre_de_places")
    nature = elem.get("nature")

    if places != "":
        places = int(places)
        total = total + places
        if nature == "Surface gratuit":
            gratuit += places
        elif nature == "Surface payant":
            payant += places

print(f"Nombre total de places : {total}")
print(f"Nombre de places gratuites : {gratuit}")
print(f"Nombre de places payantes : {payant}")

#------------------------------------------------------------------------#

import json, requests
url = "https://opendata.bordeaux-metropole.fr/api/explore/v2.1/catalog/datasets/leh-implantation-defibrillateurs-municipaux/records?limit=10"
reponse = requests.get(url, verify = True)
dico = reponse.json()
results = dico.get("results")
for record in results:
    adresse = record.get("adr_num")
    commune = record.get("adr_voie")
    print(adresse, commune)
print(f"Il y a {len(results)} defibrillateurs")


