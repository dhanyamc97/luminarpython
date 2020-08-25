lowlimit=int(input("lower limit"))
upperlimit=int(input("upper limit"))

for num in range(lowlimit,upperlimit):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
           print(num)