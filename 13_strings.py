class MyString(str):
    def __str(self):
        return self[::-1]


# casefold removes all case destinctions in unicode
s = MyString('Hello, world').casefold()
print(s)

x = 42
y = 73

print('The number is {} {}'.format(x, y))