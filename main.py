from puntensysteem import Puntensysteem
import excelreader
from operator import attrgetter

naam = input("Hallo gebruiker, hoe heet je?")
quote_amount = 3  # Hoeveel quotes we willen pakken

# Onze easter egg
if naam == "Harry Potter":
    l = input("Wauw jij bent super slim, weet je wat jij mag je eigen specificatie kiezen. Wat kies je?")
    print("Wat cool, jij hebt gekozen voor", l)
    exit()

print(f"Hallo {naam}, laten we beginnen0")
puntensysteem = Puntensysteem()
excel = excelreader.Excelreader("database.xls", "Vragen")
vragen = excel.get_data()

for i in vragen:
    can_continue = False
    while not can_continue:
        vraag = input(f"{i.vraag} - {i.puntentelling}")
        if vraag.isnumeric():
            if int(vraag) in i.mogelijke_antwoorden:
                puntensysteem.voeg_punten_toe(i.domein, int(vraag))
                i.gegeven_antwoord = int(vraag)

                can_continue = True
            else:
                print("Dat antwoord is niet mogelijk, probeer opnieuw")

        else:
            print("Dat antwoord is niet mogelijk, probeer opnieuw")

vragen.sort(key=attrgetter('gegeven_antwoord'), reverse=True)  # Sorteert de vragen op basis van de hoogste dingen

domeinen = puntensysteem.get_domeinen()
for i in domeinen:
    print(f"Jouw domein is: {i.domein} met {i.punten} punten")

    nieuwe_lijst = []
    for p in vragen:
        if p.domein == i.afgekorte_domein and p.gegeven_antwoord > 3:
            nieuwe_lijst.append(p)

    lijst_met_quotes = []
    if len(nieuwe_lijst) != 0:
        for p in nieuwe_lijst:
            lijst_met_quotes.append(p.quote)
    else:
        for p in vragen:
            lijst_met_quotes.append(p.quote)
            quote_amount -= 1
            if quote_amount == 0:
                break

    zin = ""
    for p in lijst_met_quotes:
        zin += p+" "

    print(zin)
