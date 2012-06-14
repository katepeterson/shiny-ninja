x = 23                      # for testing purposes, x starts as 23
     
def even_x():
    global x                # "writes to" and "reads from" non-local variable x
    
    x = x / 2               # divides x in half, saves as x
    print(x)                # print x
    if(x == 1):             # if x is equal to 1:
        print("done")       # print "done" to signal program has completed.

    elif(x % 2 == 0.0):     # or, if the remainder is zero and so x is even:
        even_x()            # now, print "even_x()"; should instead run function.

    elif(x % 2 == 1.0):     # or, if the remainder is one and so x is odd:
        odd_x()             # now, print "odd_x()"; should instead run function.
        
def odd_x():
    global x                # "writes to" and "reads from" non-local variable x
    
    x = x * 3               # multiplies x by three, saves as x
    x = x + 1               # adds one to x, saves as x
    
    if(x == 1):             # if x is equal to 1:
        print("done")       # print "done" to signal program has completed.

    elif(x % 2 == 0.0):     # or, if the remainder is zero and so x is even:
        print(x)            # print x
        even_x()            # now, prints "even_x()"; should instead run function.

    elif(x % 2 == 1.0):     # or, if the remainder is one and so x is odd:
        print(x)            # print x
        odd_x()             # now, print "odd_x()"; should instead run function.

def run_program():
    global x                # "writes to" and "reads from" non-local variable x

    if(x == 1):             # if x is equal to 1:
        print("done")       # print "done" to signal program has completed.

    elif(x % 2 == 0.0):     # or, if the remainder is zero and so x is even:
        print(x)            # print x
        even_x()            # now, print "even_x()"; should instead run function.

    elif(x % 2 == 1.0):     # or, if the remainder is one and so x is odd:
        print(x)            # print x
        odd_x()             # now, print "odd_x()"; should instead run function.

run_program()