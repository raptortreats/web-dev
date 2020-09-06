# this allows you to assign each item to an iterable to a variable

numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)

names = ('rochish', 'sammu', 'romu')
first, second, third = names

print(third)

# a variable that is prefaced with an asterisk takes all values from the iterable that are left over

q, w, *e, r = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(q)
print(w)
print(e)
print(r)


r, o, *c, h, i = range(20)

print(r)
print(o)
print(len(c))
print(h)
print(i)
