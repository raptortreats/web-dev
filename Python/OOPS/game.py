class game:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @property
    def kill(self):
        if self.health == 5:
            print(self.health, "monster is alive")

        elif self.health <= 3:
            print(self.health, "monster got hit")

        elif self.health == 0:
            print(self.health, "monster is dead")

        else:
            print("you are out of options")


hit1 = game("rochish", 5)
print(hit1.kill)
