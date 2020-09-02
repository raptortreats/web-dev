print("welcome to stupid quiz")
score = 0

que = input('are you ready (yes/no)')
if que.lower() == 'yes':
    print("lets begin")

    que = input('are you human')
    if que.lower() == 'yes':
        print("nice")
        score += 1
    else:
        print("get the fuck out of my planet")

    que = input("marvel or dc?")
    if que.lower() == 'dc':
        score += 1
        print("you are not batman, but ur ok ")

    else:
        print("bye")

    que = input("girl or boy")
    if que.lower() == 'girl':
        score += 1
        print("give me ur number ")

    else:
        print("get off my game")

    que = input("chicken or veggie")
    if que.lower() == 'chicken':
        score += 1
        print("then go kill one ")

    else:
        print("drive it in ur asshaha")

    que = input("theory or practical")
    if que.lower() == 'practical':
        score += 1
        print("you are legend")

    else:

        print("oh ok")


print("youve scored", score)
