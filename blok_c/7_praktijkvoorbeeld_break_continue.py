klanten = [
    {"naam": "Anna",   "saldo": 120.00, "actief": True},
    {"naam": "Boris",  "saldo": 45.00,  "actief": False},
    {"naam": "Carmen", "saldo": -10.50, "actief": True},
    {"naam": "David",  "saldo": 200.00, "actief": True},
]

for klant in klanten:
    if not klant["actief"]:
        print(f"{klant['naam']}: inactief — overgeslagen.")

    if klant["saldo"] < 0:
        print(f"STOP: {klant['naam']} heeft een rood saldo!")

    print(f"{klant['naam']}: saldo €{klant['saldo']} — ok.")

# Welke 2 elementen missen hier om daadwerkelijk inactieve klanten over te slaan
# en om meteen de loop te stoppen nadat de loop een klant verwerkt die een min saldo heeft