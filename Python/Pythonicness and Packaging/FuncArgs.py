def function(named_arg, *args):
    print(named_arg)
    print(args)


function(5, 3, 6, 8, 9)


def my_games(my_name, *args):
    print("name:", my_name)
    for arg in args:
        print(arg)


my_games("rtreats", "COD", "PUBG", "modern warfare",
         "resident evil", "ballistic", "WOW")
