# status = "actief"

# match status:
#     case "actief":
#         print("Gebruiker is actief")
#     case "geblokkeerd":
#         print("Gebruiker is geblokkeerd")
#     case "verwijderd":
#         print("Gebruiker bestaat niet meer")
#     case _:
#         print("Onbekende status")


# -----------------------------------------------------------

response = (404, "GET")

match response:
    case (200, method):
        print(f"Succes via {method}")
    case (404, method):
        print(f"Niet gevonden via {method}")
    case (500, _):
        print("Serverfout")
    case _:
        print("Onbekende response")