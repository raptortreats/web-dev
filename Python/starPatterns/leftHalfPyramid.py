n = 5
for i in range(0, n-1):
    for j in range(0, n-i):
        print(" ", end="")
    for k in range(j, n):
        print("*", end="")

    print("\r")
