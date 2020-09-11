days = input("enter days")
rate = input("rate per day")
#pay = (float(days) * float(rate))
# print(pay)


#astr = 'hdhdh'
#istr = 0

# try:
#   istr = int(astr)

# except:
#   istr = -1

try:
    day = float(days)
    rpd = float(rate)
    print(day*rpd)
except:
    print("error,please input numeric value")


def func():
    print("rochish")
    return
    print("raptor")


func()


def say(message, time=1):
    print(message*time)


say("re")
say("mo", 4)


def romo():
    print('rochish')


print("momo")


def computeTotalpay(days, rate):
    pay = float(days)*float(rate)
    print(pay)


computeTotalpay(45, 10)


# largest value
num = [9, 41, 12, 3, 74, 15]
largest = num[0]
for i in num:
    if i > largest:
        largest = i
print(largest)

# smallest value
n = [9, 41, 12, 3, 74, 15]
smallest = num[0]
for i in n:
    if i < smallest:
        smallest = i
print(smallest)

# sum the elements
nu = [9, 41, 12, 3, 74, 15]
add = 0
for i in nu:
    add = add+i
print(add)

# avg of the elements
numo = [9, 41, 12, 3, 74, 15]
sum = 0
count = 0
for i in numo:
    count = count+1
    sum = sum+i
print(sum/count)
