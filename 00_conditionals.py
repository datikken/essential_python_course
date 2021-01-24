import platform

print('The current python version  is: {}'.format(platform.python_version()))

x = 42
y = 73

if x > y:
    print('x > y: x is {} and y is {}'.format(x, y))
elif x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
else:
    print('do some')

hungry = False
x = 'feed the bear' if hungry else 'do not feed the bear'

print(x)