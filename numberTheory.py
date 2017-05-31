# The mathematical proofs and C++ code are courtesy of:
# Stepanov, Alexander A.; Rose, Daniel E. (2014-11-13).
# From Mathematics to Generic Programming (p. 8). Pearson Education. Kindle Edition.

# The provided C++ code is:
#  int multiply0( int n, int a)}            //pass in variables n, a. n serves as multiplier and
#    if (n = = 1) return a;                 // a serves as multiplicand. Given that 1a = a, the first case
#    return multiply0( n - 1, a) + a; }     // n = 1 -> a, else the remaining n-1 cases are computed.

# My Python interpretation
#test
def getMultiplicand():  # gets and checks the value of the multiplicand
    multiplicand = input("Please enter the value for the multiplicand.\n")
    while checkInput(multiplicand) != True:
        multiplicand = input("Please enter the value for the multiplicand.\n")
    return True

def getMultiplier():  # gets anc checks the value of the multiplier
    multiplier = input("Please enter the value for the multiplier.\n")
    while checkInput(multiplier) != True:
        multiplier = input("Please enter the value for the multiplier.\n")
    return True

def checkInput(userNum):  # validates user input
    try:
        number = int(userNum)  # checks if its a number
    except ValueError:
        print('Please enter a valid number.', userNum, ' does not qualify.\n\n')
    else:
        if number > 0:  # checks if it's a member of the Natural Numbers
            print(userNum, 'is an excellent choice.')
            return True
        else:  # Sets you straight if you've lost your way.
            print("Don't act a fool. You know that won't work for this.")
            return False

def checkMultiplyBy1(n):  # since we have established 1n = n
    if n == 1:
        return True
    else:
        return False


def multiplicationAutomation(n, a):  # Of course we have a multiplication operator that could be used but the
    # the point of our exercise is creating an algorithm and a system that offers multiplication.
    product = a
    while n > 0:
        product = + a
        n - 1

def workIt(n, a):  # We keep with the variable convention and pass in n and a respectively.
    print("Go you! Now onto to the good stuff. ")
    if checkMultiplyBy1(n):
        return a
    else:
        multiplicationAutomation(n, a)

def main():  # this bad boy controls the world!
    print("Note: Only natural number values will be accepted for now.")
    a = getMultiplicand()  # this gets & checks the multiplicand
    n = getMultiplier()  # gets & checks multiplier
    workIt(n, a)  # works the magic baby!


main()
