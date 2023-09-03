from guitar import Guitar

guitars = []
with open("guitars.csv", 'r') as file:
    for items in file:
        parts = items.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), parts[-1])
        guitars.append(guitar)
name = input("input name >>>")
while name != "":
    year = input("input years >>>")
    cost = input("input costs >>>")
    name = Guitar(name, year, cost)
    guitars.append(name)
    print("Already to add")
    name = input("Name: ")

guitars.sort()
for guitar in guitars:
    print(guitar)
