# Write the following Python code to do the following (complete ALL of these using list comprehension).

# 1. Given a list [1,2,3,4], print out all the values in the list.

print([n for n in [1, 2, 3, 4]])

# 2. Given a list [1,2,3,4], print out all the values in the list multiplied by 20.

print([n * 20 for n in [1,2,3,4]])

# 3. Given a list [“Elie”, “Tim”, “Matt”], return a new list with only the first letter ([“E”, “T”, “M”]).

print([n[0] for n in ["Ellie", "Tim", "Matt"]])

# 4. Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).

print([n for n in [1,2,3,4,5,6] if n % 2 == 0])

# or 

print([n for n in range(1,7) if n % 2 == 0])

# 5. Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).

print([n for n in [1,2,3,4] if n in [3,4,5,6]])

# 6. Given a list of words [“Elie”, “Tim”, “Matt”] return a new list with each word reversed and in lower case ([‘eile’, ‘mit’, ‘ttam’]).

names = ["Elie", "Tim", "Matt"]
print([name[::-1].lower() for name in names])

# or 

print([name[::-1].lower() for name in ["Ellie", "Tim", "Matt"]])


# 7. Given two strings “first” and “third”, return a new string with all the letters present in both words ([“i”, “r”, “t”]).

print([n for n in "first" if n in "third"])

# 8. For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).

print([n for n in range(1,101) if n % 12 == 0])

# 9. Given the string “amazing”, return a list with all the vowels removed ([‘m’, ‘z’, ‘n’, ‘g’]).

print([n for n in "amazing" if n not in "aeiou"])

# 10. Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].

print([[i for i in range(3)] for _ in range(3)])

"""
11. Generate a list with the value:

 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
]
"""
print([[i for i in range(10)] for _ in range(10)])