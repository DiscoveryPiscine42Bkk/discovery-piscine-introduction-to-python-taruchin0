def famous_births(people):
    namelist = list(people.values())
    namelist.sort(key=lambda day: int(day["date_of_birth"]))
    for each in namelist:
        print(f"{each['name']} is a great scientist born in {each['date_of_birth']}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
