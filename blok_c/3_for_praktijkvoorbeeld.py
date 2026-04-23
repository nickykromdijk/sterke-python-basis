bestellingen = [
    {"klant": "Anna",   "bedrag": 120.50},
    {"klant": "Boris",  "bedrag": 45.00},
    {"klant": "Carmen", "bedrag": 310.75},
]

for bestelling in bestellingen:
    if bestelling["bedrag"] > 100:
        print(f"{bestelling['klant']}: grote bestelling (€{bestelling['bedrag']})")
    else:
        print(f"{bestelling['klant']}: normale bestelling")

# Ik zie herhalende code, hoe kunnen we dit voorkomen?