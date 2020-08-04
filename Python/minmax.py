a = [5,7,3,1,2]
min = a[0]
max = len(a)
i = 0
for i in range(0,len(a)):
    if(a[i]<min):
        min=a[i]
        i=i+1
    if(a[i]>max):
        max = a[i]
        i = i+1
print('maximum value is',max)
print('minimum value is',min)

