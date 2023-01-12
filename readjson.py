import json
import locale

with open('accounts.json', 'r') as f:
    data = json.load(f)

locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

menu_main1 = f"""
Sie koennen die Datenbank nach folgenden Kriterien filtern:
1) Kontostand
2) Alter
3) Beenden
Geben Sie entweder die Nummer oder das Attribut, nach dem Sie filtern wollen an.
"""

menu_main2 = f"""
Sie koennen die Datenbank nach folgenden Kriterien filtern:
1) Status
2) Kontostand
3) Alter
4) Augenfarbe
5) Name
6) Geschlecht
7) Firma
8) Email
9) Telefon
10) Adresse
11) Registrierungsdatum
12) Beenden
Geben Sie entweder die Nummer oder das Attribut, nach dem Sie filtern wollen an.
"""

ausgabe = f
"""
Name: {}
"""

def ausgabe_datensatz (ds):
    ausgabe = f"""
    id          {ds["_id"]}
    Name        {ds["name"]}
    Alter       {ds["age"]}
    Kontostand  {ds["balance"]}
    """
    print(ausgabe)


def filter_kontostand ():
    print("Person mit dem höchsten Kontostand")
    highest = ""
    first = True
    for dataset in data:
        if (first != True):
            if (float(locale.atof(dataset["balance"])) > float(locale.atof(highest["balance"]))):
                highest = dataset
        else:
            highest = dataset
            first = False

    ausgabe_datensatz(highest)

def filter_alter ():
    print("Alle Personen mit einem Alter über 25 Jahren:")
    for dataset in data:
        if (dataset["age"] > 25):
            ausgabe_datensatz(dataset)

while(True):
    print (menu_main1)
    user_in = input("Eingabe ")
    if (user_in == "1" or str.lower(user_in) == "kontostand"):
        filter_kontostand()
    elif (user_in == "2" or str.lower(user_in) == "alter"):
        filter_alter()    
    elif (user_in == "3" or str.lower(user_in) == "beenden"):
        break 

