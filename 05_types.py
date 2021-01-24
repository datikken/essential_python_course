from decimal import *

x = 7

print('x is {}'.format(x))
print(type(x))

# strings are objects in python
string = 'seven'.lower()

print('number is {}'.format(string))
print(type(string))

# numeric type int and float
a = Decimal('.1')
b = Decimal('.2')

x = a + a + a + a - b

print('x is {}'.format(x))
print(type(x))

# Boolean
t = 7 < 5
print('x is {}'.format(t))
print(type(t))

no = None

# sequence 1.tuple
s = (1, 2, 3, 4, 5)
for i in s:
    print('s is {}'.format(i))

# dictionary
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
x['three'] = 'new key'

for k, v in x.items():
    print('k: {}, v: {}'.format(k, v))

tuples = (1, 'string', 3, 4)
print('x is {}'.format(tuples))
print(type(tuples[1]))