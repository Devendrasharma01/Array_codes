#Write a program to find the minimum and maximum elements in an array?

def find_min_max(array):
    max_value = max(array)
    min_value = min(array)
    print(f"The minimum value in array is: {min_value}, and maximum value is: {max_value} ")

input_string = input("Enter a list of number with space: ")
input_list = input_string.split()
array = [int(num) for num in input_list]
print("The input array is: ",array)
find_min_max(array)