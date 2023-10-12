# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Vraag de gebruiker om autos in te voeren, gescheiden door komma'
input_string = input("Voer minimaal 5 autos in, gescheiden door komma's: ")
# Split de invoerstring met de komma's
autos = [auto.strip() for auto in input_string.split(',')]
# Sorteer de lijst vanaf Z tot A
autos.sort(reverse=False)
print(autos)





