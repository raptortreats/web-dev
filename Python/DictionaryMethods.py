pets = {'dog': 'bieber', 'cat': 'bhura', 'dinosaur': 'dino'}


# copy()--copies the key values to other dictionaries
x = pets.copy()

print(x)

# fromkeys()--Returns a dictionary with the specified keys and value
x = ('maruti', 'ford', 'masarati')
y = ('GT')

models = dict.fromkeys(x, y)
print(models)

# get()--gets a specified value from dict
print(pets.get('cat'))

# items()--Returns a dictionary with the specified keys and value
print(pets.items())


# keys()--returns the dict keys
print(pets.keys())

# pop()--removes specified item from dict
pets.pop('dog')
print(pets)

# popitem()--removes the last item from dict
pets.popitem()
print(pets)

# update()--adds a new key value pair
pets.update({"horse": "remy"})
print(pets)

# values()--returns the dict values
p = pets.values()
print(p)
