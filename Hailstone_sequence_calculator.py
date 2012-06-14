x = 7                                               # x will be determined by user input
i = 0                                               # i is a counter to see how long it takes to find 1

def even_x(x,i):
    """ Divides the (even) number by two, saving it over the previous value for x.
    Then determines if it's finished running, even_x() is needed again, or odd_x() is now necessary. 
    """
    #global x                                        # "writes to" and "reads from" non-local variable x
    #global i                                        # "writes to" and "reads from" non-local variable i

    x = x / 2                                       # divides x in half, saves as x
    i = i + 1                                       # adds 1 to i, keeping track of how many steps x=1 requires
    print(x)                                        # print x
    
    if(x == 1):                                     # if x is equal to 1:
        print "It took", i, "steps to reach 1."     # prints number of steps to find 1.

    elif(x % 2 == 0.0):                             # or, if the remainder is zero and so x is even:
        even_x(x,i)                                    # now, print "even_x()"; should instead run function.

    elif(x % 2 == 1.0):                             # or, if the remainder is one and so x is odd:
        odd_x(x,i)                                     # now, print "odd_x()"; should instead run function.

def odd_x(x,i):
    """ Multiplies the (odd) number by three, then adds one, and saves it over the previous value for x.
    Then determines if it's finished running, odd_x() is needed again, or even_x() is now necessary.
    """
    #global x                                        # "writes to" and "reads from" non-local variable x
    #global i                                        # "writes to" and "reads from" non-local variable i

    x = x * 3                                       # multiplies x by three, saves as x
    x = x + 1                                       # adds one to x, saves as x
    i = i + 1                                       # adds 1 to i, keeping track of how many steps x=1 requires
    print(x)    
    
    if(x == 1):                                     # if x is equal to 1:
        print "It took", i, "steps to reach 1."     # prints number of steps to find 1.

    elif(x % 2 == 0.0):                             # or, if the remainder is zero and so x is even:
        even_x(x,i)                                    # now, prints "even_x()"; should instead run function.

    elif(x % 2 == 1.0):                             # or, if the remainder is one and so x is odd:
        odd_x(x,i)                                     # now, print "odd_x()"; should instead run function.

def run_program(x):
    """ Starts the program running by determining which one of three things is correct:
    it was started at 1;
    it is an odd number above one and so odd_x()is needed;
    or it is an even number, and so even_x() is needed,
    """
    #global x                                        # "writes to" and "reads from" non-local variable x
    i = 0
    if(x == 1):                                     # if x is equal to 1:
        print "It took", i, "steps to reach 1."     # prints number of steps to find 1.

    elif(x % 2 == 0.0):                             # or, if the remainder is zero and so x is even:
        print(x)                                    # print x
        even_x(x,i)                                    # now, print "even_x()"; should instead run function.

    elif(x % 2 == 1.0):                             # or, if the remainder is one and so x is odd:
        print(x)                                    # print x
        odd_x(x,i)                                     # now, print "odd_x()"; should instead run function.

run_program(x)