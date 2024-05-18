# Write a program to reverse an array?

def arr_reverce(array):
    reversed_array = list(reversed(array))
    print(reversed_array)
                

input_string = input("Enter a list of number with space: ")
input_list = input_string.split()
array = [int(num) for num in input_list]
print("The input array is: ",array)
arr_reverce(array)