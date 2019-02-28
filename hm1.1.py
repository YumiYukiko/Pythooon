def NOD (a,b):
    while a !=0 and b !=0 :
        if a>b:
            a = a % b
        else:
            b = b % a
    return a+b
    
a = 0
b = 0

while a<=0 or b<=0:
    a = float(input("a = "))
    b = float(input("b = "))

print("NOD = %d" %(NOD(a,b)))