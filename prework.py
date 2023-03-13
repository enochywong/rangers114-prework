# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(username):
    """Display username from user input"""
    print(f"Hello {username.title()}!")


hello_name("john")


# Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Print the odd numbers from 1 - 100"""
    number = 1
    while number < 101:
        if number % 2 == 1:
            print(number)
            number += 1
        else:
            number += 1

# Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Return the max number of a given list"""
    max_number = max(a_list)
    return max_number


# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """To determine a given year is leap year or not and return boolean type"""
    if a_year % 4 == 0 and a_year % 100 != 0:
        leap_year = True
        return leap_year
    elif a_year % 4 == 0 and a_year % 400 == 0:
        leap_year = True
        return leap_year
    else:
        leap_year = False
        return leap_year


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    """To check if all numbers in a list are consecutive numbers. Return boolean type"""

    a_list_sorted = a_list.sort()
    counter = 1
    index_1 = -1
    index_2 = -2
    while counter != len(a_list):
        if a_list_sorted[index_2] - a_list_sorted[index_1] == 1:
            counter += counter
            index_1 -= index_1
            index_2 -= index_2
        else:
            consecutive_numbers = False
            return consecutive_numbers
    consecutive_numbers = True
    return consecutive_numbers





