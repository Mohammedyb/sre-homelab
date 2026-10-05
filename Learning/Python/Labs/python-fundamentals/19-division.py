def remainder_division (a,b):
    if b == 0:
        raise ZeroDivisionError
    result = a//b
    remainder = a%b
    print(a, "/", b, "is", result, "remainder", remainder ) 


#Main Program
remainder_division(10,0)
