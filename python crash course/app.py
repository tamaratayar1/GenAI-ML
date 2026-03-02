from helpers import add, subtract

def calculate_numbers(a, b, fn):
    if fn == "add":
        return add(a,b)
    elif fn == "subtract":
        return subtract(a,b)

print(calculate_numbers(1, 4, "add"))
print(calculate_numbers(1, 4, 'subtract'))

from collections import Counter
l = [1,1,2,3,3,4,4,5,5]
print(Counter(l))

string = "aweosakjdsaldwjdwq"
print(Counter(string)) 

s = 'this is such a nice nice nice thing that is nice!'
print(Counter(s.split())) 

d = {}
d['one'] = 1
d['two'] = 2
d['three'] = 3
d['four'] = 4

for k,v in d.items():
    print(k,v)

