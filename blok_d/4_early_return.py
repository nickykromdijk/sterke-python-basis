def controleer_leeftijd(leeftijd):
    if leeftijd < 0:
        return "Ongeldige leeftijd."
    elif leeftijd < 18:
        return "Geen toegang — minderjarig."
    else:
        return "Toegang verleend."

