# Make sure you are not modifying the method signatures
# Function 1: Write a simple Hello World program
# This function should print "Hello, World!" to the screen.
def hello_world():
    # TODO: Implement this function
    print ("Hello World!")
     
hello_world()

# Function 2: Get input and output with different variable types
# This function should prompt the user for their name (string), age (int), and height (float),
# and then print them back in a formatted message.
def input_output():
    # TODO: Implement this function
    name = input("Enter your name: ")
    age = int(input ("Enter your age: "))
    height = float(input("Enter your height: "))
    print ("Hello,"+ name + "!")
    print ("You are", age, "years old.")
    print ("Your height is", height, "meters.")
    
input_output()

