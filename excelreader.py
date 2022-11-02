import xlrd
import random

class Excelreader():
	def __init__(self, bestandnaam, sheetnaam):
		self.bestandnaam = bestandnaam
		workbook = xlrd.open_workbook(bestandnaam)
		self.worksheet = workbook.sheet_by_name(sheetnaam)
		self.domein_vragen = []


	# returned een lijst met objecten
	def get_data(self):
		rows = 4 # Er zijn 4 rows namelijk se, fict, itec en DE
		columns = 1000 # We weten de exacte lengte niet dus we itereren totdat we een error krijgen. Super lui maar het werkt.

		for i in range(rows):
			for y in range(1, columns):
				try:
					value = self.worksheet.cell(y, i).value.strip()
					value = value.replace(" ", " ") # excel dom

					if value != "":
						splitted = value.split("&&")
						vraag = splitted[0]
						puntentelling = splitted[1].strip()
						quote = splitted[2].strip()

						if i == 0:
							self.domein_vragen.append(Domeinvraag("se", vraag, puntentelling, quote))

						if i == 1:
							self.domein_vragen.append(Domeinvraag("fict", vraag, puntentelling, quote))
						
						if i == 2:
							self.domein_vragen.append(Domeinvraag("iat", vraag, puntentelling, quote))
						
						if i == 3:
							self.domein_vragen.append(Domeinvraag("de", vraag, puntentelling, quote))

				except IndexError as e:
					break

		random.shuffle(self.domein_vragen) # We shufflen onze vragenlijst
		return self.domein_vragen

class Domeinvraag():
	def __init__(self, domein, vraag, puntentelling, quote):
		self.domein = domein
		self.vraag = vraag
		self.puntentelling = puntentelling

		minimale = self.puntentelling.split("t/m")[0]
		maximale = self.puntentelling.split("t/m")[1]
		self.mogelijke_antwoorden = list(range(int(minimale), int(maximale)+1))

		self.gegeven_antwoord = 0
		self.quote = quote

