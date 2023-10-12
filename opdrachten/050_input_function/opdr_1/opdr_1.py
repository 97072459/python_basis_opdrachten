# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.


# Vraag de gebruiker om de lengte van de eerste zijde
zijde1 = int(input("Geef de lengte van de eerste zijde\n"))

# Vraag de gebruiker om de lengte van de tweede zijde
zijde2 = int(input("Geef de lengte van de tweede zijde\n"))

# Bereken de lengte van de schuine zijde met behulp van de stelling van Pythagoras
schuine_zijde = (zijde1 ** 2 + zijde2 ** 2) ** 0.5

# Toon het resultaat
print("\nDe lengte van de schuine zijde is:", schuine_zijde)
