# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Originele lijst van pizza's
pizza_list = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteren
pizza_list.sort()
print(pizza_list)

# Nieuwe toevoegen
pizza_list.append('yo-favorito')
print(pizza_list)

# Verwijderen
pizza_list.remove('olivio')
print(pizza_list)

# De eerste 3 pizza's uit
print(pizza_list[:3])

# Middelste pizza
print([pizza_list[len(pizza_list) // 2]])

# Print de laatste 3 pizza'
print(pizza_list[-3:])
