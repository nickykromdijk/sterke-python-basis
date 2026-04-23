import json

json_tekst = '{"naam": "Anna", "leeftijd": 34}'
klant = json.loads(json_tekst)
print(klant["naam"])  # gewoon een dict!