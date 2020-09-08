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
