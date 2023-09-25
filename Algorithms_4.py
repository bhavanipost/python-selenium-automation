# 1. Sum and multiplication of even and odd numbers.
# You are given an array of integers. Your task is to calculate two values: the sum of all even numbers and the product of all odd numbers in the array. Please return these two values as a list [sum_even, product_odd].
#
# Example
# For the array [1, 2, 3, 4]:
#
# The sum of all even numbers is 2 + 4 = 6.
# The product of all odd numbers is 1 * 3 = 3.
# The function should return the list [6, 3].

def sum_even_and_product_odd(arr: list):
    # Initialize variables for the sum of even numbers and the product of odd numbers
    sum_even = 0
    product_odd = 1

    for num in arr:
        if num % 2 == 0:
            sum_even += num
        else:
            product_odd *= num

    result = []
    result.append(sum_even)
    result.append(product_odd)

    return result
    #print(arr)
    #print(result)

print(sum_even_and_product_odd([1, 2, 3, 4]))


# 2.Sum between range values
# You are given an array of integers and two integer values, min and max. Your task is to write a function that finds the sum of all elements in the array that fall within the range [min, max], inclusive.
#
# Example
# arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
# min_val = 3
# max_val = 7
#
# Output: 25 (3 + 4 + 5 + 6 + 7)

def sum_between_range(arr: list, min_val: int, max_val: int):
    sum_value = 0
    for num in arr:
        if num >= min_val and num <= max_val:
            sum_value += num

    return sum_value

my_array = [5, 6, 9, 2, 10, 3]
min_value = [3]
max_value = [9]
print(sum_between_range([5, 6, 9, 2, 10, 3], 3, 9))


# 3, Stock price 2
# You are given an array of prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
# You may complete as many transactions as you like (buy one and sell one share of the stock multiple times).
#
# Example: prices = [7, 1, 5, 3, 6, 4] Return: 7
#
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

# Define a function that takes a list of stock prices as its argument

    # Initialize the variable 'maximum' to store the maximum profit, starting at 0
   # maximum = 0

    # Loop through the list of prices; stop one element before the last to avoid index out-of-bounds

# Check if the next day's price is higher than the current day's

# If it is, add the difference between the two prices to 'maximum'

# Return the calculated maximum profit after the loop ends

def buy_and_sell_stock(prices: list):
    maximum = 0
    total_days = len(prices)

    for i in range(total_days-1):
        if prices[i] < prices[i+1]:
            maximum += prices[i+1] - prices[i]

    return maximum

print(buy_and_sell_stock([7, 1, 5, 3, 6, 4]))
#print(buy_and_sell_stock([5, 5, 10, 12, 6, 9]))


# 4 Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the list to [1, 3, 0].


def plus_one(arr: list):
    # Add 1 to the last digit
    arr[-1] += 1

    # Loop through the digits in reverse order
    for i in range(len(arr) - 1, 0, -1): # 2, 1, 0
        # Check for carry-over
        if arr[i] == 10:
            arr[i] = 0
            arr[i - 1] += 1
        else:
            break  # No more carry-over, exit the loop

    # Special case: If the first digit is 10, change it to 1 and add a 0 at the end
    if arr[0] == 10:
        arr[0] = 0
        arr.insert(0,1)

# Example usage:
input_digits = [9, 9 ,9]
plus_one(input_digits)
print(input_digits)

def plus_one(arr: list):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        else:
            arr[i] = 0
            arr[i-1] += 1

    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr

test_data = [9, 9, 9]
print(plus_one(test_data))



