# these are also called as Dunders
# these have double underscore


class multi:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return multi(self.x*other.x, self.y*other.y)


f = multi(2, 3)
s = multi(3, 4)
result = (f*s)

print(result.x)
print(result.y)


# __gt__
# lt
# eq
# le
# ge
# ne

class string:
    def __init__(self, nex):
        self.nex = nex

    def __gt__(self, other):
        for i in range(len(other.nex)+1):
            result = other.nex[:i]+">"+self.nex
            result += ">"+other.nex[i:]
            print(result)


rochi = string("rochish")
sammu = string("sammu")
rochi > sammu


# output
# >rochish>sammu
# s>rochish>ammu
# sa>rochish>mmu
# sam>rochish>mu
# samm>rochish>u
# sammu>rochish>
