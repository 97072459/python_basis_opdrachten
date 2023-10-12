# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

my_list = []

# De range van 3 tot 81 met stappen van 3
for cijfer in range (3, 82, 3):
    # Berekening van het kwadraat van het getal en deel het door 3
    berekening = (cijfer ** 2) / 3.0
    # Berekening aan de mylist (resultat) toevoegen
    my_list.append(berekening)
print(my_list)