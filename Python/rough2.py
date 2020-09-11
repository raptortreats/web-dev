
summ = 0
count = 0
while True:
    numbers = input("enter number")

    try:
        n = int(numbers)
        count = count+1
        summ = summ+n

    except:

        if numbers == "exit":
            break
        else:
            print("invalid input enter a number")
            continue
print(summ)
print(count)
print("avg:", summ/count)
