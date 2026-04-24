# Geordend en aanpasbaar, geen duplicaten toegestaan

klant = {
    "naam": "Anna",
    "leeftijd": 34,
    "actief": True,
}

klant2 = {
    "naam": "Piet",
    "leeftijd": 55,
    "actief": True,
}

# Opvragen en aanpassen
klant["naam"] = "Annabel"

# Toevoegen
klant["email"] = "anna@gmail.com"
print(klant)

# Alle keys en values
print(list(klant.keys()))
print(list(klant.values()))
# Lijst van dicts
klanten = [klant, klant2]
print({"klanten": klanten})