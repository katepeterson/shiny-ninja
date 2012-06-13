# Hailstone Sequence Generator

""" In theory, this program takes an integer (eventually selected by user input).
    Then, the integer is divided by two to test for a remainder.
    
    If there is a remainder of 0, then the number is again divided by two.
    That 1/2 of the original number is saved over the original variable.
    
    If there was a remainder of 1, then the original number is multiplied by three.
    The 3-times-larger number is saved over the original variable.
    That variable then has a one added to it, and is saved again. the 
    
    The new variable is now either [(X*3) +1] or [X/2] the original. 
    The program then repeats the same steps: 
    It tests for a remainder and behaves accordingly.
    
    If the program runs correctly, any number should eventually, when entered,
    End in a repeating loop of 4-2-1 (loop is cut off at 4 currently).

    The goal of the program is to find how many iterations
    Of the odd_x() [(X*3) +1] or even_x() [X/2] functions are necessary
    To reach the 4-2-1 loop.
    
    Note: When the even_x() and odd_x() functions run without errors,
    A running count will be added with a new variable (current_count)
    'current_count' will have one added to it
    Each time the odd_x() and even_x() functions run. 
    At the end of the program, there will be a line saying
    print("It took ", current_count, " steps to reach 1.") """

x_variable = 21 # when the rest of this works, the pre-chosen test number will be changed to input(int("Please enter a number: "))
y_variable = x_variable 


def even_x():
    # if I'm right, then "global x_variable" makes the variable pull from and write to the variable up above, 
    # so the data is saved for the other functions
    global x_variable
    global y_variable
    y_variable = x_variable # saves x_variable to y_variable
    x_variable = y_variable / 2 # divides x_variable in half,
    y_variable = x_variable # then saves x_variable to y_variable again.
    # Both x_variable and y_variable are now equal to half their previous value.
    
    # print(x_variable) # prints the new total, thereby keeping a running list of results
    """ temporarily commented out, because it kept crashing when the numbers got too big
     obviously, that problem occurs because of the odd_x() function
     but there's no reason to print this one if I don't print the other. """
    
    # here's the bit I'm unsure about
    if(x_variable == 4):
        print("done")

    # am I using % right?
    # If I am, it should determine the remainder of the variable, 
    # then run the appropriate function. 
    elif(x_variable / 2 % 2 == 0.0):
        even_x()
    elif(x_variable / 2 % 2 == 1.0):
        odd_x()


def odd_x():
    # same as above
    global x_variable
    global y_variable
    # print(x_variable)
    
    y_variable = x_variable # saves x_variable to y_variable, 
    x_variable = y_variable * 3 # multiplies x_variable by three, 
    y_variable = x_variable # saves x_variable to y_variable,
    x_variable = y_variable + 1 # adds one to x_variable, 
    y_variable = x_variable # saves, for the last time, x_variable to y_variable.
    
    # Both x_variable and y_variable are now equal.
    # And both equal (X * 3) + 1, 
    # where X = the amount they formerly were. 
    # (e.g. 3 becomes 10, 15 becomes 46)
    
    # print(x_variable) # prints the new total, thereby keeping a running list of results
    # temporarily commented out, because it kept crashing when the numbers got too big
    
    # again, is the next section my problem?
    if(x_variable == 4): # When program runs correctly, this will be 1, rather than 4
        print("done")
    elif(x_variable / 2 % 2 == 0.0):
        even_x()
    elif(x_variable / 2 % 2 == 1.0):
        odd_x()
    
    
def run_program():
    global x_variable
    if(x_variable / 2 % 2 == 0.0):
        even_x()
    else:
        odd_x()

run_program()