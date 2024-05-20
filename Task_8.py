 #Find duplicates in O(n) time and O(1) extra space Given an array of n elements that contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and use only constant memory space.


def print_duplicates(arr):
    n = len(arr)
    for i in range(n):
        index = arr[i] % n
        arr[index] += n

    for i in range(n):
        if (arr[i]//n) > 1:
            print(i, end=" ")

input_string = input("Enter the list of elements with space: ")
input_list = input_string.split()
array = [int(num) for num in input_list]
print(f"The array is: {array}")
print_duplicates(array)
