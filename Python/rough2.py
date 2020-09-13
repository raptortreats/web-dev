
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


str = "Perfect-Plan-B:0.7541"
pos = str.find(":")
print(float(str[pos+1::]))
