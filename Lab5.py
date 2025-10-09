# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    i = 1 #number of rows
    square= ""
    while i <= n:
        if i == 1 or i == n: #first or last row
            square += '*' * n + '\n' 
        else:
            square += '*' + ' ' * (n - 2) + '*' + '\n' #middle rows
        i += 1 
    return square
n = int(input("Enter the size of the square: "))
print(hollow_square(n))

# 1
# 12
# 123
# 1234
def number_pattern(n):
    i = 1 #couts rows
    pattern= ""
    while i <= n: #for each row
        j = 1 #counts numbers in each row/number we're adding
        while j <= i: 
            pattern += str(j) 
            j += 1 
        pattern += '\n' 
        i += 1
    return pattern
n = int(input("Enter the number of rows: "))
print(number_pattern(n))

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0 
    count = 1 
    while count <= n: #counting from 1 to n
        total += count 
        count += 1 
    return total
n = int(input("Enter a positive integer: "))
print("Sum of first", n, "natural numbers is:", sum_of_natural_numbers(n))

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    i= 1 #counts rows
    pyramid= "" 
    while i <= n:
        spaces = ' ' * (n - i) #number of spaces before stars
        stars = '*' * (2 * i - 1) #number of stars in each row
        pyramid += spaces + stars + '\n' #constructing each row/separating rows
        i += 1
    return pyramid
n = int(input("Enter the number of rows: "))
print(centered_star_pyramid(n))