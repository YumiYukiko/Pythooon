def NOD ():
    a = 0
    b = 0

    while a<=0 or b<=0:
        a = int(input("a = "))
        b = int(input("b = "))

    startA = a
    startB = b
    r = 1
    while a !=0 and b !=0 :
        if a>b:
            a = a % b
        else:
            b = b % a

    print("NOD %i and %i = %i" %(startA,startB,a+b))

NOD()