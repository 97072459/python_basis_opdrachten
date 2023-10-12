# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

# De rest moet jij doen.....


# Aantal pogingen
pogingen = 0

print("Raad mijn geheime getal")

while True:
    # Vraag de gebruiker om een getal in te voeren
    pogingen += 1
    geraden_getal = int(input())
    
    # Controleer of het geraden getal gelijk is aan het geheime getal
    if geraden_getal == geheim_getal:
        print(f"Je hebt het getal geraden! Het is {geheim_getal}!")
        print(f"Je hebt het in {pogingen} keer geraden")
        break
    elif geraden_getal < geheim_getal:
        print("hoger")
    else:
        print("lager")
