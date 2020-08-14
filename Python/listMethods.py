str = [1, 2, 3, 4, 5, 6]

# clear()--removes all the elements in the list
str.clear()
print(str)

list = ["i love python"]
# append()--adds an element at the end of the list
list.append("and anaconda")
print(list)

# copy()--returns a copy of the list
list2 = list.copy()
print(list2)

# count()-- returns no of elements with specified value
print(list.count('and anaconda'))


# insert()--adds an element at specified location
list.insert(1, 'pandas')
print(list)


# pop()--removes an elemnt from a  specified postion
list.pop(1)
print(list)

# sort()-- sorts the elements of the list
list.sort()
print(list)


# reverse()--reverse the list
list.reverse()
print(list)
