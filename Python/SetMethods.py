fruits = {'apple', 'mangoes', 'banana'}

# add()-- adds an element to the set
fruits.add('oranges')
print(fruits)

# difference()--returns a set with elements in set1 without set2
raptor = {'apple', 'pea', 'grapes', 'starberry'}

yellow = fruits.difference(raptor)
print(yellow)

# discard()--removes a specified item
raptor.discard('pea')
print(raptor)

# isdisjoint()--returns True if there are no similar items in sets
rome = {'spanish', 'french', 'italian', 'romanian'}
mmm = fruits.isdisjoint(rome)
print(mmm)


# union()---returns a set whih contains all the  elements of both sets
u = fruits.union(raptor)
print(u)


# update()-- helps to insert one set values to main set
fruits.update(raptor)
print(fruits)
