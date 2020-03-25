
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    try:
        try_dev = number/1
    except:
        print("string was given not number ... ")
        return 0

    if number <=0:
        print("wrong number was given ...")
        return 0
 

    floored = 1

    while floored*floored <= number:
        floored+=1
    return floored - 1
        


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (12 == sqrt(144)) else "Fail")
print ("Pass" if  (1 == sqrt(3.1415)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (0 == sqrt(-100)) else "Fail")
print ("Pass" if  (0 == sqrt(0.9)) else "Fail")
print ("Pass" if  (0 == sqrt(None)) else "Fail")
print ("Pass" if  (0 == sqrt('number')) else "Fail")


# Pass
# wrong number was given ...
# Pass
# Pass
# Pass
# Pass
# Pass
# Pass
# Pass
# wrong number was given ...
# Pass
# wrong number was given ...
# Pass
# Pass
# string was given not number ... 
# Pass
# string was given not number ... 
# Pass
