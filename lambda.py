people = [
    {"name": "Harry", "house": "Gryff"},
    {"name": "Cho", "house": "Rav"},
    {"name": "Drago", "house": "Stieve"}
]

#def f(person):
   # return person["name"]

#people.sort(key=f)
# easer way:
people.sort(key=lambda person: person["name"])
print(people)