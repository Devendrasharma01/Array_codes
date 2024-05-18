# Write a program to Find the occurrence of an integer in the array?

def re_occurence(array,key):
    count = 0
    for i in range(0, len(array)):
        if key == array[i]:
            count +=1
        elif key != array[i]:
            continue
        else:
            print(f"Entered element is not in array: {key}")
    print(count)



input_string = input("Enter a list of number with space: ")
input_list = input_string.split()
array = [int(num) for num in input_list]
print("The input array is: ",array)
check_element = int(input("Enter the element you want to check: "))
re_occurence(array,check_element)
