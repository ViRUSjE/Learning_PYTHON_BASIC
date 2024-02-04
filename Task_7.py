"Adding elements to list"

animals = []
animals_2 = ["Simba", "Pumba", "Timon"]
"Printing empty list"
print(animals)

print(animals_2)

animals.append("Julian")

"Printing whole list"
print(animals)

"Printing first element of list"
print(animals[0])


animals.insert(1, "skiper")
print(animals)
print(animals[1])

animals.append("Rico")

print(animals)

animals.extend(animals_2)
print(animals)