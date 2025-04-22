animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5}
]

sorted_animals = sorted(animals, key=lambda x: x['age'])
print(sorted_animals)