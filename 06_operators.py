x = 0x0a
y = 0x02
z = x & y

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

#boolean operators
#and
#or
#not
#in
#not in
#is
#is not

a = True
b = False

x = ('htc', 'cbd', 'xts', 'lsd')
y = 'junkie'

if a or b:
    print('expression is true')
else:
    print('expression is false')

print(id(y))
print(id(x[0]))