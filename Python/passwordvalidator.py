password = "rffffhfhfhf"
if(password == None):
    print('password shoudnt be blank')
elif(len(password) < 6):
    print('password shouldnt be less than 6 char')
elif(" " in password):
    print('password shouldnt contain spaces')
else:
    print('valid password')
