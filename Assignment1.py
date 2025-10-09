# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
   return max(num1, num2, num3) #finiding the maximum of the three numbers
num1= float(input("Enter first value:"))
num2= float(input("Enter second value:"))
num3= float(input("Enter third value:"))
print("Maximum number is:", built_in_functions_max(num1, num2, num3))

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    return min(num1, num2, num3) #finiding the minimum of the three numbers
num1= float(input("Enter first value:"))
num2= float(input("Enter second value:"))
num3= float(input("Enter third value:"))
print("Minimum number is:", built_in_functions_min(num1, num2, num3))

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number > 0:
        print ("The nuumber is positive.")
    elif number < 0:
        print ("The number is negative.")
    else:
        print ("The number is zero.")
number= float(input("Enter a number:"))
check_number(number)

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    for i in range (1, rows + 1):
        print ("*" * i)
rows= int(input("Value of row:"))
star_shape(rows)

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    i = 1 
    while i <= limit:
        if i % 3 == 0: #with modulo we are able to figure out if it is a multilple of 3
            print('Multiple of 3')
        else:
            print(i)
        i += 1
limit= int(input("Enter limit:"))
count_multiples_of_3(limit)


# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
    print("Sum of even numbers:", total)
start= int(input("Enter start value:"))
end= int(input("Enter end value:"))
sum_of_even_numbers(start, end)


