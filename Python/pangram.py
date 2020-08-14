def pngrm():
    n = "two driven jocks help fax my big quiz"
    n = n.replace(" ", "")
    count = 0
    n = set(n)
    print(n)
    for i in n:
        count = count + 1
    print(count)


pngrm()
