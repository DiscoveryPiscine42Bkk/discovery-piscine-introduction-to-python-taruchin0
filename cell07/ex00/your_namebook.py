def array_of_names(names):
    namelist = []
    for fname,lname in names.items():
        namelist.append((fname.capitalize() + " " + lname.capitalize()))
    return namelist
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))
