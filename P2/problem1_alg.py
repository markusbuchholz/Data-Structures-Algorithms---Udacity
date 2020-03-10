

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    try:
        return int(number**0.5)
    except:
        return 0




print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print(sqrt(-3))
print(sqrt(3.1415))
print(sqrt(None))
print(sqrt('number'))
print("Pass" if (99380 == sqrt(9876543210)) else "Fail")
