
def roc(question):
    if question == "give password":
        print("i dont wamt to")

    elif question == "do you love me":
        print('yes i do')
    elif question == "u hate me":
        print("angry face")

    else:
        print("thank you for your support")


while True:
    question = input("ask: ")
    if question == "you changed":
        break
    roc(question)
