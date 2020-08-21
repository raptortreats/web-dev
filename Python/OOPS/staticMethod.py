class naruto:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def powlvl(pow):
        if pow > 50:
            print("shippudden level")  # staticmethod has no attributes
            # this cant access the class state
        else:
            print("naruto level")


p1 = naruto("rock lee", 17)
p2 = naruto("keeba", 14)
print(p1.name)
p1.powlvl(99)
