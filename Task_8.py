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
