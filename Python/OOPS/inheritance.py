# inheritance provides a way to share functionality towards classes


class animals:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class dog(animals):
    def sound(self):
        print("bow bow")


class cat(animals):
    def sound(self):
        print("purrrr")


class snake(animals):
    def sound(self):
        print("hisss")


dumo = dog("dumo", "black")
print(dumo.color)
dumo.sound()
sammu = snake("sammu", "greenshit")
sammu.sound()
