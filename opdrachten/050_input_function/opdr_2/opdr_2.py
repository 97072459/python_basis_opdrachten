# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]

#Nou belt Marie dat ze niet meer meegaat.
#Zorg ervoor dat Marie uit de lijst wordt gehaald.
gasten.remove("Marie")
print(gasten)

#Even later belt George, hij wil ook mee. George wil naast Kees zitten!
#Zorg ervoor dat George naast Kees wordt toegevoegd.
positie_van_kees = gasten.index("Kees")
gasten.insert(positie_van_kees + 1, "George")
print(gasten)