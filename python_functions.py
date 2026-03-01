# 1. difference: this function takes in two parameters and returns the difference between the two

from codecs import charmap_build
from re import A


def difference(a, b):
    return a - b

print(difference(2, 2))
print(difference(2, 0))

# 2. print_day: this function takes in one parameter (a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.). If the number is less than 1 or greater than 7, the function should return None

def print_day(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if num < 1 or num > 7:
        return None
    return days[num - 1]

print(print_day(3))
print(print_day(41))

# 3. last_element: this function takes in one parameter (a list) and returns the last value in the list. It should return None if the list is empty.

def last_element(lst):
    if lst == []:
        return None
    return lst[-1]
print(last_element([1,2,3,4]))
print(last_element([]))

# 4. number_compare: this function takes in two parameters (both numbers). If the first is greater than the second, this function returns “First is greater.” If the second number is greater than the first, the function returns “Second is greater.” Otherwise the function returns “Numbers are equal.”

def number_compare (a, b):
    if a > b: 
        return "First is greater"
    elif b > a:
         return "Second is greater"
    else:
         return "Numbers are equal"

print(number_compare(1,2))

# 5. single_letter_count: this function takes in two parameters (two strings). The first parameter should be a word and the second should be a letter. The function returns the number of times that letter appears in the word. The function should be case insensitive (does not matter if the input is lowercase or uppercase). If the letter is not found in the word, the function should return 0.

def single_letter_count (word, letter):
    return word.lower().count(letter.lower())

print(single_letter_count("Amazing", "a"))

# 6. multiple_letter_count: this function takes in one parameter (a string) and returns a dictionary with the keys being the letters and the values being the count of the letter

def multiple_letter_count(string):
    return {k:string.count(k) for k in string}

print(multiple_letter_count("hello"))

# 7. list_manipulation: this function should take in three parameters (a list, command, location and value).

"""
If the command is “remove” and the location is “end”, the function should remove the last value in the list and return the value removed
If the command is “remove” and the location is “beginning”, the function should remove the first value in the list and return the value removed
If the command is “add” and the location is “beginning”, the function should add the value (fourth parameter) to the beginning of the list and return the list
If the command is “add” and the location is “end”, the function should add the value (fourth parameter) to the end of the list and return the list

"""

def list_manipulation (lst, command, location, value = None):
    if command == "remove" and location == "end":
        return lst.pop()
    elif command == "remove" and location == "beginning":
        return lst.pop(0)
    elif command == "add" and location == "beginning":
        lst.insert(0, value)
        return lst
    elif command == "add" and location == "end":
        lst.append(value)
        return lst

print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))

# 8. is_palindrome: A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This function should take in one parameter and returns True or False depending on whether it is a palindrome. As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama') returns True.

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome("hannah"))

# 9. frequency: This function accepts a list and a search_term (this will always be a primitive value) and returns the number of times the search_term appears in the list.

def frequency (lst, search_term):
    return lst.count(search_term)

print(frequency([1,2,3,4,4,4,], 4))

# 10. flip_case: This function accepts a string and a letter and reverses the case of all occurances of the letter in the string.

def flip_case (string, letter):
    result = ""
    for char in string:
        if char.lower() == letter.lower():
            result += char.swapcase()
        else:
            result += char
    return result

print(flip_case("Hardy har har", "h"))

# 11. multiply_even_numbers: This function accepts a list of numbers and returns the product of all even numbers in the list.
def multiply_even_numbers (lst):
    result = 1
    for num in lst:
        if num % 2 == 0:
            result *= num
    return result

print(multiply_even_numbers([2,3,4,5,6]))

# 12. mode: This function accepts a list of numbers and returns the most frequent number in the list of numbers. You can assume that the mode will be unique.

def mode (lst):
    counts = {n: lst.count(n) for n in lst}
    return max(counts, key = counts.get)

print(mode([1,2,4,4,4,5,6,7]))

# 13. capitalize: This function accepts a string and returns the same string with the first letter capitalized.

def capitalize (string):
    return string.capitalize()

print(capitalize("tim"))

# 14. compact: This function accepts a list and returns a list of values that are truthy values.

def compact (lst):
    return [v for v in lst if v]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))

# 15. partition: This function accepts a list and a callback function (which you can assume returns True or False). The function should iterate over each element in the list and invoke the callback function at each iteration. If the result of the callback function is True, the element should go into one list if it’s False, the element should go into another list. When it’s finished, partition should return both lists inside of one larger list.

def partition (lst, fn):
    true_list = []
    false_list = []
    for val in lst:
        if fn(val):
            true_list.append(val)
        else: 
            false_list.append(val)
    return [true_list, false_list]

def is_even(num):
    return num % 2 == 0

print(partition([1,2,3,4], is_even))

# 16. intersection: This function should accept a two dimensional list and return a list with the values that are the same in each list.

def intersection (lst1, lst2):
    return [n for n in lst1 if n in lst2]

print(intersection([1,2,3], [2,3,4]))

# 17. once: This function accepts a function and returns a new function that can only be invoked once. If the function is invoked more than once, it should return None. Hint you will need to define a new function inside of your once function and return that function. You can add properties to your inner function to see if it has run already.

def once (fn):
    def inner(*args):
        if inner.called:
            return None
        inner.called = True
        return fn(*args)
    inner.called = False
    return inner

def add (a, b):
    return a+b

one_addition = once(add)
print(one_addition(2, 2))
print(one_addition(2, 2))

# Bonus: Research what decorators are and refactor your once code to use a decorator so that you can run

@once
def add(a,b):
    return a + b
