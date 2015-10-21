def is_prime(x):
    """checks if x is prime or not. returns boolean"""
    counter = 0
    for y in range(1,x,1):
        if x % y == 0:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def is_happy(x):
    """checks if x is happy or not. returns boolean"""
    newNum = x

    while (newNum != 0):
        onesDigit = newNum % 10
        tensDigit = (newNum/10) % 10
        hundredDigit = newNum / 100
        newNum = onesDigit*onesDigit + tensDigit*tensDigit + hundredDigit*hundredDigit

        if newNum == 4:
            return False
        if newNum == 16:
            return False
        if newNum == 37:
            return False
        if newNum == 58:
            return False
        if newNum == 89:
            return False
        if newNum == 145:
            return False
        if newNum == 42:
            return False
        if newNum == 20:
            return False
        if newNum == 1:
            return True

def is_square(x):
    """checks if x is square or not. returns boolean"""
    sumTotal = 0
    for y in range(1,x+1,2):
        sumTotal += y
        if sumTotal == x:
            return True

    return False

def is_triangular(x):
    """checks if x is triangular or not. returns boolean"""
    sumTotal = 0
    for y in range(1,x+1,1):
        sumTotal += y
        if sumTotal == x:
            return True

    return False
    

def is_smug(x):
    """checks if x is smug or not. returns boolean"""
    for y in range(1,x+1):
        for z in range(1,x+1):
            if y*y + z*z == x:
                return True

    return False



def is_honest(x):
    """checks if x is honest or not. returns boolean"""
    pretend = 0
    square = 0
    for y in range(1,x+1):
        if x//y == y:
            square += 1
            if y*y != x:
                pretend += 1

    if square == 0:
        return True
    else:
        if pretend == 0:
            return True
        else:
            return False

def output(x):
    print (x)
    
    if is_prime(x):
        print ("   prime,"),
    else:
        print ("   composite,"),

    if is_happy(x):
        print (" happy,"),
    else:
        print (" unhappy,"),

    if is_triangular(x):
        print (" triangular,"),
    else:
        print (" not triangular,"),

    if is_square(x):
        print (" square,"),
    else:
        print (" not square,"),
      

    if is_smug(x):
        print (" smug,"),
    else:
        print (" not smug,"),

    if is_honest(x):
        print (" honest\n"),
    else:
        print (" dishonest\n"),


def main():
    limit = 1000000
    for x in range (1,limit+1):
        output(x)
        
if __name__ == "__main__":
    main()
