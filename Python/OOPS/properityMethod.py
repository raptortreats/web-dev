class opm:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    @property
    def str(self):
        return self.name + "is of rank" + self.rank

    @str.setter
    def str(self, str):

        change = str.split(" ")
        print(change)
        self.name = change[0]
        self.rank = change[-1]


hero1 = opm("saitama", "B")
hero1.str = "genos is of rank s"  # setting
print(hero1.str)
