def sqrt(a):
    x = 1
    i = 0
    while True:
        oldValue = x
        x = 1/2*(x**2 + a)/x
        i += 1
        if abs(x - oldValue) < 0.0001:
            break
    return x

def equation():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    print("\n(%0.3f)x*x+(%0.3f)x+(%0.3f) = 0" %(a,b,c))
    
    if a == 0:
        x = -c/b
        print("Answer is %0.3f" %(x))
    elif a != 0 and b == 0:
        if c>0:
            print("No roots")
        else:
            x = sqrt(-c)/a
            print("x = %0.3f" %(x))
    else:
        d = b**2-4*a*c
        print("D = %0.3f" %(d))
        if d<0:
            print("\n There are no valid roots")
        elif d == 0:
            x = -b/(2*a)
            print("\n The root is %0.3f" %(x))
        else:
            x1 = (-b-sqrt(d))/(2*a)
            x2 = (-b+sqrt(d))/(2*a)
            print("\n The roots are %0.3f and %0.3f" %(x1,x2))

equation()
