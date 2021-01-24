letters = ['a', 'b', 'c']

n = 0
while (n < 3):
    print(letters[n])
    n += 1

#fibonacci example
a,b = 0,1

while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b


animals = ('bear', 'bunny', 'dog', 'cat')

for pet in animals:
    if pet == 'dog': continue
    if pet == 'bear': continue
    print(pet)
else:
    print('that is all of the animals')



secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 3

while pw != secret:
    count += 1
    if count > max_attempt: break
    pw = input(f"{count}: What's the secret word? ")

print("Authorized" if auth else "Raising a strap...")

