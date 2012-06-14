# Hailstone Sequence Calculator

""" In theory, this program takes an integer (eventually selected by user input).
    Then, the integer is tested to determine whether it is even or it. 
    This is done so by dividing by two to test for a remainder.
    
    If there is a remainder of 0, then the number is again divided by two.
    That 1/2 of the original number is saved over the original variable.
    If there was a remainder of 1, then the original number is multiplied by three.
    The 3-times-larger number is saved over the original variable.
    That variable then has a one added to it, and is saved again.
    
    The new variable is now either [(___*3) +1] or (___/2) the original. 
    The program then repeats the same steps,  
    testing for a remainder and behaving accordingly.
    
    If the program runs correctly, any number should eventually, when entered,
    end in a repeating loop of 4-2-1.

    The goal of the program is to find how many iterations
    of the odd_x() or even_x() functions are necessary to reach the 4-2-1 loop.
    
    Note: When the even_x() and odd_x() functions run without errors,
    A running count will be added with a new variable (i). 
    it will then have one added to it 
    each time the odd_x() and even_x() functions run. 
    At the end of the program, there will be a line saying
    print("It took ", i, " steps to reach 1.") """

x = 23

def even_x():
    global x
    
    x = x / 2  # divides x in half, saves as x

    if(x == 1):
        print("done")
    elif(x % 2 == 0.0):
        print(x)        
        print("even_x()")
    elif(x % 2 == 1.0):
        print(x)
        print("odd_x()")
        
def odd_x():
    global x
    
    x = x * 3 # multiplies x by three, saves as x
    x = x + 1 # adds one to x, saves as x
    
    if(x == 1):
        print("done")

    elif(x / 2 % 2 == 0.0):
        print(x)
        print("even_x()")

    elif(x / 2 % 2 == 1.0):
        print(x)
        print("odd_x()")

def run_program():
    global x
    if(x == 1):
        print("done")
    elif(x % 2 == 0.0):
        print(x)
        print("even_x()")
    else:
        print(x)
        print("odd_x()")