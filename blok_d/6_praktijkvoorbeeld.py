def bereken_rente(saldo: float, percentage: float = 5.0) -> float:
    """Berekent de rente op basis van saldo en percentage."""
    return saldo * (percentage / 100)

def verwerk_klant(klant: dict) -> str:
    """Geeft een statusmelding terug voor een klant."""
    if not klant["actief"]:
        return f"{klant['naam']}: account inactief."
    if klant["saldo"] < 0:
        return f"{klant['naam']}: rood saldo — geen rente."

    rente = bereken_rente(klant["saldo"])
    return f"{klant['naam']}: rente van €{rente:.2f} toegepast."

klanten = [
    {"naam": "Anna",   "saldo": 200.00, "actief": True},
    {"naam": "Boris",  "saldo": -15.00, "actief": True},
    {"naam": "Carmen", "saldo": 150.00, "actief": False},
]

for klant in klanten:
    print(verwerk_klant(klant))