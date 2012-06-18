# Hailstone_Sequence_Calculator

def even_x(x,i):
    """ Divides the (even) number by two, saving it over the previous value for x.
    Then determines if it's finished running, even_x() is needed again, or odd_x() is now necessary. 
    """
 
    x = x / 2                                       # divides x in half, saves as x
    i = i + 1                                       # adds 1 to i, keeping track of how many steps x=1 requires

    if(x == 1):                                     # if x is equal to 1:
        return x, i                                    # return i

    elif(x % 2 == 0.0):                             # or, if the remainder is zero and so x is even:
        (x,i) = even_x(x,i)                         # runs even_x() function.

    elif(x % 2 == 1.0):                             # or, if the remainder is one and so x is odd:
        (x, i) = odd_x(x,i)                         # runs odd_x() function.

    return x, i                                     # returns x and i

def odd_x(x,i):
    """ Multiplies the (odd) number by three, then adds one, and saves it over the previous value for x.
    Then determines if it's finished running, odd_x() is needed again, or even_x() is now necessary.
    """
 
    x = x * 3                                       # multiplies x by three, saves as x
    x = x + 1                                       # adds one to x, saves as x
    i = i + 1                                       # adds 1 to i, keeping track of how many steps x=1 requires

    if(x == 1):                                     # if x is equal to 1:
        return x, i                                    # return i

    elif(x % 2 == 0.0):                             # or, if the remainder is zero and so x is even:
        (x,i) = even_x(x,i)                         # runs even_x() function.

    elif(x % 2 == 1.0):                             # or, if the remainder is one and so x is odd:
        (x, i) = odd_x(x,i)                         # runs odd_x() function.

    return x, i                                     # returns x and i

def run_program(x):
    """ Starts the program running by determining which one of three things is correct:
    it was started at 1;
    it is an odd number above one and so odd_x()is needed;
    or it is an even number, and so even_x() is needed,
    """
    #x = 3                                          # "writes to" and "reads from" non-local variable x
    i = 0                                           # i is set as equal to zero so as to start the counter properly
    if(x == 1):                                     # if x is equal to 1:
        return x, i                                    # return i

    elif(x % 2 == 0.0):                             # or, if the remainder is zero and so x is even:
        (x,i) = even_x(x,i)                         # runs even_x() function.

    elif(x % 2 == 1.0):                             # or, if the remainder is one and so x is odd:
        (x, i) = odd_x(x,i)                         # runs odd_x() function.

    return x, i  

#run_program(x)