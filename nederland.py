"""
Author: O. Smit

Description:

Some experimenting and practicing with dictionaries.
"""


# create a mapping of 'provincies' to 'hoofstad'
provincies = {
    'Drenthe': 'Assen',
    'Flevoland': 'Lelystad',
    'Friesland': 'Leeuwarden',
    'Gelderland': 'Arnhem',
    'Groningen': 'Groningen',
    'Limburg': 'Maastricht',
    'Noord-Brabant': 'Den Bosch',
    'Noord-Holland': 'Haarlem',
    'Overijssel': 'Zwolle',
    'Utrecht': 'Utrecht',
    'Zeeland': 'Middelburg',
    'Zuid-Holland': 'Den Haag'
}

# create a mapping of 'stad' to 'inwonersaantal'
steden = {
    'Assen': 68000,
    'Lelystad': 78000,
    'Leeuwarden': 108000,
    'Arnhem': 152000,
    'Groningen': 200000,
    'Maastricht': 122000,
    'Den Bosch': 151000,
    'Haarlem': 235000,
    'Zwolle': 124000,
    'Utrecht': 362000,
    'Middelburg': 49000,
    'Den Haag': 553000
}

print('-' * 10)
for provincie, stad in provincies.items():
    print(f"De hoofstad van {provincie} is {stad}.")

print('-' * 10)
for stad, inwoners in steden.items():
    print(f"{stad} telt {inwoners} inwoners.")

print('-' * 10)
for provincie, inwoners in provincies.items():
    print(f"De hoofstad van {provincie} telt {steden[inwoners]} inwoners.")

print('-' * 10)
smaller_cities = []
for stad, inwoners in steden.items():
    if len(str(steden[stad])) < 6:
        smaller_cities.append(stad)

print("Deze steden tellen minder dan honderdduizend inwoners:")
print('\n'.join(smaller_cities))
