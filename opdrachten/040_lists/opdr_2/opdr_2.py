# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....

#Print de naam van de 1e rivier  
#Print het 2e land waar de 1e rivier doorheen stroomt
#Zowel land als rivier beginnen met een hoofdletter, gebruik hiervoor een tekstfunctie.
#print(rivieren[0])
print("De river", rivieren[0].capitalize(),  "stroomt onder andere door", rivier_info[rivieren[0]][1].capitalize())

#Print de naam van de 2e rivier  
#Print het 1e land waar de 1e rivier doorheen stroomt
#Zowel land als rivier beginnen met een hoofdletter
#print(rivieren[1])
print("De river", rivieren[1].capitalize(),  "stroomt onder andere door", rivier_info[rivieren[1]][0].capitalize())
                                                                                  
#Print de naam van de 3e rivier  
#Print het 3e land waar de 1e rivier doorheen stroomt
#Zowel land als rivier beginnen met een hoofdletter
#print(rivieren[2])
print("De river", rivieren[2].capitalize(),  "stroomt onder andere door", rivier_info[rivieren[2]][2].capitalize())