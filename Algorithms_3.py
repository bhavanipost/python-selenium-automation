
#Task 1. Two Lowest Elements
#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.


#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def find_two_lowest(arr: list):
    lowest_items = []
    min_value = None
    for val in range(2):
        min_value = arr[0]
        for item in arr:
            if min_value > item:
                min_value = item
        arr.remove(min_value)
        lowest_items.append(min_value)
    return lowest_items

print("two lowest items")
print(find_two_lowest([198, 3, 4, 9, 10, 9, 2]))


#Task 2
#Given a list of numbers, return the inverse of each. Each positive becomes a negative, and the negatives become positives.

#Example:
#Input: [1, 5, -2, 4]
#Output: [-1, -5, 2, -4]
# Loop through each index of the array

def invert_list(arr: list):
    reverseList = []
    for i in range(len(arr)):
        reverseList.append(arr[len(arr)-(i+1)] * -1)
    return reverseList

print(invert_list([-1, -5, 2, -4]))


#Task 3
#Implement a function that returns the difference between the largest and the smallest value in a given list.
#The list contains positive and negative numbers. All elements are unique.

#Example:
#Input: [3, 5, 7, 2]
#Output: 5 - 2 = 3



def max_diff(arr: list):
    if len(arr) == 0:
        return 0
    arr.sort()
    diff_arr = arr[-1] - arr[0]
    return diff_arr

d_list = [3, 5, 7, 2]
print(max_diff(d_list))


#Task 4
#Write a function that counts the number of elements in a given list larger than their adjacent neighbors.

#Example:
#Input: [2, 56, 7, 21, 22, 19, 26]
#Output: 3 (56, 22)

def count_larger_neighbors(arr: list):
    emt_list = []
    count = 0
    for i in range(1, len(arr) - 1):
        if (arr[i]) > (arr[i - 1]) and (arr[i]) > (arr[i + 1]):
             n1 = arr[i]
        elif (arr[i - 1]) > (arr[i]) and (arr[i -1]) >(arr[i + 1]):
             n1 = arr[i - 1]
        else:
            n1 = arr[i + 1]
        count += 1
        emt_list.append(n1)
    return (count, emt_list)
cnl =  [2, 56, 7, 21, 22, 19, 26]
print(count_larger_neighbors(cnl))

#Task 5
#Given an array. Find the minimum element in the list and subtract it from each element in the array.

#Example:
#Input: [9, 2, 5, 4, 7, 6, 1]
#The minimum element in the list: 1
#Output: [8, 1, 4, 3, 6, 5, 0]

def subtract_min(arr: list):
    min_element = min(arr)
    list_n1 =[]
    for sm in arr:
        n = sm - min_element
        list_n1.append(n)
    return list_n1
sl1 = [9, 2, 5, 4, 7, 6, 1]
print(subtract_min(sl1))



