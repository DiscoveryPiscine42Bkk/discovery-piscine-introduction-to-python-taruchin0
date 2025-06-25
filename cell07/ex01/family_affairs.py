def find_the_redheads(names):
    newlist = []
    for name,colour in names.items():
        if colour == 'red':
            newlist.append(name)
    return newlist

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))
