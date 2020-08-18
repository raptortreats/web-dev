class friends:
    def __init__(self, name, dialogues):
        self.name = name
        self.dialogues = dialogues

    def nation(self):
        print("american")


one = friends("ross", "unagi")
two = friends("chandler", "sarcastic comment")
three = friends("joey", "how you doin?")
four = friends("monica", "i know")
five = friends("rachel", "Noooooo")
six = friends("phoebe", "angry replies")


print(two.dialogues)
print(six.name)
print(four.dialogues)
print(three.dialogues)
five.nation()
