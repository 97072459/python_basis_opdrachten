# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...

# Vraag de leeftijd van de bezoeker
leeftijd = int(input("Geef uw leeftijd: "))

# Bepaal de groep op basis van de leeftijd
if leeftijd < 18:
    groep = "kinderen"
    korting_percentage = 50
elif leeftijd >= 65:
    groep = "ouderen"
    korting_percentage = 30
else:
    groep = "volwassenen"
    korting_percentage = 0

# Bereken korting
toegangsprijs = 12.5  # Standaard toegangsprijs voor volwassenen
korting_bedrag = (korting_percentage / 100) * toegangsprijs
te_betalen_bedrag = toegangsprijs - korting_bedrag

# Toon de uitvoer
print(f"U behoort tot de groep {groep}")
print(f"U krijgt {korting_percentage}% korting")
print(f"U betaalt daarom {te_betalen_bedrag:.2f}")