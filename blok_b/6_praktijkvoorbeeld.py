gebruiker = {
    "naam": "Anna",
    "actief": True,
    "rol": "medewerker",
    "login_pogingen": 3
}

if not gebruiker["actief"]:
    print("Account is inactief.")
elif gebruiker["login_pogingen"] > 3:
    print("Account geblokkeerd door te veel pogingen.")
elif gebruiker["rol"] == "admin":
    print(f"Welkom, {gebruiker['naam']}! Volledige toegang.")
else:
    print(f"Welkom, {gebruiker['naam']}! Beperkte toegang.")