class Domein():
    def __init__(self, domein, punten, afgekorte_domein):
        self.domein = domein
        self.punten = punten
        self.afgekorte_domein = afgekorte_domein


class Puntensysteem():
    # Dit is de initialisatie
    # Dit runt nadat je een Puntensysteem object maakt
    def __init__(self):
        self.se = 0
        self.fict = 0
        self.de = 0
        self.iat = 0

    # Dit voegt steeds een punt toe aan een domein
    def voeg_punten_toe(self, destination, aantal_punten):
        if destination.lower() == "se":
            self.se += aantal_punten
        if destination.lower() == "fict":
            self.fict += aantal_punten
        if destination.lower() == "de":
            self.de += aantal_punten
        if destination.lower() == "iat":
            self.iat += aantal_punten

    # Aan het einde kan je deze functie oproepen om de domeinen te krijgen
    def get_domeinen(self):
        max_punten = max(self.se, self.de, self.fict, self.iat)
        domeinen = [self.se, self.de, self.fict, self.iat]
        jouw_domeinen = []
        if self.se == max_punten:
            jouw_domeinen.append(Domein("Software Engineering", max_punten, "se"))
        if self.de == max_punten:
            jouw_domeinen.append(Domein("Data Engineering", max_punten, "de"))
        if self.fict == max_punten:
            jouw_domeinen.append(Domein("Forenisch ICT", max_punten, "fict"))
        if self.iat == max_punten:
            jouw_domeinen.append(Domein("Interactie Technologie", max_punten, "iat"))

        return jouw_domeinen
