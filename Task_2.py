#Write a program to cyclically rotate the array clockwise by one time.?

def cyclically(array):
    if len(array) == 0:
        print("array")
    
    last_element = array[-1]

    for i in range(len(array) - 1, 0 , -1 ):
        array[i] = array[i-1]
    array[0] = last_element
    print(array)

input_string = input("Enter a list of number with space: ")
input_list = input_string.split()
array = [int(num) for num in input_list]
print("The input array is: ",array)
cyclically(array)
