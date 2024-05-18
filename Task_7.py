# Write a program to find a number that occurs an odd number of times in a given array of positive integers. In the array, all numbers occur an even number of times.

def odd_occur(array):
    repeat = 0
    str_num = ""
    for num in array:
        repeat ^= num
       
    print(repeat)
     


input_string = input("Enter the list of elements with space: ")
input_list = input_string.split()
array = [int(num) for num in input_list]
print(f"The array is: {array}")
odd_occur(array)