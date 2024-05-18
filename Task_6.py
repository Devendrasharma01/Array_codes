# Write a program to sort a given array of 0s, 1s and 2s. In the final array put all 0s first, then all 1s and all 2s last.

def sort_arr(array):
    low,mid,high = 0 , 0 , len(array)-1
    while mid <= high:
        if array[mid] == 0:
           array[low],array[mid] = array[mid],array[low]
           low += 1
           mid += 1
        elif array[mid] == 1:
            mid +=1
        else:
            array[mid],array[high] = array[high],array[mid]
            high -= 1
    print(array)


input_string = input("Enter the list of elements with space: ")
input_list = input_string.split()
array = [int(num) for num in input_list]
print(f"The array is: {array}")
sort_arr(array)