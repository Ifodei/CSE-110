youngest_person = ""
youngest_age_so_far = 99999999999999999999
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

for items in people:
    part = items.split()
    name = part [0]
    age = int (part [1])
    if age < youngest_age_so_far:
        youngest_age_so_far = age
        youngest_person = name

print (f"The yongest person is {youngest_person} and he/she is aged {youngest_age_so_far}")