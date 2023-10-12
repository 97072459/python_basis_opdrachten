# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

# Vragen stellen
vraag1 = input("Wat vind je van de huidige regering? ")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe? ")
vraag3 = input("Wat vind jij de mooiste stad van Nederland? ")

# Antwoorden opslaan in een tekstbestand
with open("enquete_resultaten.txt", "w") as bestand:
    bestand.write("Antwoord op vraag 1 (Huidige regering): " + vraag1 + "\n")
    bestand.write("Antwoord op vraag 2 (Python-lessen): " + vraag2 + "\n")
    bestand.write("Antwoord op vraag 3 (Mooiste stad van Nederland): " + vraag3 + "\n")

print("Bedankt voor het invullen van de enquête. De antwoorden zijn opgeslagen in enquete_resultaten.txt.")
