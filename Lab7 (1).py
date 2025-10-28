import numpy as np

# Function 1: Rotate the Array
# This function creates an array of a specified size, fills it with numbers starting from `starting_integer` and increasing by 3,
# then rotates elements at even indices 2 positions to the left.
def rotate_the_array(array_size, starting_integer):
    # initialize an array of array_size with all zeros
    the_array = [0] * array_size

    # fill the array with values increasing by 3 each time
    for i in range(array_size):
        the_array[i] = starting_integer + (3 * i)

    # Testing
    print("Original array:", the_array)

    # rotate elements at even indices two positions to the left
    for i in range(0, array_size - 2, 2):
        temp = the_array[i]
        the_array[i] = the_array[i + 2]
        the_array[i + 2] = temp

    # Testing
    print("Rotated array:", the_array)

    return the_array

# Example test
rotate_the_array(6, 2)




