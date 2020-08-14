def cin(str):
    a = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(str)):
        if(str[i] == 'z'):
            print('a')
            continue
        for j in range(0, len(a)):

            if(a[j] == str[i]):
                print(a[j+1])


cin("rochzsh")
