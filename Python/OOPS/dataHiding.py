# encapsulation
class DH:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(1, value)

    def pop(self):
        self._hiddenlist.pop(-1)

    def __repr__(self):
        return "DH({})".format(self._hiddenlist)


a = DH([1, 2, 3])
print(a)
a.push(12)
print(a)
a.pop()
print(a)
print(a._hiddenlist)


# private method
# cant be accessed outside the class

class animal:
    __dog = 2

    def print_dog(self):
        print(self.__dog)


a = animal()
a.print_dog()
print(a._animal__dog)
# print(a.__dog) cannot access like this
