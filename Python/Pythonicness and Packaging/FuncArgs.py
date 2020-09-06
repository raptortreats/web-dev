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


# **KWARGS  allows you to hande named arguments that you have not defined in advance

def my_func(x, y=7, *args, **kwargs):
    print(kwargs)


my_func(1, 2, 3, 4, s=8, r=10)
