# Write a program to separate even and odd numbers in an array of integers. Put all even numbers first, and then odd numbers.?

def odd_eve_seperator(array):
    even_num = [num for num in array if num % 2 == 0]
    odd_num = [num for num in array if num % 2 != 0]

    return even_num + odd_num

    



input_string = input("Enter a list of number with space: ")
input_list = input_string.split()
array = [int(num) for num in input_list]
print("The input array is: ",array)
segregate = odd_eve_seperator(array)
print(segregate)